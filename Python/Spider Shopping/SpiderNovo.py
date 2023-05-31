import pygame;
from sys import exit;
from pygame.locals import *;
from listaLigada import ListaLigada
import random

#iniciando a biblioteca pygame
pygame.init()

# define as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

#Definindo tamanho da tela
LARGURA = 800
ALTURA = 600

#Variavéis de tempo:
Clock = pygame.time.Clock()
Timer = 5
Tempo_Segundo = 50
intervalo = 1000 # intervalo de tempo para a mudança das imagens

# define a janela do jogo
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Spider Shopping')

# define a fonte do texto
fonte = pygame.font.SysFont("arial", 30)
# demais fontes
fonte = pygame.font.SysFont('arial', 75, True, True)
fonte2 = pygame.font.SysFont("arial",50,True,True)

#Função para colocar textos na tela:
def draw_text(text, font, text_col ,x ,y):
    img = font.render(text, True, text_col)
    tela.blit(img,(x,y))

#criando um fundo de tela
imagem_fundo = pygame.image.load("imagens_botoes\\mercado.png")
imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))

#variaveis de imagem
check_img = pygame.image.load("imagens_botoes\\check.png").convert_alpha()
check_img = pygame.transform.scale(check_img, (30, 30))
lista_img = pygame.image.load("imagens_botoes\\checklist.png").convert_alpha()
quadro_resultado_img = pygame.image.load("imagens_botoes\\score.png").convert_alpha()
#definindo os botoes de imagem
botao_nome_jogo = pygame.image.load("imagens_botoes\\spider shopping.png").convert_alpha()
botao_iniciar = pygame.image.load("imagens_botoes\\play.png").convert_alpha()
botao_iniciar2 = pygame.image.load("imagens_botoes\\play.png").convert_alpha()
botao_sair = pygame.image.load("imagens_botoes\\exit.png").convert_alpha()
botao_nivel_facil = pygame.image.load("imagens_botoes\\easy.png").convert_alpha()
botao_nivel_medio = pygame.image.load("imagens_botoes\\medium.png").convert_alpha()
botao_nivel_dificil = pygame.image.load("imagens_botoes\\hard.png").convert_alpha()
botao_selecionar_nivel = pygame.image.load("imagens_botoes\\niveis.png").convert_alpha()
botao_voltar = pygame.image.load("imagens_botoes\\voltar.png").convert_alpha()
botao_finalizar = pygame.image.load("imagens_botoes\\finalizar.png").convert_alpha()
botao_quadrado = pygame.image.load("imagens_botoes\\quadrado.png").convert_alpha()

#Escala das Imagens não interativas:
Lista_img = pygame.transform.scale(lista_img,(300,300))
Quadro_img = pygame.transform.scale(quadro_resultado_img,(400,400))

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
    
#Variaveis de menu:
Tela1 = False   #Menu inicial e Segundo Menu
Tela2 = False   #Tela Durante o jogo

#instanciando os botões
botao_nome_jogo = Botao(200, 150, botao_nome_jogo, 0.6)
botao_iniciar = Botao(100, 200, botao_iniciar, 0.6)
botao_sair = Botao(450, 200, botao_sair, 0.6)
botao_nivel_facil = Botao(50, 200, botao_nivel_facil, 0.6)
botao_nivel_medio = Botao(250, 200, botao_nivel_medio, 0.6)
botao_nivel_dificil = Botao(450, 200, botao_nivel_dificil, 0.6)
botao_selecionar_nivel = Botao(250, 40, botao_selecionar_nivel, 0.6)
botao_voltar = Botao(250, 320, botao_voltar, 0.6)
botao_finalizar = Botao(200, 300, botao_finalizar, 0.6)
botao_iniciar2 = Botao(100, 200, botao_iniciar2, 0.6)

#instancianndo os marcadores da lista
botao_quadrado_img1 = Botao(400,-205, botao_quadrado,0.05)
botao_quadrado_img2 = Botao(400,-170, botao_quadrado,0.05)
botao_quadrado_img3 = Botao(400,-135, botao_quadrado,0.05)
botao_quadrado_img4 = Botao(400,-100, botao_quadrado,0.05)
botao_quadrado_img5 = Botao(400,-65, botao_quadrado,0.05)
botao_quadrado_img6 = Botao(400,-30, botao_quadrado,0.05)
botao_quadrado_img7 = Botao(400,5, botao_quadrado,0.05)
botao_quadrado_img8 = Botao(400,40, botao_quadrado,0.05)
botao_quadrado_img9 = Botao(400,75, botao_quadrado,0.05)
botao_quadrado_img10 = Botao(400,110, botao_quadrado,0.05)
botao_quadrado_img11 = Botao(400,145, botao_quadrado,0.05)
botao_quadrado_img12 = Botao(400,180, botao_quadrado,0.05)


#variaveis de checagem
V1 = False
V2 = False
V3 = False
V4 = False
V5 = False
V6 = False
V7 = False
V8 = False
V9 = False
V10 = False
V11 = False
V12 = False

