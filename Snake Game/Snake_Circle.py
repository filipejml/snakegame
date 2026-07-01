import random
import sys
from collections import deque
from pathlib import Path

import pygame
from pygame.locals import (
    KEYDOWN,
    K_DOWN,
    K_ESCAPE,
    K_LEFT,
    K_p,
    K_q,
    K_r,
    K_RETURN,
    K_RIGHT,
    K_SPACE,
    K_UP,
    QUIT,
)


LARGURA = 640
ALTURA = 480
TAMANHO_CELULA = 20

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

FASES = [
    {
        "nome": "Jardim Neon",
        "pontuacao_minima": 0,
        "velocidade": 5,
        "cores_maca": [(255, 80, 80), (80, 255, 140), (80, 180, 255)],
        "cor_obstaculo": (90, 90, 120),
        "obstaculos": [],
    },
    {
        "nome": "Labirinto Solar",
        "pontuacao_minima": 10,
        "velocidade": 7,
        "cores_maca": [(255, 220, 40), (255, 130, 30), (255, 70, 160)],
        "cor_obstaculo": (255, 150, 40),
        "obstaculos": [
            (320, 140),
            (320, 160),
            (320, 180),
            (320, 300),
            (320, 320),
            (320, 340),
        ],
    },
    {
        "nome": "Oceano Elétrico",
        "pontuacao_minima": 24,
        "velocidade": 9,
        "cores_maca": [(30, 220, 255), (50, 110, 255), (180, 80, 255)],
        "cor_obstaculo": (40, 120, 210),
        "obstaculos": [
            (180, 160),
            (200, 160),
            (220, 160),
            (400, 300),
            (420, 300),
            (440, 300),
            (300, 220),
            (320, 220),
            (340, 220),
        ],
    },
    {
        "nome": "Caos Cromático",
        "pontuacao_minima": 40,
        "velocidade": 12,
        "cores_maca": [
            (255, 40, 40),
            (40, 255, 80),
            (40, 120, 255),
            (255, 230, 30),
            (220, 50, 255),
            (30, 255, 240),
        ],
        "cor_obstaculo": (210, 60, 210),
        "obstaculos": [
            (160, 140),
            (160, 160),
            (160, 180),
            (460, 280),
            (460, 300),
            (460, 320),
            (280, 120),
            (300, 120),
            (320, 120),
            (340, 120),
            (280, 360),
            (300, 360),
            (320, 360),
            (340, 360),
        ],
    },
]


class Cobra:
    def __init__(self):
        self.raio = 10
        self.reiniciar()

    def reiniciar(self):
        self.segmentos = deque(
            [{"pos": (200, 200), "cor": (255, 255, 255)}]
        )
        self.direcao = LEFT

    @property
    def cabeca(self):
        return self.segmentos[0]

    def posicoes(self):
        return {segmento["pos"] for segmento in self.segmentos}

    def mudar_direcao(self, nova_direcao):
        direcoes_opostas = {
            UP: DOWN,
            DOWN: UP,
            LEFT: RIGHT,
            RIGHT: LEFT,
        }
        if nova_direcao != direcoes_opostas[self.direcao]:
            self.direcao = nova_direcao

    def adicionar_ao_final(self, cor):
        novo_segmento = {"pos": self.segmentos[-1]["pos"], "cor": cor}
        self.segmentos.append(novo_segmento)

    def retirar_do_inicio(self):
        if len(self.segmentos) > 1:
            return self.segmentos.popleft()
        return None

    def mover(self):
        for indice in range(len(self.segmentos) - 1, 0, -1):
            self.segmentos[indice]["pos"] = self.segmentos[indice - 1]["pos"]

        x, y = self.cabeca["pos"]
        deslocamentos = {
            UP: (0, -TAMANHO_CELULA),
            DOWN: (0, TAMANHO_CELULA),
            RIGHT: (TAMANHO_CELULA, 0),
            LEFT: (-TAMANHO_CELULA, 0),
        }
        dx, dy = deslocamentos[self.direcao]
        self.cabeca["pos"] = (x + dx, y + dy)

    def colidiu_com_corpo(self):
        posicao_cabeca = self.cabeca["pos"]
        return any(
            segmento["pos"] == posicao_cabeca
            for segmento in list(self.segmentos)[1:]
        )

    def colidiu_com_borda(self):
        x, y = self.cabeca["pos"]
        return x < 0 or x >= LARGURA or y < 0 or y >= ALTURA

    def desenhar(self, tela):
        for segmento in self.segmentos:
            pygame.draw.circle(
                tela, segmento["cor"], segmento["pos"], self.raio
            )


