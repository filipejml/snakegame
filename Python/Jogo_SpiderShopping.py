import pygame 
import tkinter as tk #biblioteca de interface gráfica; cria janelas, botões, caixas de texo, listas
import random 


# locals é um submodo de pygame, * importa todas as funçoes e constantes do locals
from pygame.locals import *; 
#função para fechar a janela quando solicitado
from sys import exit; 
 
#iniciando todas as funções do pygame
pygame.init()

#criando o objeto que seja definido como tela
#tela é uma variavel a
#largura e altura tambem sao variaveis
#(largura,altura) é uma tupla para o tamanho da tela

largura = 820
altura = 620
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Memoria Spider") #mudando o nome

game_start = False

#fonte do jogo
font = pygame.font.SysFont("arialblack", 40) #definir fonte
TEXT_COL = (255,255,255) #definindo cor 

#tamanho do botao
LARGURA_BOTAO = 120
ALTURA_BOTAO = 40

#coordenadas do botao
X_BOTAO = LARGURA_TELA // 2 - LARGURA_BOTAO // 2
Y_BOTAO = ALTURA_TELA // 2 - ALTURA_BOTAO // 2

# define a lista de níveis de dificuldade 
NIVEIS_DIFICULDADE = ["Fácil", "Médio", "Dificil"]

# define a variável do nível de dificuldade atual
NIVEL_DIFICULDADE = 0

#Define a funcao para desenhar o botao
def desenha_botao(texto, cor, x, y, largura, altura):
        retangulo = pygame.draw.rect(tela, cor, (x, y, largura, altura))
        texto_renderizado = FONTE.render(texto, True, PRETO)
        texto_rect = texto_renderizado.get_rect()
        texto_rect.center = retangulo.center
        tela.blit(texto_renderizado, texto_rect)
        return retangulo

#define mudança de nível
def mudar_nivel_dificuldade():
        global NIVEL_DIFICULDADE
        NIVEL_DIFICULDADE = (NIVEL_DIFICULDADE + 1) % len(NIVEIS_DIFICULDADE)

#define a função para atualizar a tela do jogo
def atualizar_tela():
        #limpa a tela
        tela.fill(BRANCO)


#def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col) 
        tela.blit(img, (x,y))

#classe para iniciar o jogo
#def comecar_jogo(max_movimentos, image_list):



#loop principal do jogo
while True:
    tela.fill((52,78,91))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_1:
                  game_start = True 
        #fechando janela
        if event.type == QUIT:
            pygame.quit()
            exit() #funcao para fechar
    
    root.mainloop()
    pygame.display.update()   