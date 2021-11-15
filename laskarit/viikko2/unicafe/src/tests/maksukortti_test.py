import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)
    
    def test_onko_rahaa_kortilla(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        vastaus = self.maksukortti.saldo
        self.assertEqual(vastaus, 20)

    def test_onko_rahee(self):
        self.maksukortti.ota_rahaa(5)
        vastaus = self.maksukortti.saldo
        self.assertEqual(vastaus, 5)
    
    def test_onko_rahaa(self):
        self.maksukortti.ota_rahaa(11)
        vastaus = self.maksukortti.saldo
        self.assertEqual(vastaus, 10)
    
    def test_oliko_tarpeeksi(self):
        vastaus1 = self.maksukortti.ota_rahaa(6)
        vastaus2 = self.maksukortti.ota_rahaa(6)
        self.assertTrue(vastaus1)
        self.assertFalse(vastaus2)

    def test_palautus(self):
        vastaus = self.maksukortti
        self.assertEqual(str(vastaus), "saldo: 0.1")