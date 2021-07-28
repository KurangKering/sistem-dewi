import re

class DisambiguatorSuffixRuleKu1(object):
    """
    afiks atau imbuhan yang terdapat padaakhir kata,
    contoh:
    denganku: dengan
    """

    def disambiguate(self, word):
        matches = re.match(r'^(.*)ku$', word)
        if matches:
            return matches.group(1)

class DisambiguatorSuffixRuleMu1(object):
    """
    afiks atau imbuhan yang terdapat padaakhir kata,
    contoh:
    mentuamu : mentua
    """

    def disambiguate(self, word):
        matches = re.match(r'^(.*)mu$', word)
        if matches:
            return matches.group(1)

class DisambiguatorSuffixRuleNya1(object):
    """
    afiks atau imbuhan yang terdapat padaakhir kata,
    contoh:
    adinya: adi
    """

    def disambiguate(self, word):
        matches = re.match(r'^(.*)nya$', word)
        if matches:
            return matches.group(1)
