import pygame
from pygame.locals import *
import random
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

#definindo posicões aleatórias para a maça na tela
def grid_random():
    x = random.randint(0, 31) * 20
    y = random.randint(0, 23) * 20
    return (x, y)

#definindo a colisão
def colisao(c1, c2):
    return c1 == c2

# Criando a cobra
cobra = [{'pos': (200, 200), 'cor': (255, 255, 255)}]
cobra_corpo = pygame.Surface((20, 20))

# Criando a maçã
maca = pygame.Surface((20, 20))
maca_pos = grid_random()
cores_maca = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
maca_cor = random.choice(cores_maca)

# Iniciando a cobra se movimentando para a esquerda
direcao = LEFT

# Definindo a velocidade do jogo
clock = pygame.time.Clock()

# Pontuação e recorde
pontuacao = 0
recorde = 0
fonte = pygame.font.SysFont("lexend", 24)

# Estado do jogo
game_over = False

# Carregando o recorde do arquivo
try:
    with open("recorde.txt", "r") as arquivo:
        recorde = int(arquivo.read())
except FileNotFoundError:
    pass

# Loop principal
while True:
    if len(cobra) <= 10:
        velocidade = 5
    elif 10 < len(cobra) <= 20:
        velocidade = 6
    elif 20 < len(cobra) <= 30:
        velocidade = 7
    elif 30 < len(cobra) <= 40:
        velocidade = 8
    elif 40 < len(cobra) <= 50:
        velocidade = 9
    elif 50 < len(cobra) <= 60:
        velocidade = 10
    elif 60 < len(cobra) <= 70:
        velocidade = 11
    else:
        velocidade = 12

    clock.tick(velocidade)

    for event in pygame.event.get():
        if event.type == QUIT:
            # Salvando o recorde no arquivo antes de sair
            with open("recorde.txt", "w") as arquivo:
                arquivo.write(str(recorde))
            pygame.quit()

        #controle de posição
        if event.type == KEYDOWN:
            if event.key == K_UP and direcao != DOWN:
                direcao = UP
            elif event.key == K_DOWN and direcao != UP:
                direcao = DOWN
            elif event.key == K_RIGHT and direcao != LEFT:
                direcao = RIGHT
            elif event.key == K_LEFT and direcao != RIGHT:
                direcao = LEFT

            if game_over and event.key == K_v:
                # Reiniciando o jogo
                cobra = [{'pos': (200, 200), 'cor': (255, 255, 255)}]
                direcao = LEFT
                pontuacao = 0
                game_over = False

    if not game_over:
        # Testando a colisão com o próprio corpo
        for i in range(1, len(cobra)):
            if colisao(cobra[0]['pos'], cobra[i]['pos']):
                game_over = True

        # Testando a colisão com a borda da tela
        if cobra[0]['pos'][0] < 0 or cobra[0]['pos'][0] >= 640 or cobra[0]['pos'][1] < 0 or cobra[0]['pos'][1] >= 480:
            game_over = True

        if colisao(cobra[0]['pos'], maca_pos):
            maca_pos = grid_random()

            if cobra[0]['cor'] == maca_cor:
                if len(cobra) > 1:
                    cobra.pop(0)
                    pontuacao -= 1
                    print("Cobra atualizada decrescimo:", cobra)
            else:
                pontuacao += 2
                novo_segmento = {'pos': cobra[-1]['pos'], 'cor': maca_cor}
                cobra.append(novo_segmento)
                print("Cobra atualizada com acrescimo:", cobra)
            maca_cor = random.choice(cores_maca)

            if pontuacao > recorde:
                recorde = pontuacao

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

    # Apresentando na tela
    tela.fill((0, 0, 0))
    tela.blit(maca, maca_pos)
    maca.fill(maca_cor)

    for segment in cobra:
        cobra_corpo.fill(segment['cor'])
        tela.blit(cobra_corpo, segment['pos'])

    if game_over:
        # Exibindo a mensagem de fim de jogo
        mensagem = fonte.render("Fim de jogo! Sua pontuação foi: " + str(pontuacao) + " pontos!", True,
                                (255, 255, 255))
        reiniciar = fonte.render("Pressione a tecla 'V' para reiniciar o jogo", True, (255, 255, 255))
        tela.blit(mensagem, (160, 200))
        tela.blit(reiniciar, (180, 240))

    # Exibindo a pontuação e o recorde na tela
    texto_pontuacao = fonte.render("Pontuação: " + str(pontuacao), True, (255, 255, 255))
    texto_recorde = fonte.render("Recorde: " + str(recorde), True, (255, 255, 255))
    tela.blit(texto_pontuacao, (10, 10))
    tela.blit(texto_recorde, (10, 40))

    # Atualizando a tela
    pygame.display.update()
