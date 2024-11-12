import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    #Luodun kassapäätteen rahamäärä  on oikea (rahaa 1000 euroa)
    def test_kassapaateessa_oikea_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassapaateessa_aluksi_nolla_myytya_lounasta(self):
        myyty = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(myyty, 0)

    def test_kassassa_rahaa_euroina(self):
        kassa_euroina = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(kassa_euroina, 1000)

    #Käteismaksu: Jos maksu riittävä: kassassa oleva rahamäärä kasvaa 
    # lounaan hinnalla ja vaihtorahan suuruus on oikea
    def test_kateisella_edullisesti_vaihtoraha_oikein_ja_kassa_kasvaa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(vaihtoraha, 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisella_maukkaasti_vaihtoraha_oikein_ja_kassa_kasvaa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(vaihtoraha, 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maksu_ei_riittava_edullisesti_raha_palautetaan(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200) 

    def test_maksu_ei_riittava_maukkaasti_raha_palautetaan(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(vaihtoraha, 390) 

    def test_maksu_ei_riittava_kassa_ei_muutu_lounasmaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        myyty = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(myyty, 0)  

    def test_kortilla_rahaa_veloitetaan_edullisesti_ja_palautuu_true(self):
        kortti = Maksukortti(500)
        tapahtuma = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(tapahtuma, True)   
        self.assertEqual(kortti.saldo_euroina(), 2.6)   

    def test_korttimaksussa_edullisesti_lounaiden_maara_kasvaa(self):
        kortti = Maksukortti(500)
        tapahtuma = self.kassapaate.syo_edullisesti_kortilla(kortti) 
        self.assertEqual(self.kassapaate.edulliset, 1)      

    def test_kortilla_ei_katetta_edullisesti_palautuu_false(self):
        kortti = Maksukortti(100)
        tapahtuma = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(tapahtuma, False)

    def test_kortilla_rahaa_veloitetaan_maukkaasti_ja_palautuu_true(self):
        kortti = Maksukortti(500)
        tapahtuma = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(tapahtuma, True)   
        self.assertEqual(kortti.saldo_euroina(), 1.0)   

    def test_korttimaksussa_maukkaasti_lounaiden_maara_kasvaa(self):
        kortti = Maksukortti(500)
        tapahtuma = self.kassapaate.syo_maukkaasti_kortilla(kortti) 
        self.assertEqual(self.kassapaate.maukkaat, 1)      

    def test_kortilla_ei_katetta_maukkaasti_palautuu_false(self):
        kortti = Maksukortti(100)
        tapahtuma = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(tapahtuma, False)

    def test_kassassa_oleva_raha_ei_muutu_maksaessa_kortilla(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.kassapaate.syo_edullisesti_kortilla(kortti)  
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000) 

    def test_kortille_ladattaessa_saldo_muuttuu_ja_kassa_kasvaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 400)   
        self.assertEqual(kortti.saldo, 1400)   
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400) 

    def test_ladataan_kortille_neq_summa_palautuu_false(self):
        kortti = Maksukortti(100)
        tapahtuma = self.kassapaate.lataa_rahaa_kortille(kortti, -400)   
        self.assertEqual(tapahtuma, None)      