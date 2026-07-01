import pygame
from pygame.locals import *
import random
import sys
from collections import deque
from pathlib import Path
from random import randint

# Inicializando o pygame
pygame.init()

# Criando a tela
tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Snake Game")

# Controle de posições
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

FASES = [
    {
        'nome': 'Jardim Neon',
        'pontuacao_minima': 0,
        'velocidade': 5,
        'cores_maca': [(255, 80, 80), (80, 255, 140), (80, 180, 255)],
        'cor_obstaculo': (90, 90, 120),
        'obstaculos': []
    },
    {
        'nome': 'Labirinto Solar',
        'pontuacao_minima': 10,
        'velocidade': 7,
        'cores_maca': [(255, 220, 40), (255, 130, 30), (255, 70, 160)],
        'cor_obstaculo': (255, 150, 40),
        'obstaculos': [(320, 140), (320, 160), (320, 180),
                       (320, 300), (320, 320), (320, 340)]
    },
    {
        'nome': 'Oceano Elétrico',
        'pontuacao_minima': 24,
        'velocidade': 9,
        'cores_maca': [(30, 220, 255), (50, 110, 255), (180, 80, 255)],
        'cor_obstaculo': (40, 120, 210),
        'obstaculos': [(180, 160), (200, 160), (220, 160),
                       (400, 300), (420, 300), (440, 300),
                       (300, 220), (320, 220), (340, 220)]
    },
    {
        'nome': 'Caos Cromático',
        'pontuacao_minima': 40,
        'velocidade': 12,
        'cores_maca': [(255, 40, 40), (40, 255, 80), (40, 120, 255),
                       (255, 230, 30), (220, 50, 255), (30, 255, 240)],
        'cor_obstaculo': (210, 60, 210),
        'obstaculos': [(160, 140), (160, 160), (160, 180),
                       (460, 280), (460, 300), (460, 320),
                       (280, 120), (300, 120), (320, 120), (340, 120),
                       (280, 360), (300, 360), (320, 360), (340, 360)]
    }
]

def obter_fase(pontuacao):
    fase = FASES[0]
    for candidata in FASES:
        if pontuacao >= candidata['pontuacao_minima']:
            fase = candidata
    return fase

# Definindo uma posição aleatória livre para a maçã na tela
def grid_random(cobra, obstaculos):
    posicoes_ocupadas = {segmento['pos'] for segmento in cobra}
    posicoes_ocupadas.update(obstaculos)
    posicoes_livres = [
        (x, y)
        for x in range(20, 620, 20)
        for y in range(20, 460, 20)
        if (x, y) not in posicoes_ocupadas
    ]
    return random.choice(posicoes_livres)

# Definindo colisões
def colisao(c1, c2):
    return c1 == c2

# Operações da fila: elementos entram no fim e saem do início
def adicionar_ao_final(cobra, segmento):
    cobra.append(segmento)

def retirar_do_inicio(cobra):
    return cobra.popleft()

def descrever_efeito_maca(cobra, maca_cor):
    if cobra[0]['cor'] != maca_cor:
        return "Adicionar no fim (+2 pontos)"
    if len(cobra) > 1:
        return "Retirar do início (-1 ponto)"
    return "Sem efeito: tamanho mínimo"

# Criando a cobra
cobra = deque([{'pos': (200, 200), 'cor': (255, 255, 255)}])
raio_cobra = 10

# Definindo a fase inicial
fase_atual = obter_fase(0)
obstaculos = list(fase_atual['obstaculos'])

# Criando a maçã
maca_pos = grid_random(cobra, obstaculos)
raio_maca = 10
maca_cor = random.choice(fase_atual['cores_maca'])

# Iniciando a cobra se movimentando para a esquerda
direcao = LEFT

# Definindo a velocidade do jogo
clock = pygame.time.Clock()   

