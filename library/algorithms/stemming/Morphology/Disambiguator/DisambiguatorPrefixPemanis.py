import re

class DisambiguatorPrefixPemanisRuleMo1(object):
    """
    afiks atau imbuhan yang berfungsi sebagai pelengkap prefiks yang telah di tambahkan dalam sebuah kata, prefiks pemanis berada di antara imbuhan dan kata dasar
    """

    def disambiguate(self, word):

        matches = re.match(r'^(.*)mo(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)
