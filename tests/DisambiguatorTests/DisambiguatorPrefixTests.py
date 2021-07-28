from django.test import TestCase, Client
from pprint import pprint
from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorPrefix import *
# Create your tests here.
#
#

class DisambiguatorPrefixTests(TestCase):
    """
    Bentuk dasar diawali /p
    contoh :
    mikir -> pikir
    mukil -> pukil
    mato -> pato
    """
    def test_DisambiguatorPrefixRuleN1(self):
        disambiguator = DisambiguatorPrefixRuleN1()
        word = "mikir"
        target = "pikir"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)

    """
    Bentuk dasar diawali /b
    contoh :
    mukil -> Beli
    metak -> betak
    """
    def test_DisambiguatorPrefixRuleN2(self):
        disambiguator = DisambiguatorPrefixRuleN2()
        word = "metak"
        target = "betak"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    Bentuk dasar diawali /t
    contoh :
    nurit -> turit
    nangis -> tangis
    nanam -> tanam
    """
    def test_DisambiguatorPrefixRuleN3(self):
        disambiguator = DisambiguatorPrefixRuleN3()
        word = "nurit"
        target = "turit"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)

    """
    Bentuk dasar diawali /d
    contoh :
    napat -> dapat
    """
    def test_DisambiguatorPrefixRuleN4(self):
        disambiguator = DisambiguatorPrefixRuleN4()
        word = "napat"
        target = "dapat"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    Bentuk dasar diawali /k
    contoh :
    ngareng  -> Kareng
    ngunci  -> Kunci
    """
    def test_DisambiguatorPrefixRuleN5(self):
        disambiguator = DisambiguatorPrefixRuleN5()
        word = "ngareng"
        target = "kareng"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    Bentuk dasar diawali /g
    contoh :
    ngoco  -> goco
    ngali  -> gali
    """
    def test_DisambiguatorPrefixRuleN6(self):
        disambiguator = DisambiguatorPrefixRuleN6()
        word = "ngoco"
        target = "goco"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)



    """
    Bentuk dasar diawali /c
    contoh :
    nyela  -> cela
    nyoba  -> coba
    """
    def test_DisambiguatorPrefixRuleN7(self):
        disambiguator = DisambiguatorPrefixRuleN7()
        word = "nyela"
        target = "cela"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)



    """
    Bentuk dasar diawali /s
    contoh :
    nyoro  -> soro
    nyawit  -> sawit
    """
    def test_DisambiguatorPrefixRuleN8(self):
        disambiguator = DisambiguatorPrefixRuleN8()
        word = "nyoro"
        target = "soro"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    Bentuk dasar diawali huruf vokal
    contoh :
    ngapan   -> apan
    ngentin  -> entin
    """
    def test_DisambiguatorPrefixRuleN9(self):
        disambiguator = DisambiguatorPrefixRuleN9()
        word = "ngapan"
        target = "apan"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)



    """
    bentuk dasar bersuku tunggal yang fonem depannya sebuah  konsonan
    contoh :
    ngesit   -> sit
    ngerik  -> rik
    """
    def test_DisambiguatorPrefixRuleN10(self):
        disambiguator = DisambiguatorPrefixRuleN10()
        word = "ngesit"
        target = "sit"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    dirangkaikan dengan bentuk dasar fonem depan vokal
    contoh :
    kangada   -> ada
    kangalup  -> alup
    """
    def test_DisambiguatorPrefixRuleKa1(self):
        disambiguator = DisambiguatorPrefixRuleKa1()
        word = "kangada"
        target = "ada"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    Penggabungan prefiks ka- dengan fonem dasar dengan fonem depan /b
    contoh :
    Kamengkak   -> Bengkak
    kamaeng  -> Baeng
    """
    def test_DisambiguatorPrefixRuleKa2(self):
        disambiguator = DisambiguatorPrefixRuleKa2()
        word = "kamengkak"
        target = "bengkak"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    Penggabungan prefiks ka- dengan fonem dasar dengan fonem depan /ds
    contoh :
    kanapat   -> Dapat
    kaningin  -> Dingin
    """
    def test_DisambiguatorPrefixRuleKa3(self):
        disambiguator = DisambiguatorPrefixRuleKa3()
        word = "kanapat"
        target = "dapat"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    Penghilangan prefix ka-
    contoh :
    kapukil   -> pukil
    """
    def test_DisambiguatorPrefixRuleKa4(self):
        disambiguator = DisambiguatorPrefixRuleKa4()
        word = "kapukil"
        target = "pukil"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)

    """
    bentuk dasar bersuku dua
    contoh :
    barotak   -> otak
    """
    def test_DisambiguatorPrefixRuleBa1(self):
        disambiguator = DisambiguatorPrefixRuleBa1()
        word = "barotak"
        target = "otak"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    bentuk dasar bersuku tunggal yang fonem depannya sebuah  konsonan
    contoh :
    baretin   -> tin
    baredo  -> do
    """
    def test_DisambiguatorPrefixRuleBa2(self):
        disambiguator = DisambiguatorPrefixRuleBa2()
        word = "baretin"
        target = "tin"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    prefiks pa- diikuti bentuk dasar bersuku dua
    contoh :
    paroras   -> oras
    """
    def test_DisambiguatorPrefixRulePa1(self):
        disambiguator = DisambiguatorPrefixRulePa1()
        word = "paroras"
        target = "oras"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    prefiks pa- diikuti bentuk dasar bersuku dua
    contoh :
    pangkenang   -> kenang
    """
    def test_DisambiguatorPrefixRulePa2(self):
        disambiguator = DisambiguatorPrefixRulePa2()
        word = "pangkenang"
        target = "kenang"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    prefiks pa- diikuti bentuk dasar bersuku dua
    contoh :
    pangeneng   -> eneng
    """
    def test_DisambiguatorPrefixRulePa3(self):
        disambiguator = DisambiguatorPrefixRulePa3()
        word = "pangeneng"
        target = "eneng"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)



    """
    prefiks pa- diikuti bentuk dasar bersuku tunggal fonem awal konsonan
    contoh :
    pangesat   -> sat
    """
    def test_DisambiguatorPrefixRulePa4(self):
        disambiguator = DisambiguatorPrefixRulePa4()
        word = "pangesat"
        target = "sat"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    prefiks pa- dirangkaikan dengan bentuk dasar yang fonem awalnya adalah konsonan /b
    contoh :
    pameang   -> beang
    """
    def test_DisambiguatorPrefixRulePa5(self):
        disambiguator = DisambiguatorPrefixRulePa5()
        word = "pameang"
        target = "beang"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    prefiks pa- dirangkaikan dengan bentuk dasar yang fonem awalnya adalah konsonan /s
    contoh :
    panyisir   -> sisir
    """
    def test_DisambiguatorPrefixRulePa6(self):
        disambiguator = DisambiguatorPrefixRulePa6()
        word = "panyisir"
        target = "sisir"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    prefiks pa- dirangkaikan dengan bentuk dasar yang fonem awalnya adalah konsonan /t
    contoh :
    panamuk   -> tamuk
    """
    def test_DisambiguatorPrefixRulePa7(self):
        disambiguator = DisambiguatorPrefixRulePa7()
        word = "panamuk"
        target = "tamuk"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)

    """
    Perangkaian prefiks sa- dengan bentuk dasar bersuku dua  mengakibatkan  penambahan sebuah fonem nasal di antara  prefiks sa- dan bentuk dasarnya
    contoh :
    sangkurang   -> kurang
    """
    def test_DisambiguatorPrefixRuleSa1(self):
        disambiguator = DisambiguatorPrefixRuleSa1()
        word = "sangkurang"
        target = "kurang"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    prefiks sa-dirangkaikan dengan bentuk dasar bersuku kata tunggal dengan fonem depan konsonan / n / ditambahkan di antara prefiks sa- dan bentuk dasarnya
    contoh :
    sangesat   -> sat
    """
    def test_DisambiguatorPrefixRuleSa2(self):
        disambiguator = DisambiguatorPrefixRuleSa2()
        word = "sangesat"
        target = "sat"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)



    """
    prefiks sa- bergabung dengan bentuk dasar bersuku dua yang fonem depannya adalah konsonan / b
    contoh :
    samalik   -> balik
    """
    def test_DisambiguatorPrefixRuleSa3(self):
        disambiguator = DisambiguatorPrefixRuleSa3()
        word = "samalik"
        target = "balik"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)



    """
    prefiks sa- bergabung dengan bentuk dasar bersuku dua yang fonem depannya adalah konsonan / d
    contoh :
    sanadi   -> dadi
    """
    def test_DisambiguatorPrefixRuleSa4(self):
        disambiguator = DisambiguatorPrefixRuleSa4()
        word = "sanadi"
        target = "dadi"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    prefiks sa- bergabung dengan bentuk dasar bersuku dua yang fonem depannya adalah konsonan / g
    contoh :
    sangila   -> Gila
    """
    def test_DisambiguatorPrefixRuleSa5(self):
        disambiguator = DisambiguatorPrefixRuleSa5()
        word = "sangila"
        target = "gila"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    penghilangan fonem terhadap kata dasar
    contoh :
    Tutetak   -> tetak
    """
    def test_DisambiguatorPrefixRuleTu1(self):
        disambiguator = DisambiguatorPrefixRuleTu1()
        word = "tutetak"
        target = "tetak"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    penghilangan fonem terhadap kata dasar
    contoh :
    Yabawa   -> bawa
    """
    def test_DisambiguatorPrefixRuleYa1(self):
        disambiguator = DisambiguatorPrefixRuleYa1()
        word = "yabawa"
        target = "bawa"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    penghilangan fonem terhadap kata dasar
    contoh :
    malentak   -> lentak
    """
    def test_DisambiguatorPrefixRuleMa1(self):
        disambiguator = DisambiguatorPrefixRuleMa1()
        word = "malentak"
        target = "lentak"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)