# Pontuação e recorde
pontuacao = 0
recorde = 0
fonte = pygame.font.SysFont("lexend", 24)
fonte_titulo = pygame.font.SysFont("lexend", 48)
CAMINHO_RECORDE = Path(__file__).resolve().parent.parent / "recorde.txt"

# Estado do jogo
game_over = False
menu_ativo = True
pausado = False

# Carregando o recorde do arquivo
try:
    with CAMINHO_RECORDE.open("r", encoding="utf-8") as arquivo:
        recorde = int(arquivo.read())
except FileNotFoundError:
    pass

def encerrar_jogo():
    with CAMINHO_RECORDE.open("w", encoding="utf-8") as arquivo:
        arquivo.write(str(recorde))
    pygame.quit()
    sys.exit()

# Função para desenhar círculos na tela
def desenhar_circulo(posicao, raio, cor):
    pygame.draw.circle(tela, cor, posicao, raio)

# Loop principal
while True:
    nova_fase = obter_fase(pontuacao)
    if nova_fase is not fase_atual:
        fase_atual = nova_fase
        posicoes_cobra = {segmento['pos'] for segmento in cobra}
        obstaculos = [
            posicao for posicao in fase_atual['obstaculos']
            if posicao not in posicoes_cobra
        ]
        maca_pos = grid_random(cobra, obstaculos)
        maca_cor = random.choice(fase_atual['cores_maca'])

    clock.tick(fase_atual['velocidade'])

    for event in pygame.event.get():
        if event.type == QUIT:
            encerrar_jogo()

        if event.type == KEYDOWN:
            if event.key in (K_q, K_ESCAPE):
                encerrar_jogo()

            if menu_ativo:
                if event.key in (K_RETURN, K_SPACE):
                    menu_ativo = False
                continue

            if game_over:
                if event.key == K_r:
                    # Reiniciando o jogo
                    cobra = deque([{'pos': (200, 200), 'cor': (255, 255, 255)}])
                    fase_atual = obter_fase(0)
                    obstaculos = list(fase_atual['obstaculos'])
                    maca_pos = grid_random(cobra, obstaculos)
                    maca_cor = random.choice(fase_atual['cores_maca'])
                    direcao = LEFT
                    pontuacao = 0
                    pausado = False
                    game_over = False
                continue

            if event.key == K_p:
                pausado = not pausado
                continue

            # Controle de posição
            if not pausado and event.key == K_UP and direcao != DOWN:
                direcao = UP
            elif not pausado and event.key == K_DOWN and direcao != UP:
                direcao = DOWN
            elif not pausado and event.key == K_RIGHT and direcao != LEFT:
                direcao = RIGHT
            elif not pausado and event.key == K_LEFT and direcao != RIGHT:
                direcao = LEFT

    if not menu_ativo and not pausado and not game_over:
        # Testando a colisão com o próprio corpo
        for i in range(1, len(cobra)):
            if colisao(cobra[0]['pos'], cobra[i]['pos']):
                game_over = True

        # Testando a colisão com a borda da tela
        if cobra[0]['pos'][0] < 0 or cobra[0]['pos'][0] >= 640 or cobra[0]['pos'][1] < 0 or cobra[0]['pos'][1] >= 480:
            game_over = True

        # Testando a colisão com os obstáculos da fase
        if cobra[0]['pos'] in obstaculos:
            game_over = True

        if colisao(cobra[0]['pos'], maca_pos):
            maca_pos = grid_random(cobra, obstaculos)

            if cobra[0]['cor'] == maca_cor:
                if len(cobra) > 1:
                    retirar_do_inicio(cobra)
                    pontuacao -= 1
                    print("Cobra atualizada com decréscimo:", cobra)
            else:
                pontuacao += 2
                novo_segmento = {'pos': cobra[-1]['pos'], 'cor': maca_cor}
                adicionar_ao_final(cobra, novo_segmento)
                print("Cobra atualizada com acréscimo:", cobra)
            maca_cor = random.choice(fase_atual['cores_maca'])

        # Movendo o corpo da cobra
        for i in range(len(cobra) - 1, 0, -1):
            cobra[i]['pos'] = cobra[i - 1]['pos']

        # Atualizando a cobra com base na posição atual
        if direcao == UP:
            cobra[0]['pos'] = (cobra[0]['pos'][0], cobra[0]['pos'][1] - 20)
        if direcao == DOWN:
            cobra[0]['pos'] = (cobra[0]['pos'][0], cobra[0]['pos'][1] + 20)
        if direcao == RIGHT:
            cobra[0]['pos'] = (cobra[0]['pos'][0] + 20, cobra[0]['pos'][1])
        if direcao == LEFT:
            cobra[0]['pos'] = (cobra[0]['pos'][0] - 20, cobra[0]['pos'][1])

    # Atualizando o recorde
    if pontuacao > recorde:
        recorde = pontuacao
        with CAMINHO_RECORDE.open("w", encoding="utf-8") as arquivo:
            arquivo.write(str(recorde))

    # Apresentando na tela
    tela.fill((0, 0, 0))

    if menu_ativo:
        titulo = fonte_titulo.render("SNAKE COLORIDO", True, (80, 255, 180))
        iniciar = fonte.render("Enter ou Espaço: iniciar", True, (255, 255, 255))
        sair = fonte.render("Q ou Esc: sair", True, (255, 255, 255))
        tela.blit(titulo, titulo.get_rect(center=(320, 170)))
        tela.blit(iniciar, iniciar.get_rect(center=(320, 250)))
        tela.blit(sair, sair.get_rect(center=(320, 290)))
        pygame.display.update()
        continue

    desenhar_circulo(maca_pos, raio_maca, maca_cor)

    for obstaculo in obstaculos:
        pygame.draw.rect(
            tela,
            fase_atual['cor_obstaculo'],
            (obstaculo[0] - 10, obstaculo[1] - 10, 20, 20)
        )

    for segmento in cobra:
        desenhar_circulo(segmento['pos'], raio_cobra, segmento['cor'])

    if game_over:
        # Exibindo a mensagem de fim de jogo
        mensagem = fonte.render("Fim de jogo! Sua pontuação foi: " + str(pontuacao) + " pontos!", True,
                                (255, 255, 255))
        reiniciar = fonte.render("Pressione a tecla 'r' para reiniciar o jogo", True, (255, 255, 255))
        sair = fonte.render("Pressione 'q' ou Esc para sair", True, (255, 255, 255))
        tela.blit(mensagem, (160, 200))
        tela.blit(reiniciar, (180, 240))
        tela.blit(sair, (190, 280))

    if pausado:
        titulo_pausa = fonte_titulo.render("PAUSADO", True, (255, 220, 40))
        continuar = fonte.render("P: continuar | Q ou Esc: sair", True, (255, 255, 255))
        tela.blit(titulo_pausa, titulo_pausa.get_rect(center=(320, 210)))
        tela.blit(continuar, continuar.get_rect(center=(320, 260)))

    # Exibindo a pontuação e o recorde na tela
    texto_pontuacao = fonte.render("Pontuação: " + str(pontuacao), True, (255, 255, 255))
    texto_recorde = fonte.render("Recorde: " + str(recorde), True, (255, 255, 255))
    texto_fase = fonte.render("Fase: " + fase_atual['nome'], True, (255, 255, 255))
    texto_velocidade = fonte.render(
        "Velocidade: " + str(fase_atual['velocidade']), True, (255, 255, 255)
    )
    texto_efeito = fonte.render(
        "Próxima maçã: " + descrever_efeito_maca(cobra, maca_cor),
        True,
        (255, 255, 255)
    )
    tela.blit(texto_pontuacao, (10, 10))
    tela.blit(texto_recorde, (10, 40))
    tela.blit(texto_fase, (250, 10))
    tela.blit(texto_velocidade, (250, 40))
    tela.blit(texto_efeito, (10, 70))

    # Atualizando a tela
    pygame.display.update()
