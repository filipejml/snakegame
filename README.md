# Snake Game

Jogo da cobrinha desenvolvido em Python com a biblioteca Pygame. A cobra se
movimenta em uma grade, coleta maçãs coloridas, cresce ou diminui conforme a
cor coletada e ganha velocidade durante a partida.

## Funcionalidades

- Movimento da cobra pelas setas do teclado.
- Geração de maçãs em posições aleatórias.
- Paletas ampliadas, com cores diferentes em cada fase, incluindo branco e
  preto em todas elas.
- Segmentos da cobra assumem a cor da maçã coletada.
- Sistema de pontuação:
  - maçã com cor diferente da cabeça: adiciona 2 pontos e um segmento;
  - maçã com a mesma cor da cabeça: remove 1 ponto e um segmento, quando
    possível.
- Quatro fases explícitas, liberadas pela pontuação.
- Velocidade e obstáculos diferentes em cada fase.
- Painel com fase, velocidade e efeito da próxima maçã.
- Visual temático por fase, com grades, HUD translúcido e cores próprias.
- Cobra com contorno e olhos, maçãs com brilho e obstáculos destacados.
- Detecção de colisão com as bordas, o próprio corpo e os obstáculos.
- Menu inicial, pausa e opção de sair pelo teclado.
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
python -m pip install -r requirements.txt
```

### Linux e macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Execução

Execute o jogo com:

```bash
python "Snake Game/Snake_Circle.py"
```

No Linux ou macOS, caso necessário, use `python3` no lugar de `python`.

## Testes

Depois de instalar as dependências, execute a suíte com:

```bash
python -m unittest discover -s tests -v
```

Os testes verificam pontuação, comportamento FIFO, colisões com bordas, corpo
e obstáculos, além dos limites de pontuação da progressão de dificuldade.

## Controles

| Tecla | Ação |
|---|---|
| Seta para cima | Move para cima |
| Seta para baixo | Move para baixo |
| Seta para a esquerda | Move para a esquerda |
| Seta para a direita | Move para a direita |
| `Enter` ou `Espaço` | Inicia a partida pelo menu |
| `P` | Pausa ou continua a partida |
| `R` | Reinicia depois do fim da partida |
| `Q` ou `Esc` | Salva o recorde e encerra o jogo |

A cobra não pode inverter diretamente para a direção oposta.

## Fases

| Pontuação | Fase | Velocidade | Obstáculos |
|---:|---|---:|---:|
| 0 | Jardim Neon | 5 | 0 |
| 10 | Labirinto Solar | 7 | 6 |
| 24 | Oceano Elétrico | 9 | 9 |
| 40 | Caos Cromático | 12 | 14 |

Cada fase possui uma paleta própria para as maçãs e uma cor específica para
seus obstáculos. Ao mudar de fase, obstáculos que coincidiriam com a posição
atual da cobra são descartados para evitar uma derrota injusta.

## Como a aplicação foi implementada

Toda a lógica está em `Snake Game/Snake_Circle.py`, organizada em três classes:

1. `Jogo` controla o loop principal, eventos, fases, pontuação, recorde e telas.
2. `Cobra` controla direção, movimento, colisões e operações da fila.
3. `Maca` controla posição, cor, efeito e geração em uma célula livre.
4. O Pygame inicializa uma janela de 640 × 480 pixels.
5. A tela é organizada implicitamente em uma grade de 20 pixels.
6. A cobra é representada por uma `deque` de dicionários. Essa estrutura
   implementa uma fila com inserção e remoção eficientes nas extremidades.
   Cada segmento possui uma posição `(x, y)` e uma cor RGB.
7. As operações FIFO ficam explícitas nos métodos `adicionar_ao_final()` e
   `retirar_do_inicio()`: os segmentos entram no fim e saem do início da fila.
8. O método `Maca.gerar()` escolhe uma nova posição livre para a maçã.
9. O loop principal delega eventos, teclas, colisões, coleta, movimento,
   recorde e renderização a métodos pequenos e específicos.
10. Ao coletar uma maçã, sua cor é comparada com a cor da cabeça para decidir
   se a cobra cresce ou diminui.
11. A pontuação seleciona uma fase em `FASES`, que define nome, velocidade,
   paleta de cores e posições dos obstáculos.
12. A maçã só pode surgir em células que não estejam ocupadas pela cobra ou
   pelos obstáculos.
13. Quando a pontuação supera o recorde, o novo valor é gravado imediatamente
   em `recorde.txt`. O caminho é calculado a partir do local do script,
   independentemente da pasta de execução.

## Estrutura do projeto

```text
snakegame/
├── README.md
├── recorde.txt
├── requirements.txt
├── tests/
│   └── test_snake_game.py
└── Snake Game/
    └── Snake_Circle.py
```

O arquivo `recorde.txt` deve conter somente um número inteiro.

## Possíveis melhorias

- Adicionar sons.
