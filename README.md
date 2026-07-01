# Snake Game

Jogo da cobrinha desenvolvido em Python com a biblioteca Pygame. A cobra se
movimenta em uma grade, coleta maçãs coloridas, cresce ou diminui conforme a
cor coletada e ganha velocidade durante a partida.

## Funcionalidades

- Movimento da cobra pelas setas do teclado.
- Geração de maçãs em posições aleatórias.
- Sete cores possíveis para as maçãs.
- Segmentos da cobra assumem a cor da maçã coletada.
- Sistema de pontuação:
  - maçã com cor diferente da cabeça: adiciona 2 pontos e um segmento;
  - maçã com a mesma cor da cabeça: remove 1 ponto e um segmento, quando
    possível.
- Aumento progressivo da velocidade conforme o tamanho da cobra.
- Detecção de colisão com as bordas e com o próprio corpo.
- Tela de fim de jogo e reinício pela tecla `R`.
- Recorde salvo localmente no arquivo `recorde.txt`.

## Requisitos

- Python 3.11 ou versão compatível.
- Pygame.

## Instalação

Clone ou baixe o projeto e acesse sua pasta:

```bash
git clone <URL_DO_REPOSITORIO>
cd snakegame
```

É recomendável criar um ambiente virtual:

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pygame
```

### Linux e macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pygame
```

## Execução

Execute o jogo com:

```bash
python "Snake Game/Snake_Circle.py"
```

No Linux ou macOS, caso necessário, use `python3` no lugar de `python`.

## Controles

| Tecla | Ação |
|---|---|
| Seta para cima | Move para cima |
| Seta para baixo | Move para baixo |
| Seta para a esquerda | Move para a esquerda |
| Seta para a direita | Move para a direita |
| `R` | Reinicia depois do fim da partida |

A cobra não pode inverter diretamente para a direção oposta.

## Como a aplicação foi implementada

Toda a lógica principal está em `Snake Game/Snake_Circle.py`.

1. O Pygame inicializa uma janela de 640 × 480 pixels.
2. A tela é organizada implicitamente em uma grade de 20 pixels.
3. A cobra é representada por uma lista de dicionários. Cada segmento possui
   uma posição `(x, y)` e uma cor RGB.
4. As operações FIFO ficam explícitas nas funções `adicionar_ao_final()` e
   `retirar_do_inicio()`: os segmentos entram no fim e saem do início da fila.
5. A função `grid_random()` escolhe uma nova posição livre para a maçã.
6. O loop principal processa o teclado, verifica colisões, atualiza a posição
   dos segmentos e redesenha a tela.
7. Ao coletar uma maçã, sua cor é comparada com a cor da cabeça para decidir
   se a cobra cresce ou diminui.
8. O tamanho da cobra define a quantidade de atualizações por segundo, de 5
   até 12.
9. Quando a pontuação supera o recorde, o novo valor é gravado imediatamente
   em `recorde.txt`. O caminho é calculado a partir do local do script,
   independentemente da pasta de execução.

## Estrutura do projeto

```text
snakegame/
├── README.md
├── recorde.txt
└── Snake Game/
    └── Snake_Circle.py
```

O arquivo `recorde.txt` deve conter somente um número inteiro.

## Possíveis melhorias

- Impedir que uma nova maçã apareça sobre a cobra.
- Encerrar explicitamente o loop ao fechar a janela.
- Separar a cobra, a maçã e o estado da partida em classes ou módulos.
- Adicionar sons, menu inicial, pausa e testes automatizados.
