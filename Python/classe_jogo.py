import pygame 
import os
import random 

# locals é um submodo de pygame, * importa todas as funçoes e constantes do locals
from pygame.locals import *; 
#função para fechar a janela quando solicitado
from sys import exit; 

# inicializa o Pygame
pygame.init()

# define o tamanho da janela do jogo
LARGURA = 800
ALTURA = 600
largura_item = 80
espaco_vitrine = 20

class Jogo:
    def __init__(self):
        # inicializa o Pygame
        pygame.init()

        # cria a tela do jogo
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption('Spider Shopping')
        
        # define a fonte usada no jogo
        self.fonte = pygame.font.Font(None, 30)
        
        def carrega_imagem(nome_arquivo):
            imagem = pygame.image.load(nome_arquivo)
            return imagem
        
        # define a lista de compras
        self.lista_compras = []
        self.prateleira = {'pao': carrega_imagem('imagens_jogo\\pao.png'),
                            'leite': carrega_imagem('imagens_jogo\leit.png'),
                            'arroz': carrega_imagem('imagens_jogo\\arroz.png'),
                            "açucar":  carrega_imagem('imagens_jogo\açucar.png'),
                            "biscoito":  carrega_imagem('imagens_jogo\biscoito.png'),
                            "café": carrega_imagem('imagens_jogo\\cafe.png'),
                            "escova": carrega_imagem('imagens_jogo\\escova.png'),
                            "feijão": carrega_imagem('imagens_jogo\\feijao.png'),
                            "macarrao": carrega_imagem('imagens_jogo\\macarrao.png'),
                            "oleo": carrega_imagem('imagens_jogo\\oleo.png'),
                            "pasta de dente": carrega_imagem('imagens_jogo\\pasta.png'),
                            "sal": carrega_imagem('imagens_jogo\\sal.png')
                            }
        
        # define o carrinho de compras
        self.carrinho_compras = []
        self.qtd_itens_carrinho = {}

        # define o nível de dificuldade
        self.nivel_jogo = None
        self.configura_nivel('Fácil')

        # define o loop principal do jogo
        self.loop_jogo()

        def carrega_imagem(self, nome_arquivo):
            # carrega uma imagem da prateleira
            caminho = os.path.join('imagens_jogo', nome_arquivo)
            imagem = pygame.image.load(caminho).convert_alpha()
            return imagem

        def configura_nivel(self, nivel):
            if nivel == 'Fácil':
                self.nivel_jogo = nivel
                self.n_itens = 4
                self.velocidade_vitrine = 2
                self.espaco_vitrine = 50
            elif nivel == 'Médio':
                self.nivel_jogo = nivel
                self.n_itens = 6
                self.velocidade_vitrine = 30
            elif nivel == 'Difícil':
                self.nivel_jogo = nivel
                self.n_itens = 8
                self.velocidade_vitrine = 4
                self.espaco_vitrine = 20


        # define o loop principal do jogo
        self.loop_jogo()

        def carrega_imagem(self):
        # carrega uma imagem aleatória da prateleira
            nome_item = random.choice(self.prateleira)
            imagem_item = pygame.image.load(nome_item + '.png').convert_alpha()
            return imagem_item

        def novo_item_vitrine(self):
            # cria um novo item na vitrine
            imagem_item = self.carrega_imagem()
            largura_item = imagem_item.get_width()
            altura_item = imagem_item.get_height()
            x_item = LARGURA
            y_item = random.randint(50, ALTURA - altura_item - 50)
            retangulo_item = pygame.Rect(x_item, y_item, largura_item, altura_item)
            nome_item = imagem_item.filename.split('.')[0]
            return {'imagem': imagem_item, 'retangulo': retangulo_item, 'nome': nome_item}

        def loop_jogo(self):
            # define o loop principal do jogo
            while True:
                # processa os eventos do Pygame
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                # atualiza a posição dos itens na vitrine
                for item in self.itens_vitrine:
                    item['retangulo'].move_ip(-self.velocidade_vitrine, 0)
                    if item['retangulo'].right < 0:
                        # o item saiu da tela, coloca-o no final da vitrine
                        novo_x = max([item['retangulo'].right for item in self.itens_vitrine]) + self.largura_item + self.espaco_vitrine
                        item['retangulo'].move_ip(novo_x - item['retangulo'].left, 0)

                # adiciona novos itens na vitrine se necessário
                while len(self.itens_vitrine) < self.n_itens:
                    novo_item = self.gera_item_vitrine()
                    self.itens_vitrine.append(novo_item)