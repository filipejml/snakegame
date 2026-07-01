import importlib.util
import os
import unittest
from pathlib import Path


os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

CAMINHO_MODULO = (
    Path(__file__).resolve().parents[1] / "Snake Game" / "Snake_Circle.py"
)
ESPECIFICACAO = importlib.util.spec_from_file_location(
    "snake_circle", CAMINHO_MODULO
)
snake_circle = importlib.util.module_from_spec(ESPECIFICACAO)
ESPECIFICACAO.loader.exec_module(snake_circle)


class TestFila(unittest.TestCase):
    def test_segmento_entra_no_final_e_sai_do_inicio(self):
        cobra = snake_circle.Cobra()
        segmento_inicial = cobra.cabeca
        cor_nova = (255, 0, 0)

        cobra.adicionar_ao_final(cor_nova)
        removido = cobra.retirar_do_inicio()

        self.assertIs(removido, segmento_inicial)
        self.assertEqual(len(cobra.segmentos), 1)
        self.assertEqual(cobra.cabeca["cor"], cor_nova)

    def test_cobra_nunca_fica_vazia(self):
        cobra = snake_circle.Cobra()

        removido = cobra.retirar_do_inicio()

        self.assertIsNone(removido)
        self.assertEqual(len(cobra.segmentos), 1)


class TestPontuacao(unittest.TestCase):
    def criar_jogo_minimo(self):
        jogo = snake_circle.Jogo.__new__(snake_circle.Jogo)
        jogo.cobra = snake_circle.Cobra()
        jogo.maca = snake_circle.Maca()
        jogo.pontuacao = 0
        jogo.fase_atual = snake_circle.FASES[0]
        jogo.obstaculos = []
        return jogo

    def test_cor_diferente_adiciona_segmento_e_dois_pontos(self):
        jogo = self.criar_jogo_minimo()
        jogo.maca.cor = (255, 0, 0)

        jogo.processar_coleta()

        self.assertEqual(jogo.pontuacao, 2)
        self.assertEqual(len(jogo.cobra.segmentos), 2)

    def test_cor_igual_remove_inicio_e_um_ponto(self):
        jogo = self.criar_jogo_minimo()
        jogo.cobra.adicionar_ao_final((255, 0, 0))
        jogo.maca.cor = jogo.cobra.cabeca["cor"]

        jogo.processar_coleta()

        self.assertEqual(jogo.pontuacao, -1)
        self.assertEqual(len(jogo.cobra.segmentos), 1)

    def test_cor_igual_nao_remove_segmento_unico(self):
        jogo = self.criar_jogo_minimo()
        jogo.maca.cor = jogo.cobra.cabeca["cor"]

        jogo.processar_coleta()

        self.assertEqual(jogo.pontuacao, 0)
        self.assertEqual(len(jogo.cobra.segmentos), 1)


class TestColisoes(unittest.TestCase):
    def test_colisao_com_borda(self):
        cobra = snake_circle.Cobra()
        cobra.cabeca["pos"] = (-20, 200)

        self.assertTrue(cobra.colidiu_com_borda())

    def test_colisao_com_proprio_corpo(self):
        cobra = snake_circle.Cobra()
        cobra.adicionar_ao_final((255, 0, 0))
        cobra.segmentos[-1]["pos"] = cobra.cabeca["pos"]

        self.assertTrue(cobra.colidiu_com_corpo())

    def test_colisao_com_obstaculo(self):
        jogo = snake_circle.Jogo.__new__(snake_circle.Jogo)
        jogo.cobra = snake_circle.Cobra()
        jogo.obstaculos = [jogo.cobra.cabeca["pos"]]

        self.assertTrue(jogo.houve_colisao())

    def test_posicao_livre_nao_colide(self):
        jogo = snake_circle.Jogo.__new__(snake_circle.Jogo)
        jogo.cobra = snake_circle.Cobra()
        jogo.obstaculos = [(320, 320)]

        self.assertFalse(jogo.houve_colisao())


class TestProgressaoDificuldade(unittest.TestCase):
    def obter_fase(self, pontuacao):
        jogo = snake_circle.Jogo.__new__(snake_circle.Jogo)
        jogo.pontuacao = pontuacao
        return jogo.obter_fase()

    def test_fases_nos_limites_de_pontuacao(self):
        casos = [
            (0, "Jardim Neon", 5),
            (9, "Jardim Neon", 5),
            (10, "Labirinto Solar", 7),
            (23, "Labirinto Solar", 7),
            (24, "Oceano Elétrico", 9),
            (39, "Oceano Elétrico", 9),
            (40, "Caos Cromático", 12),
        ]

        for pontuacao, nome, velocidade in casos:
            with self.subTest(pontuacao=pontuacao):
                fase = self.obter_fase(pontuacao)
                self.assertEqual(fase["nome"], nome)
                self.assertEqual(fase["velocidade"], velocidade)


if __name__ == "__main__":
    unittest.main()