# itens ------------------------------------------------------------
item_1 = pygame.image.load("imagens_jogo\\açucar.png")
item_2 = pygame.image.load("imagens_jogo\\arroz.png")
item_3 = pygame.image.load("imagens_jogo\\biscoito.png")
item_4 = pygame.image.load("imagens_jogo\\cafe.png")
item_5 = pygame.image.load("imagens_jogo\\escova.png")
item_6 = pygame.image.load("imagens_jogo\\feijao.png")
item_7 = pygame.image.load("imagens_jogo\\leit.png")
item_8 = pygame.image.load("imagens_jogo\\macarrao.png")
item_9 = pygame.image.load("imagens_jogo\\oleo.png")
item_10 = pygame.image.load("imagens_jogo\\pao.png")
item_11 = pygame.image.load("imagens_jogo\\pasta.png")
item_12 = pygame.image.load("imagens_jogo\\sal.png")
imagens_itens = [item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12]

lista_1 = ListaLigada()
for i in imagens_itens:
    lista_1.adicionarCelula(i)

#iniciando variaveis
pontuacao = 0
acertos = 0
aux = 0
dif = 0
relogio = pygame.time.Clock()

lista2 = ListaLigada()
lista3 = ListaLigada()

#Loop do Jogo:
aparecer_aranhas = False
run = True
while run:

    pygame.time.delay(50)
    tela.fill((202, 202, 241))
    tela.blit(imagem_fundo,(0,0))

    if Tela2 == True:
        imagem_fundo = pygame.image.load("imagens_botoes\interior_mercado.png")
        pygame.draw.rect(tela,(0,0,0), (222, 13, 444, 56))
        draw_text("Timer: "+str (Tempo_Segundo),fonte,(255, 255, 255), 444, 12.5)

        if aux == dif or aux == 0:
            sla = lista_1.tamanhoLista()
            escolha_itens_1 = random.randint(1,sla)
            escolha_itens_2 = random.randint(1,sla)
            escolha_itens_3 = random.randint(1,sla)
            escolha_itens_4 = random.randint(1,sla)
            aux = 0
        aux += 1

        cria_item_1 = Botao(-92, -224, lista_1.retornaImagem(escolha_itens_1), 2.5)
    
        if cria_item_1.desenhar() and Tempo_Segundo != 0:
            if lista3.buscaImagem(lista3.retornaImagem(escolha_itens_1)) == True:

                if lista2.buscaImagem(lista3.retornaImagem(escolha_itens_1)) == False:
                    acertos = acertos + 1
                    lista2.adicionarCelula(lista3.retornaImagem(escolha_itens_1))
                    pontuacao = pontuacao + 1
                else:
                    pontuacao = pontuacao - 1

            else:
                pontuacao = pontuacao - 1

        cria_item_2 = Botao(250, -149, lista_1.retornaImagem(escolha_itens_2), 2.5)
        
        if cria_item_2.desenhar() and Tempo_Segundo != 0:
            if lista3.buscaImagem(lista3.retornaImagem(escolha_itens_2)) == True:

                if lista2.buscaImagem(lista3.retornaImagem(escolha_itens_2)) == False:
                    acertos = acertos + 1
                    lista2.adicionarCelula(lista3.retornaImagem(escolha_itens_2))
                    pontuacao = pontuacao + 1
                else:
                    pontuacao = pontuacao - 1

            else:
                pontuacao = pontuacao - 1

        cria_item_3 = Botao(467, -149, lista_1.retornaImagem(escolha_itens_3), 2.5)
        
        if cria_item_3.desenhar() and Tempo_Segundo != 0:
            if lista3.buscaImagem(lista3.retornaImagem(escolha_itens_3)) == True:

                if lista2.buscaImagem(lista3.retornaImagem(escolha_itens_3)) == False:
                    acertos = acertos + 1
                    lista2.adicionarCelula(lista3.retornaImagem(escolha_itens_3))
                    pontuacao = pontuacao + 1
                else:
                    pontuacao = pontuacao - 1
                
            else:
                pontuacao = pontuacao - 1

        cria_item_4 = Botao(526, -149, lista_1.retornaImagem(escolha_itens_4), 2.5)
        
        if cria_item_4.desenhar() and Tempo_Segundo != 0:
            if lista3.buscaImagem(lista3.retornaImagem(escolha_itens_4)) == True:

                if lista2.buscaImagem(lista3.retornaImagem(escolha_itens_4)) == False:
                    acertos = acertos + 1
                    lista2.adicionarCelula(lista3.retornaImagem(escolha_itens_4))
                    pontuacao = pontuacao + 1
                else:
                    pontuacao = pontuacao - 1

            else:
                pontuacao = pontuacao - 1

        if Tempo_Segundo != 0:
            if(Timer > 52):
                Timer -= 1
            else:
                Tempo_Segundo -= 1
                Timer = 60

        if Tempo_Segundo == 0:
            tela.blit(Quadro_img,(140, -30))
            pygame.draw.rect(tela,(249,92,2), (289, 106, 517, 50))
            draw_text("Fim de Jogo",fonte,(255, 55, 255), 310, 225)
            draw_text("Acertos: "+str(acertos),fonte2,(255, 255, 255), 270, 365)
            draw_text("Pontos Totais: "+str(pontuacao),fonte2,(255, 255, 255), 270, 445)
            pygame.draw.rect(tela,(255,255,255), (680, 528, 100, 60))
            if botao_finalizar.desenhar():
                imagem_fundo = pygame.image.load("imagens_botoes\mercado.png")
                Tempo_Segundo = 45
                aux = 0
                Tela2 = False
                Tela1 = False

    else:
        
        if Tela1 == True:
            tela.blit(Lista_img, (-267, -40))

            if botao_nivel_facil.desenhar():
                dif = 20

            if botao_nivel_medio.desenhar():
                dif = 15

            if botao_nivel_dificil.desenhar():
                dif = 8

            draw_text("Abacaxi",fonte2,(0, 0, 0), 100, 90)
            if botao_quadrado_img1.desenhar():
                V1 = not V1

            if V1 == True:    
                lista3.adicionarCelula(item_1)
                tela.blit(check_img, (440, 150))
            if V1 == False:
                lista3.removeCelula(item_1)

            draw_text("Manga",fonte2,(0, 0, 0), 100, 135)
            if botao_quadrado_img2.desenhar():
                V2 = not V2
            
            if V2 == True:    
                lista3.adicionarCelula(item_2)
                tela.blit(check_img, (440, 185))
            if V2 == False:
                lista3.removeCelula(item_2)

            draw_text("Garfo",fonte2,(0, 0, 0), 100, 178)
            if botao_quadrado_img3.desenhar():
                V3 = not V3

            if V3 == True:    
                lista3.adicionarCelula(item_3)
                tela.blit(check_img, (440, 220))
            if V3 == False:
                lista3.removeCelula(item_3)

            draw_text("Faca",fonte2,(0, 0, 0), 100, 220)
            if botao_quadrado_img4.desenhar():
                V4 = not V4

            if V4 == True:    
                lista3.adicionarCelula(item_4)
                tela.blit(check_img, (440, 255))
            if V4 == False:
                lista3.removeCelula(item_4)

            draw_text("Maçã",fonte2,(0, 0, 0), 100, 262)
            if botao_quadrado_img5.desenhar():
                V5 = not V5

            if V5 == True:
                lista3.adicionarCelula(item_5)
                tela.blit(check_img, (440, 290))
            if V5 == False:
                lista3.removeCelula(item_5)

            draw_text("Cesto",fonte2,(0, 0, 0), 100, 300)
            if botao_quadrado_img6.desenhar():
                V6 = not V6

            if V6 == True:
                lista3.adicionarCelula(item_6)
                tela.blit(check_img, (440, 325))
            if V6 == False:
                lista3.removeCelula(item_6)

            draw_text("Cenoura",fonte2,(0, 0, 0), 100, 338)
            if botao_quadrado_img7.desenhar():
                V7 = not V7

            if V7 == True:
                lista3.adicionarCelula(item_7)
                tela.blit(check_img, (440, 360))
            if V7 == False:
                lista3.removeCelula(item_7)

            draw_text("Panela",fonte2,(0, 0, 0), 100, 376)
            if botao_quadrado_img8.desenhar():
                V8 = not V8

            if V8 == True:
                lista3.adicionarCelula(item_8)
                tela.blit(check_img, (440, 395))
            if V8 == False:
                lista3.removeCelula(item_8)

            draw_text("Caneta",fonte2,(0, 0, 0), 100, 413)
            if botao_quadrado_img9.desenhar():
                V9 = not V9

            if V9 == True:
                lista3.adicionarCelula(item_9)
                tela.blit(check_img, (440, 430))
            if V9 == False:
                lista3.removeCelula(item_9)

            draw_text("Grampeador",fonte2,(0, 0, 0), 100, 450)
            if botao_quadrado_img10.desenhar():
                V10 = not V10
            
            if V10 == True:
                lista3.adicionarCelula(item_10)
                tela.blit(check_img, (440, 465))
            if V10 == False:
                lista3.removeCelula(item_10)

            draw_text("Borracha",fonte2,(0, 0, 0), 100, 487)
            if botao_quadrado_img11.desenhar():
                V11 = not V11

            if V11 == True:
                lista3.adicionarCelula(item_11)
                tela.blit(check_img, (440, 500))
            if V11 == False:
                lista3.removeCelula(item_11)

            draw_text("Papel",fonte2,(0, 0, 0), 100, 525)
            if botao_quadrado_img12.desenhar():
                V12 = not V12

            if V12 == True:
                lista3.adicionarCelula(item_12)
                tela.blit(check_img, (440, 535))
            if V12 == False:
                lista3.removeCelula(item_12)
                          
            if botao_iniciar2.desenhar():
                Tela1 = False
                Tela2 = True

            if botao_voltar.desenhar():
                Tela1 = False
        else:

            if botao_iniciar.desenhar():
                Tela1 = True

            if botao_sair.desenhar():
                run = False


    #Evento de saída padrão:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    relogio.tick(60)
    tempo_jogo = pygame.time.get_ticks()
pygame.quit()