class Maca:
    def __init__(self):
        self.raio = 10
        self.posicao = (0, 0)
        self.cor = (255, 0, 0)

    def gerar(self, cobra, obstaculos, cores):
        posicoes_ocupadas = cobra.posicoes().union(obstaculos)
        posicoes_livres = [
            (x, y)
            for x in range(20, 620, TAMANHO_CELULA)
            for y in range(20, 460, TAMANHO_CELULA)
            if (x, y) not in posicoes_ocupadas
        ]
        self.posicao = random.choice(posicoes_livres)
        self.cor = random.choice(cores)

    def descrever_efeito(self, cobra):
        if cobra.cabeca["cor"] != self.cor:
            return "Adicionar no fim (+2 pontos)"
        if len(cobra.segmentos) > 1:
            return "Retirar do início (-1 ponto)"
        return "Sem efeito: tamanho mínimo"

    def desenhar(self, tela):
        pygame.draw.circle(tela, self.cor, self.posicao, self.raio)


class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.fonte = pygame.font.SysFont("lexend", 24)
        self.fonte_titulo = pygame.font.SysFont("lexend", 48)

        self.caminho_recorde = (
            Path(__file__).resolve().parent.parent / "recorde.txt"
        )
        self.recorde = self.carregar_recorde()
        self.menu_ativo = True
        self.pausado = False
        self.game_over = False
        self.reiniciar()

    def carregar_recorde(self):
        try:
            return int(self.caminho_recorde.read_text(encoding="utf-8"))
        except (FileNotFoundError, ValueError):
            return 0

    def salvar_recorde(self):
        self.caminho_recorde.write_text(str(self.recorde), encoding="utf-8")

    def obter_fase(self):
        fase = FASES[0]
        for candidata in FASES:
            if self.pontuacao >= candidata["pontuacao_minima"]:
                fase = candidata
        return fase

    def configurar_fase(self):
        nova_fase = self.obter_fase()
        mudou_de_fase = nova_fase is not self.fase_atual
        if mudou_de_fase:
            self.fase_atual = nova_fase
            posicoes_cobra = self.cobra.posicoes()
            self.obstaculos = [
                posicao
                for posicao in self.fase_atual["obstaculos"]
                if posicao not in posicoes_cobra
            ]
        return mudou_de_fase

    def reiniciar(self):
        self.cobra = Cobra()
        self.maca = Maca()
        self.pontuacao = 0
        self.fase_atual = FASES[0]
        self.obstaculos = list(self.fase_atual["obstaculos"])
        self.maca.gerar(
            self.cobra, self.obstaculos, self.fase_atual["cores_maca"]
        )
        self.pausado = False
        self.game_over = False

    def encerrar(self):
        self.salvar_recorde()
        pygame.quit()
        sys.exit()

    def processar_eventos(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.encerrar()

            if event.type != KEYDOWN:
                continue

            if event.key in (K_q, K_ESCAPE):
                self.encerrar()

            if self.menu_ativo:
                if event.key in (K_RETURN, K_SPACE):
                    self.menu_ativo = False
                continue

            if self.game_over:
                if event.key == K_r:
                    self.reiniciar()
                continue

            if event.key == K_p:
                self.pausado = not self.pausado
                continue

            if self.pausado:
                continue

            controles = {
                K_UP: UP,
                K_DOWN: DOWN,
                K_RIGHT: RIGHT,
                K_LEFT: LEFT,
            }
            if event.key in controles:
                self.cobra.mudar_direcao(controles[event.key])

    def atualizar(self):
        if self.menu_ativo or self.pausado or self.game_over:
            return

        self.cobra.mover()
        if (
            self.cobra.colidiu_com_corpo()
            or self.cobra.colidiu_com_borda()
            or self.cobra.cabeca["pos"] in self.obstaculos
        ):
            self.game_over = True
            return

        if self.cobra.cabeca["pos"] == self.maca.posicao:
            if self.cobra.cabeca["cor"] == self.maca.cor:
                if self.cobra.retirar_do_inicio() is not None:
                    self.pontuacao -= 1
            else:
                self.cobra.adicionar_ao_final(self.maca.cor)
                self.pontuacao += 2

            self.configurar_fase()
            self.maca.gerar(
                self.cobra,
                self.obstaculos,
                self.fase_atual["cores_maca"],
            )

        if self.pontuacao > self.recorde:
            self.recorde = self.pontuacao
            self.salvar_recorde()

    def desenhar_menu(self):
        titulo = self.fonte_titulo.render(
            "SNAKE COLORIDO", True, (80, 255, 180)
        )
        iniciar = self.fonte.render(
            "Enter ou Espaço: iniciar", True, (255, 255, 255)
        )
        sair = self.fonte.render("Q ou Esc: sair", True, (255, 255, 255))
        self.tela.blit(titulo, titulo.get_rect(center=(320, 170)))
        self.tela.blit(iniciar, iniciar.get_rect(center=(320, 250)))
        self.tela.blit(sair, sair.get_rect(center=(320, 290)))

    def desenhar_obstaculos(self):
        for x, y in self.obstaculos:
            pygame.draw.rect(
                self.tela,
                self.fase_atual["cor_obstaculo"],
                (x - 10, y - 10, TAMANHO_CELULA, TAMANHO_CELULA),
            )

    def desenhar_painel(self):
        textos = [
            ("Pontuação: " + str(self.pontuacao), (10, 10)),
            ("Recorde: " + str(self.recorde), (10, 40)),
            ("Fase: " + self.fase_atual["nome"], (250, 10)),
            (
                "Velocidade: " + str(self.fase_atual["velocidade"]),
                (250, 40),
            ),
            (
                "Próxima maçã: " + self.maca.descrever_efeito(self.cobra),
                (10, 70),
            ),
        ]
        for conteudo, posicao in textos:
            texto = self.fonte.render(conteudo, True, (255, 255, 255))
            self.tela.blit(texto, posicao)

    def desenhar_fim_de_jogo(self):
        mensagem = self.fonte.render(
            f"Fim de jogo! Sua pontuação foi: {self.pontuacao} pontos!",
            True,
            (255, 255, 255),
        )
        reiniciar = self.fonte.render(
            "Pressione R para reiniciar", True, (255, 255, 255)
        )
        sair = self.fonte.render(
            "Pressione Q ou Esc para sair", True, (255, 255, 255)
        )
        self.tela.blit(mensagem, mensagem.get_rect(center=(320, 200)))
        self.tela.blit(reiniciar, reiniciar.get_rect(center=(320, 240)))
        self.tela.blit(sair, sair.get_rect(center=(320, 280)))

    def desenhar_pausa(self):
        titulo = self.fonte_titulo.render("PAUSADO", True, (255, 220, 40))
        continuar = self.fonte.render(
            "P: continuar | Q ou Esc: sair", True, (255, 255, 255)
        )
        self.tela.blit(titulo, titulo.get_rect(center=(320, 210)))
        self.tela.blit(continuar, continuar.get_rect(center=(320, 260)))

    def desenhar(self):
        self.tela.fill((0, 0, 0))

        if self.menu_ativo:
            self.desenhar_menu()
        else:
            self.maca.desenhar(self.tela)
            self.desenhar_obstaculos()
            self.cobra.desenhar(self.tela)
            self.desenhar_painel()

            if self.game_over:
                self.desenhar_fim_de_jogo()
            elif self.pausado:
                self.desenhar_pausa()

        pygame.display.update()

    def executar(self):
        while True:
            self.clock.tick(self.fase_atual["velocidade"])
            self.processar_eventos()
            self.atualizar()
            self.desenhar()


if __name__ == "__main__":
    Jogo().executar()
