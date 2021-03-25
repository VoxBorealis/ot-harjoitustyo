import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassassa_oikea_määrä_rahaa_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kassassa_edulliset_oikein_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassassa_maukkaat_oikein_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    ##
    def test_syo_edullisesti_kateisella_toimii_kassan_saldo_nousee(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_toimii_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_syo_edullisesti_kateisella_toimii_edullinen_counter_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_toimii_maksu_ei_riittava_kassan_saldo_ei_nouse(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisella_toimii_maksu_ei_riittava_kaikki_rahat_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_syo_edullisesti_kateisella_toimii_maksu_ei_riittava_edullinen_counter_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    ##
    def test_syo_maukkaasti_kateisella_toimii_kassan_saldo_nousee(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kateisella_toimii_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_syo_maukkaasti_kateisella_toimii_edullinen_counter_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_toimii_maksu_ei_riittava_kassan_saldo_ei_nouse(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella_toimii_maksu_ei_riittava_kaikki_rahat_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_syo_maukkaasti_kateisella_toimii_maksu_ei_riittava_edullinen_counter_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)
##
    def test_syo_edullisti_kortilla_toimii_veloitetaan_summa_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")

    def test_syo_edullisesti_kortilla_toimii_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_syo_edullisesti_kortilla_toimii_edulliset_counter_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla_toimii_ei_veloiteta_summaa_kortilta_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_syo_edullisesti_kortilla_toimii_edulliset_counter_ei_nouse_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_edullisesti_kortilla_toimii_palauttaa_false_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.saldo = 100
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)

    def test_syo_edullisesti_kortilla_toimii_kassan_rahamaara_ei_nouse(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
##
    def test_syo_maukkaasti_kortilla_toimii_veloitetaan_summa_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")

    def test_syo_maukkaasti_kortilla_toimii_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
    
    def test_syo_maukkaasti_kortilla_toimii_maukkaat_counter_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_toimii_ei_veloiteta_summaa_kortilta_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_syo_maukkaasti_kortilla_toimii_maukkaat_counter_ei_nouse_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kortilla_toimii_palauttaa_false_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.saldo = 100
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)

    def test_syo_maukkaasti_kortilla_toimii_kassan_rahamaara_ei_nouse(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille_toimii_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(str(self.maksukortti), "saldo: 11.0")

    def test_lataa_rahaa_kortille_toimii_kassan_raha_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_lataa_rahaa_kortille_toimii_summa_pienempi_kuin_nolla_kortin_saldo_ei_kasva(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -5)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_lataa_rahaa_kortille_toimii_summa_pienempi_kuin_nolla_kassan_raha_ei_kasva(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -5)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)