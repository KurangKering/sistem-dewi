from django.test import TestCase, Client
from pprint import pprint
from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorInfix import *
# Create your tests here.
#
#

class DisambiguatorInfixTests(TestCase):

    """
    afiks atau imbuhan yang terdapat di dalam kata
    contoh :
    tenri -> teri
    senda -> seda
    """
    def test_DisambiguatorInfixRuleEn1(self):
        disambiguator = DisambiguatorInfixRuleEn1()
        word = "tenri"
        target = "teri"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)

    """
    afiks atau imbuhan yang terdapat di dalam kata
    contoh :
    kemban -> keban
    """
    def test_DisambiguatorInfixRuleEn2(self):
        disambiguator = DisambiguatorInfixRuleEn2()
        word = "kemban"
        target = "keban"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)
