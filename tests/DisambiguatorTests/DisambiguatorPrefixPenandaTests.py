from django.test import TestCase, Client
from pprint import pprint
from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorPrefixPenanda import *
# Create your tests here.
#
#

class DisambiguatorPrefixPenandaTests(TestCase):
    """
    contoh:
    katama -> tama
    yabeli -> beli
    """
    def test_DisambiguatorPrefixPenandaRuleKa1(self):
        disambiguator = DisambiguatorPrefixPenandaRuleKa1()
        word = ["katama", "yabeli"]
        target = ["tama", "beli"]
        result1 = disambiguator.disambiguate(word[0])
        result2 = disambiguator.disambiguate(word[1])
        return self.assertEquals(target[0], result1)
        return self.assertEquals(target[1], result2)
