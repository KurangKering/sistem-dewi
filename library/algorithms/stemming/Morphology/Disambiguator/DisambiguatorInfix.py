import re

class DisambiguatorInfixRuleEn1(object):
    """
    afiks atau imbuhan yang terdapat di dalam kata
    contoh :
    tenri -> teri
    senda -> seda
    """

    def disambiguate(self, word):

        matches = re.match(r'^([^aiueo]e)n(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)

class DisambiguatorInfixRuleEn2(object):
    """
    afiks atau imbuhan yang terdapat di dalam kata
    contoh :
    kemban -> keban
    """

    def disambiguate(self, word):

        matches = re.match(r'^([^aiueo]e)m(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)

