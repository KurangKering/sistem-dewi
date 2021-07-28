from library.algorithms.stemming.Stemmer.Context.Visitor.DontStemShortWord import DontStemShortWord
from library.algorithms.stemming.Stemmer.Context.Visitor.PrefixDisambiguator import PrefixDisambiguator

from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorPrefix import *
from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorPrefixPemanis import *
from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorPrefixPenanda import *
from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorPrefixPersona import *
from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorSuffixPersona import *
from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorInfix import *

class VisitorProvider(object):

    def __init__(self):
        self.visitors = []
        self.suffix_visitors = []
        self.infix_visitors = []
        self.prefix_visitors = []
        self.prefix_pemanis_visitors = []
        self.prefix_penanda_visitors = []
        self.prefix_persona_visitors = []

        self.init_visitors()

    def init_visitors(self):
        self.visitors.append(DontStemShortWord())

        self.suffix_visitors.append(PrefixDisambiguator([DisambiguatorSuffixRuleKu1()]))
        self.suffix_visitors.append(PrefixDisambiguator([DisambiguatorSuffixRuleMu1()]))
        self.suffix_visitors.append(PrefixDisambiguator([DisambiguatorSuffixRuleNya1()]))


        self.prefix_visitors.append(PrefixDisambiguator([
            DisambiguatorPrefixRuleN1(),
            DisambiguatorPrefixRuleN2(),
            DisambiguatorPrefixRuleN3(),
            DisambiguatorPrefixRuleN4(),
            DisambiguatorPrefixRuleN5(),
            DisambiguatorPrefixRuleN6(),
            DisambiguatorPrefixRuleN7(),
            DisambiguatorPrefixRuleN8(),
            DisambiguatorPrefixRuleN9(),
            DisambiguatorPrefixRuleN10(),
                ]))

        self.prefix_visitors.append(PrefixDisambiguator([
            DisambiguatorPrefixRuleKa1(),
            DisambiguatorPrefixRuleKa2(),
            DisambiguatorPrefixRuleKa3(),
            DisambiguatorPrefixRuleKa4(),
            DisambiguatorPrefixRuleN10(),
                ]))

        self.prefix_visitors.append(PrefixDisambiguator([
            DisambiguatorPrefixRuleBa1(),
            DisambiguatorPrefixRuleBa2(),
                ]))

        self.prefix_visitors.append(PrefixDisambiguator([
            DisambiguatorPrefixRulePa1(),
            DisambiguatorPrefixRulePa2(),
            DisambiguatorPrefixRulePa3(),
            DisambiguatorPrefixRulePa4(),
            DisambiguatorPrefixRulePa5(),
            DisambiguatorPrefixRulePa6(),
            DisambiguatorPrefixRulePa7(),
                ]))

        self.prefix_visitors.append(PrefixDisambiguator([
            DisambiguatorPrefixRuleSa1(),
            DisambiguatorPrefixRuleSa2(),
            DisambiguatorPrefixRuleSa3(),
            DisambiguatorPrefixRuleSa4(),
            DisambiguatorPrefixRuleSa5(),
                ]))

        self.prefix_visitors.append(PrefixDisambiguator([
            DisambiguatorPrefixRuleTu1(),
                ]))

        self.prefix_visitors.append(PrefixDisambiguator([
            DisambiguatorPrefixRuleYa1(),
                ]))

        self.prefix_visitors.append(PrefixDisambiguator([
            DisambiguatorPrefixRuleMa1(),
                ]))


        self.prefix_persona_visitors.append(PrefixDisambiguator([
            DisambiguatorPrefixPersonaRuleKu1(),
                ]))


        self.prefix_persona_visitors.append(PrefixDisambiguator([
            DisambiguatorPrefixPersonaRuleMu1(),
                ]))


        self.prefix_persona_visitors.append(PrefixDisambiguator([
            DisambiguatorPrefixPersonaRuleTu1(),
                ]))

        self.prefix_penanda_visitors.append(PrefixDisambiguator([
            DisambiguatorPrefixPenandaRuleKa1(),
                ]))

        self.prefix_pemanis_visitors.append(PrefixDisambiguator([
            DisambiguatorPrefixPemanisRuleMo1(),
                ]))



        self.infix_visitors.append(PrefixDisambiguator([DisambiguatorInfixRuleEn1()]))
        self.infix_visitors.append(PrefixDisambiguator([DisambiguatorInfixRuleEn2()]))


    def get_visitors(self):
        return self.visitors

    def get_suffix_visitors(self):
        return self.suffix_visitors

    def get_prefix_visitors(self):
        return self.prefix_visitors

    def get_prefix_pemanis_visitors(self):
        return self.prefix_pemanis_visitors

    def get_prefix_penanda_visitors(self):
        return self.prefix_penanda_visitors

    def get_prefix_persona_visitors(self):
        return self.prefix_persona_visitors


    def get_infix_visitors(self):
        return self.infix_visitors

