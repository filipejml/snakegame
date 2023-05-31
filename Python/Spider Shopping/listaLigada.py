# Classe que contem nossa celula, nela vai conter o conteudo e o ponteiro que aponta pra proxima celula
#


class Celula:
    # é o construtor da classe, nele que vai ser inicializado as variaveis com valores padrões(None = vazio)
    def __init__(self, imagem=None, proximo=None):
        self.imagem = imagem
        self.proximo = proximo


# Classe que vai manipular nossa celula, nela ta inserida a cabeça da lista e todos os demais metodos para manipular as celulas


class ListaLigada:
    # é o construtor da classe, nele que vai ser inicializado as variaveis com valores padrões(None = vazio)
    def __init__(self):
        self.cabeca = None

    # metodo para adicionar uma nova celula sempre no fim
    def adicionarCelula(self, imagem):
        if self.buscaImagem(imagem) == False:
            novaCelula = Celula(imagem)
            if self.cabeca == None:
                self.cabeca = novaCelula
                return

            celulaAtual = self.cabeca
            while celulaAtual.proximo != None:
                celulaAtual = celulaAtual.proximo

            celulaAtual.proximo = novaCelula
            return

    # remove a celula de acordo com o seu conteudo
    def removeCelula(self, imagem):
        if self.buscaImagem(imagem) == True:
            if self.cabeca.imagem == imagem:
                self.cabeca = self.cabeca.proximo

            else:
                celulaMorta = self.cabeca
                while celulaMorta and celulaMorta.imagem != imagem:
                    celulaAnterior = celulaMorta
                    celulaMorta = celulaMorta.proximo

                if celulaMorta.proximo == None:
                    celulaAnterior.proximo = None

                else:
                    celulaAnterior.proximo = celulaMorta.proximo

    # metodo que retorna a imagem da lista
    def retornaImagem(self, local):
        if local <= self.tamanhoLista():
            celulaAtual = self.cabeca
            aux = 1
            while celulaAtual and local != aux:
                celulaAtual = celulaAtual.proximo
                aux += 1
            return celulaAtual.imagem

    # metodo que busca saber se a imagem esta na lista ligada
    def buscaImagem(self, imagem):
        celulaAtual = self.cabeca

        while celulaAtual and celulaAtual.imagem != imagem:
            celulaAtual = celulaAtual.proximo

        if celulaAtual == None:
            return False

        else:
            return True

    # retorna o tamanho total da lista
    def tamanhoLista(self):
        total = 0
        celulaAtual = self.cabeca

        while celulaAtual:
            celulaAtual = celulaAtual.proximo
            total += 1
        return total
