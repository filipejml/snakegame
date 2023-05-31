import random
import time

# Lista de compras
lista_de_compras = ["pão", "leite", "ovos", "queijo"]

# Lista de itens encontrados
itens_encontrados = []

# Tempo limite em segundos
tempo_limite = 60

# Início do jogo
inicio = time.time()

# Loop principal do jogo
while True:
    # Verifica se o tempo acabou
    if time.time() - inicio > tempo_limite:
        print("Tempo esgotado! Você perdeu!")
        break

    # Mostra a lista de compras
    print("Itens para encontrar:", lista_de_compras)

    # Pede ao jogador para digitar um item
    item = input("Digite um item que você encontrou: ")

    # Verifica se o item faz parte da lista de compras
    if item in lista_de_compras:
        # Verifica se o item já foi encontrado
        if item in itens_encontrados:
            print("Você já encontrou este item!")
        else:
            print("Item encontrado!")
            itens_encontrados.append(item)
            # Verifica se todos os itens foram encontrados
            if len(itens_encontrados) == len(lista_de_compras):
                print("Parabéns! Você encontrou todos os itens!")
                break
    else:
        print("Este item não faz parte da lista de compras!")

# Fim do jogo
