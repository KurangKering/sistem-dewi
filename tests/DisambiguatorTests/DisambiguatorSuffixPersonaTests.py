from django.test import TestCase, Client
from pprint import pprint
from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorSuffixPersona import *
# Create your tests here.
#
#

class DisambiguatorSuffixPersonaTests(TestCase):

    """
    afiks atau imbuhan yang terdapat padaakhir kata,
    contoh:
    denganku: dengan
    """
    def test_DisambiguatorSuffixRuleKu1(self):
        disambiguator = DisambiguatorSuffixRuleKu1()
        word = "denganku"
        target = "dengan"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)

    """
    afiks atau imbuhan yang terdapat padaakhir kata,
    contoh:
    mentuamu : mentua
    """
    def test_DisambiguatorSuffixRuleMu1(self):
        disambiguator = DisambiguatorSuffixRuleMu1()
        word = "mentuamu"
        target = "mentua"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)

    """
    afiks atau imbuhan yang terdapat padaakhir kata,
    contoh:
    adinya: adi
    """
    def test_DisambiguatorSuffixRuleNya1(self):
        disambiguator = DisambiguatorSuffixRuleNya1()
        word = "adinya"
        target = "adi"
        result = disambiguator.disambiguate(word)
        return self.assertEquals(target, result)
