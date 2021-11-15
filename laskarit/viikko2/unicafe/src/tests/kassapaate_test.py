import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassassa_oikea_summa(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_edullinen_lounas_kateisella_tarpeeksi_rahaa(self):
        takaisin = self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(takaisin, 10)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
    
    def test_edullinen_lounas_kateisella_ei_tarpeeksi(self):
        takaisin = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(takaisin, 200)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kallis_lounas_kateisella(self):
        takaisin = self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(takaisin, 50)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
    
    def test_kallis_lounas_kateisella_ei_tarpeeksi(self):
        takaisin = self.kassa.syo_maukkaasti_kateisella(350)
        self.assertEqual(takaisin, 350)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edullinen_kortilla(self):
        self.assertTrue(self.kassa.syo_edullisesti_kortilla(self.maksukortti))
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_edullinen_ei_rahaa_kortilla(self):
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertFalse(self.kassa.syo_edullisesti_kortilla(self.maksukortti))
        self.assertEqual(self.kassa.edulliset, 4)
        self.assertEqual(self.maksukortti.saldo, 40)

    def test_kallis_kortilla(self):
        self.assertTrue(self.kassa.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kallis_ei_rahaa_kortilla(self):
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertFalse(self.kassa.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(self.kassa.maukkaat, 2)
        self.assertEqual(self.maksukortti.saldo, 200)

    def test_kortilla_maksu_kassa_muuttumaton(self):
        self.assertTrue(self.kassa.syo_edullisesti_kortilla(self.maksukortti))
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortille_rahan_lataus(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100500)
        self.assertEqual(self.maksukortti.saldo, 1500)
        #"Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä KASVAA ladatulla summalla"
        self.kassa.lataa_rahaa_kortille(self.maksukortti, -1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100500)
        self.assertEqual(self.maksukortti.saldo, 1500)