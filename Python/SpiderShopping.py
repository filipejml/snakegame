import pygame 
import os
import tkinter as tk #biblioteca de interface gráfica; cria janelas, botões, caixas de texo, listas
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
def executar_nivel_facil():
    nivel_facil = True
    largura_tela = 640
    altura_tela = 480
    tela_nivel_facil = pygame.display.set_mode((largura_tela, altura_tela))
    
    while nivel_facil:
        # desenhar a tela de nível fácil
        tela_nivel_facil.fill((202, 202, 241))
        # aqui você pode desenhar os elementos específicos do nível fácil
        pygame.display.update()

        # loop principal para eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

    global jogo_comecou 
    global nivel_selecionado
    lista_compras = []
    prateleira = ['pao', 'leite', 'arroz', 'feijao', 'macarrao', 'oleo', 'acucar',
              'sal', 'cafe', 'cha', 'biscoito', 'refrigerante', 'suco']
    carrinho_compras = []
    nivel_jogo = 1
    n_itens = 4

    # Dicionário que armazena a quantidade de vezes que cada item foi adicionado ao carrinho
    qtd_itens_carrinho = {}

    def carregar_lista_compras(prateleira, lista_compras, n_itens, nivel_jogo):
        n_itens *= nivel_jogo
        for item in range(n_itens):
            item = random.choice(prateleira)
            lista_compras.append(item)
            prateleira.remove(item)

    def adicionar_item(prateleira, lista_compras):
        print("Qual item deseja adicionar à lista de compras?")
        item = input()
        if item in prateleira:
            lista_compras.append(item)
            prateleira.remove(item)
            print("Item adicionado à lista de compras.")
        else:
            print("O item não está disponível na prateleira.")

    def remover_item(prateleira, lista_compras):
        print("Qual item deseja remover da lista de compras?")
        item = input()
        if item in lista_compras:
            prateleira.append(item)
            lista_compras.remove(item)
            print("Item removido da lista de compras.")
        else:
            print("O item não está na lista de compras.")


    def editar_lista_compras(prateleira, lista_compras):
        carregar_lista_compras(prateleira, lista_compras, n_itens, nivel_jogo)
    
    while True:
      print("\nItens da Lista de Compras:", lista_compras)
      print("Prateleira:", prateleira)
      print("Digite 'a' para adicionar um item à lista de compras.")
      print("Digite 'r' para remover um item da lista de compras.")
      print("Digite 'sair' para sair.")
      opcao = input().lower()

      if opcao == 'a':
          adicionar_item(prateleira, lista_compras)
      elif opcao == 'r':
          remover_item(prateleira, lista_compras)
      elif opcao == 'sair':
          break
      else:
          print("Opção inválida.")
    editar_lista_compras(prateleira, lista_compras)
    os.system('cls')

    for item in lista_compras:
        carrinho_compras.append(input())
        print("Itens na lista de compras:", lista_compras)
        print("Itens no carrinho de compras:", carrinho_compras)

    # Inicializa as variáveis de pontuação
    pontuacao_acertos = 0
    pontuacao_erros = 0

    # Verifica a pontuação para cada item no carrinho de compras
    for item in carrinho_compras:
        if item in lista_compras:
            pontuacao_acertos += 5
        else:
            pontuacao_erros -= 3 * nivel_jogo

    # Exibe a pontuação final
    print(f"Pontuação Final: {pontuacao_acertos - pontuacao_erros}")
    print(f"acertos:{pontuacao_acertos/5} ,{pontuacao_erros/(3*nivel_jogo) } erros.")


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