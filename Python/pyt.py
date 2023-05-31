nome = "lucas"
idade = 20
numero = 8
if nome == "lucas":
    print("nome igual")
else:
    print("nome diferente")

lista = ["7", numero]
dicionario = {"lucas":20, "filipe":27}
tupla = ("lucas", "filipe")

for e in lista:
    print(e)

for i in range(0, len(lista)):
    print(i)

def funcao(nome, idade):
    print(f"seu nome e {nome}, sua idade é {idade}")

funcao(nome, idade)

print(dicionario)

print(tupla)

lista[0] = "jose"

print(lista)

    #pygame.draw.rect(tela, (255,0,0), (200,300,40,50)) #onde eu quero pintar, qual a cor e o tamanho (x,y,largura, altura) - retangulo
    #pygame.draw.circle(tela, (0,0,200), (300,260),40) #ultima tupla representa posicao e diametro
    #pygame.draw.line(tela, (255,255,0), (390,0), (390,600), 5) #ultimas tupla representa o ponto inicial e o ponto final da reta e por ultimo a expessura
    #pygame.display.update() #para cada interaçao a tela sera atualizada

    #fazendo o objeto se movimente
    #pygame.draw.rect(tela, (255,0,0), (x,y,40,50)) #onde eu quero pintar, qual a cor e o tamanho (x,y,largura, altura) - retangulo
    #if y >= altura:
     #   y = 0
      #  y = y + 1