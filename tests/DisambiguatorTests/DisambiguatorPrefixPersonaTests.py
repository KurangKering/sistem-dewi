from django.test import TestCase, Client
from pprint import pprint
from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorPrefixPersona import *
# Create your tests here.
#
#

class DisambiguatorPrefixPersonaTests(TestCase):

    """
    afiks atau imbuhan yang diselipkan pada bagian depan kata dasar dan menjelaskan bentuk itu dengan subjek
    ku,
    """
    def test_DisambiguatorPrefixPersonaRuleKu1(self):
        disambiguator = DisambiguatorPrefixPersonaRuleKu1()
        word = "kupukil"
        target = "pukil"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)


    """
    afiks atau imbuhan yang diselipkan pada bagian depan kata dasar dan menjelaskan bentuk itu dengan subjek
    mu
    """
    def test_DisambiguatorPrefixPersonaRuleMu1(self):
        disambiguator = DisambiguatorPrefixPersonaRuleMu1()
        word = "mungaku"
        target = "ngaku"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)

    """
    afiks atau imbuhan yang diselipkan pada bagian depan kata dasar dan menjelaskan bentuk itu dengan subjek
    tu
    """
    def test_DisambiguatorPrefixPersonaRuleTu1(self):
        disambiguator = DisambiguatorPrefixPersonaRuleTu1()
        word = "tusamate"
        target = "samate"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)
