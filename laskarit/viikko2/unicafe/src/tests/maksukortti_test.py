import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_maksukortti_str_toimii(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    #kortin saldo alussa oikein
    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)


    #Rahan lataaminen kasvattaa saldoa oikein
    def test_raha_latautuu_kortille_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)


    #Saldo vähenee oikein, jos rahaa on tarpeeksi
    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)


    #Saldo ei muutu, jos rahaa ei ole tarpeeksi
    def test_saldo_ei_muutu_jos_ei_saldoa(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    #Metodi palauttaa True, jos rahat riittivät...
    def test_ota_rahaa_palauttaa_true_jos_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)

    #... ja muuten False
    def test_ota_rahaa_palauttaa_false_jos_ei_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)

