from django.test import TestCase, Client
from pprint import pprint
from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorPrefixPemanis import *
# Create your tests here.
#
#

class DisambiguatorPrefixPemanisTests(TestCase):
    """
    afiks atau imbuhan yang berfungsi sebagai pelengkap prefiks yang telah di tambahkan dalam sebuah kata, prefiks pemanis berada di antara imbuhan dan kata dasar
    """
    def test_DisambiguatorPrefixPemanisRuleMo1(self):
        disambiguator = DisambiguatorPrefixPemanisRuleMo1()
        word = "kamolempo"
        target = "kalempo"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)
