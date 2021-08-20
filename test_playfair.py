#!/usr/bin/env python3
import unittest
from playfair import _generateTable, _createBigrams, decrypt, encrypt

class TestPlayfair(unittest.TestCase):
    def test_generateTable(self):
        self.assertAlmostEqual(''.join([str(ele) for ele in [''.join(ele) for ele in _generateTable("TEST")]]),"TESABCDFGHIKLMNOPQRUVWXYZ")
        self.assertAlmostEqual(''.join([str(ele) for ele in [''.join(ele) for ele in _generateTable("wheatstone")]]),"WHEATSONBCDFGIKLMPQRUVXYZ")
        self.assertAlmostEqual(''.join([str(ele) for ele in [''.join(ele) for ele in _generateTable("MoNtHlY")]]),"MONTHLYABCDEFGIKPQRSUVWXZ")
        self.assertAlmostEqual(''.join([str(ele) for ele in [''.join(ele) for ele in _generateTable("")]]),"ABCDEFGHIKLMNOPQRSTUVWXYZ")

    def test_createBigrams(self):
        self.assertAlmostEqual(''.join(str(ele) for ele in _createBigrams("Tajna Wiadomosc")), "TAINAWIADOMOSC")
        self.assertAlmostEqual(''.join(str(ele) for ele in _createBigrams("$UP3R T4JN4_W14D0M0$C")), "UPRTINWDMC")
        self.assertAlmostEqual(''.join(str(ele) for ele in _createBigrams("Can't touch this")), "CANTTOUCHTHISX")
        self.assertAlmostEqual(''.join(str(ele) for ele in _createBigrams("światjestszalonyzar#123132123131321ezwariuje")), "WIATIESTSZALONYZAREZWARIUIEX")

    def test_encrypt(self):
        self.assertAlmostEqual(encrypt("testowy super napis", "monthly"), "OGRHNVC PVKGP AFSERZ")
        self.assertAlmostEqual(encrypt("testowy super napis", "mont hly"), "OGRHNVC PVKGP AFSERZ")
        self.assertAlmostEqual(encrypt("MonthlyFlag{SUP3R_FL464_W_PL41F41R}", "wheatstone"), "VFCEWMVIQWD{NXL3M_KU464_S_QM41K41M}")
        self.assertAlmostEqual(encrypt("12312112NIE12313123ODCZY141212TASZ123131312TE123123123GO", "hardtoread"), "12312112PGB12313123ECLVZ141212HRUY123131312AF123123123NG")
        self.assertAlmostEqual(encrypt("MU$1SZ_W1DZ13C_CYFRY_Z3BY_PRZ3CZYT4C", "apsdasdadawdadasd"), "HZ$1WX_A1WV13G_FVLYZ_U3FU_DOV3GUZO4G")

    def test_decrypt(self):
        self.assertAlmostEqual(decrypt("MQDzqdor{Ix4Oa41W_1F_B00h_m1YlqPpPP}","qwertyuiopasdfghklzxcvbnm"),"CTFLEARN{PL4YF41R_1S_C00L_C1PHERRRR}")
        self.assertAlmostEqual(decrypt("OGRHNVC PVKGP AFSERZ","monthly"),"TESTOWY SUPER NAPISX")
        self.assertAlmostEqual(decrypt("OGRHNVC PVKGP AFSERZ","mont hly"),"TESTOWY SUPER NAPISX")
        self.assertAlmostEqual(decrypt("VFCEWMVIQWD{NXL3M_KU464_S_QM41K41M}","wheatstone"),"MONTHLYFLAG{SUP3R_FL464_W_PL41F41R}")
        self.assertAlmostEqual(decrypt("12312112PGB12313123ECLVZ141212HRUY123131312AF123123123NG","hardtoread"),"12312112NIE12313123ODCZY141212TASZ123131312TE123123123GO")
        self.assertAlmostEqual(decrypt("HZ$1WX_A1WV13G_FVLYZ_U3FU_DOV3GUZO4G","apsdasdadawdadasd"),"MU$1SZ_W1DZ13C_CYFRY_Z3BY_PRZ3CZYT4C")