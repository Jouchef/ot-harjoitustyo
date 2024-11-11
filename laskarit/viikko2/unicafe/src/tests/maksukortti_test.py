import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_positiivisen_summan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 11.0)

    def test_jos_rahaa_tarpeeksi_summa_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 9.0)

    def test_saldo_ei_muutu_jos_kate_ei_riita(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_ota_rahaa_palauttaa_true_jos_raha_riittaa(self):
        vastaus = self.maksukortti.ota_rahaa(100)

        self.assertEqual(vastaus, True)

    def test_ota_rahaa_palauttaa_false_jos_raha_ei_riita(self):
        vastaus = self.maksukortti.ota_rahaa(1100)

        self.assertEqual(vastaus, False)