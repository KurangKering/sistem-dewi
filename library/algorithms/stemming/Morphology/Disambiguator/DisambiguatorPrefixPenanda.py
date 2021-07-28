import re

class DisambiguatorPrefixPenandaRuleKa1(object):

    """
    contoh:
    katama -> tama
    yabeli -> beli
    """
    def disambiguate(self, word):
        matches = re.match(r'^(ka|ya)(.*)$', word)
        if matches:
            return matches.group(2)
