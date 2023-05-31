import pygame 
import os
import random 

# locals é um submodo de pygame, * importa todas as funçoes e constantes do locals
from pygame.locals import *; 
#função para fechar a janela quando solicitado
from sys import exit; 

# inicializa o Pygame
pygame.init()

# define as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# define o tamanho da janela do jogo
LARGURA = 800
ALTURA = 600

# define a janela do jogo
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Spider Shopping')

# define a fonte do texto
fonte = pygame.font.SysFont(None, 30)

#criando um fundo de tela
imagem_fundo = pygame.image.load("imagens_botoes\\mercado.png")
imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))

#Variavéis de tempo:
Clock = pygame.time.Clock()
Timer = 5
Tempo_Segundo = 50
intervalo = 1000 # intervalo de tempo para a mudança das imagens

#imagens que serão variaveis

#definindo os botoes de imagem
botao_nome_jogo = pygame.image.load("imagens_botoes\\spider shopping.png").convert_alpha()
botao_iniciar = pygame.image.load("imagens_botoes\\play.png").convert_alpha()
botao_sair = pygame.image.load("imagens_botoes\\exit.png").convert_alpha()
botao_nivel_facil = pygame.image.load("imagens_botoes\\easy.png").convert_alpha()
botao_nivel_medio = pygame.image.load("imagens_botoes\\medium.png").convert_alpha()
botao_nivel_dificil = pygame.image.load("imagens_botoes\\hard.png").convert_alpha()
botao_selecionar_nivel = pygame.image.load("imagens_botoes\\niveis.png").convert_alpha()
botao_voltar = pygame.image.load("imagens_botoes\\voltar.png").convert_alpha()
imagem_carrinho = pygame.image.load('imagens_botoes\\carrinho.png').convert_alpha()
imagem_aranha = pygame.image.load('imagens_botoes\\aranha.png').convert_alpha()

#classe dos botões
class Botao():
    def __init__(self, x, y, image, scale):
       width = image.get_width()
       height = image.get_height()
       self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
       self.rect = self.image.get_rect()
       self.rect.topleft = (x, y)
       self.clicked = False

    def desenhar(self):
        action = False
        #posição do mouse
        pos = pygame.mouse.get_pos()
        
        #checando os clicks
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        #checagem adicional 
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        
        #desenhando o botão na tela
        tela.blit(self.image, (self.rect.x, self.rect.y))
        
        return action
    
    def clicado(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            posicao_mouse = pygame.mouse.get_pos()
            if self.rect == posicao_mouse[0] <= self.rect + self.LARGURA and \
               self.rect == posicao_mouse[1] <= self.rect + self.ALTURA:
                return True
        return False
    
#instanciando os botões
botao_nome_jogo = Botao(200, 150, botao_nome_jogo, 0.6)
botao_iniciar = Botao(100, 200, botao_iniciar, 0.6)
botao_sair = Botao(450, 200, botao_sair, 0.6)
botao_nivel_facil = Botao(50, 200, botao_nivel_facil, 0.6)
botao_nivel_medio = Botao(250, 200, botao_nivel_medio, 0.6)
botao_nivel_dificil = Botao(450, 200, botao_nivel_dificil, 0.6)
botao_selecionar_nivel = Botao(250, 40, botao_selecionar_nivel, 0.6)
botao_voltar = Botao(250, 320, botao_voltar, 0.6)



#controles do jogo
jogo_comecou = False
nivel_selecionado = False


# define a velocidade de rolagem das imagens da vitrine
VELOCIDADE = 5

# definir a função executar_nivel_facil() antes do loop principal
class executar_nivel_facil():
    def __init__(self):
        self.lista_compras = []
        self.prateleira = ['pao', 'leite', 'arroz', 'feijao', 'macarrao', 'oleo', 'acucar',
                      'sal', 'cafe', 'cha', 'biscoito', 'refrigerante', 'suco']
        self.carrinho_compras = []
        self.nivel_jogo = botao_nivel_facil
        self.n_itens = 4
        self.qtd_itens_carrinho = {}

    def carregar_lista_compras(self):
        self.n_itens *= self.nivel_jogo
        for item in range(self.n_itens):
            item = random.choice(self.prateleira)
            self.lista_compras.append(item)
            self.prateleira.remove(item)

    def adicionar_item(self):
        print("Qual item deseja adicionar à lista de compras?")
        item = input()
        if item in self.prateleira:
            self.lista_compras.append(item)
            self.prateleira.remove(item)
            print("Item adicionado à lista de compras.")
        else:
            print("O item não está disponível na prateleira.")

    def remover_item(self):
        print("Qual item deseja remover da lista de compras?")
        item = input()
        if item in self.lista_compras:
            self.prateleira.append(item)
            self.lista_compras.remove(item)
            print("Item removido da lista de compras.")
        else:
            print("O item não está na lista de compras.")

    def editar_lista_compras(self):
        self.carregar_lista_compras()
        while True:
            print("\nItens da Lista de Compras:", self.lista_compras)
            print("Prateleira:", self.prateleira)
            print("Digite 'a' para adicionar um item à lista de compras.")
            print("Digite 'r' para remover um item da lista de compras.")
            print("Digite 'sair' para sair.")
            opcao = input().lower()

            if opcao == 'a':
                self.adicionar_item()
            elif opcao == 'r':
                self.remover_item()
            elif opcao == 'sair':
                break
            else:
                print("Opção inválida.")

    def jogar(self):
        self.editar_lista_compras()
        os.system('cls')
        for item in self.lista_compras:
            self.carrinho_compras.append(input())
        print("Itens na lista de compras:", self.lista_compras)
        print("Itens no carrinho de compras:", self.carrinho_compras)

        self.pontuacao_acertos = 0
        self.pontuacao_erros = 0

        for item in self.carrinho_compras:
            if item in self.lista_compras:
                self.pontuacao_acertos += 5
            else:
                self.pontuacao_erros -= 3 * self.nivel_jogo

        print(f"Pontuação Final: {self.pontuacao_acertos - self.pontuacao_erros}")
        print(f"acertos:{self.pontuacao_acertos/5} ,{self.pontuacao_erros/(3*self.nivel_jogo) } erros.")


#loop principal do jogo
iniciar = True

while iniciar:
    tela.fill((202, 202, 241))
    tela.blit(imagem_fundo, (0, 0))

    if not jogo_comecou:
        botao_nome_jogo.desenhar()
        if botao_iniciar.desenhar():
            jogo_comecou = True
        if botao_sair.desenhar():
            iniciar = False
    else:
        botao_selecionar_nivel.desenhar()
        botao_nivel_facil.desenhar()
        botao_nivel_medio.desenhar()
        botao_nivel_dificil.desenhar()        
        if botao_voltar.desenhar():
            jogo_comecou = False
            

        if botao_nivel_facil.clicado(event):
            executar_nivel_facil()

    for event in pygame.event.get():
        #fechando janela
        if event.type == QUIT:
            pygame.quit()
            exit() #funcao para fechar
        
    
    pygame.display.update()  