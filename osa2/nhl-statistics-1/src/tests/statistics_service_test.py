import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_onnistunut_haku(self):
        pelaaja = self.stats.search("Gretzky")
        self.assertEqual(pelaaja.name, "Gretzky")

    def test_epaonnistunut_haku(self):
        pelaaja = self.stats.search("jooo")
        self.assertIsNone(pelaaja)

    def test_joukkue_listaus(self):
        lista = self.stats.team("EDM")
        self.assertEqual(len(lista), 3)
        
        for pelaaja in lista:
            self.assertEqual(pelaaja.team, "EDM")

    def test_joukkue_none(self):
        lista = self.stats.team("juuu")
        self.assertEqual(lista, [])

    def test_top_4_pisteet(self):
        pisteet = self.stats.top(3)
        nimet = [pelaaja.name for pelaaja in pisteet]

        self.assertEqual(nimet, ["Gretzky", "Lemieux", "Yzerman", "Kurri"])

