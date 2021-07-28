import re

class DisambiguatorPrefixPersonaRuleKu1(object):
    """
    afiks atau imbuhan yang diselipkan pada bagian depan kata dasar dan menjelaskan bentuk itu dengan subjek
    ku, mu, tu
    """

    def disambiguate(self, word):

        matches = re.match(r'^ku(.*)$', word)
        if matches:
            return matches.group(1)

class DisambiguatorPrefixPersonaRuleMu1(object):
    """
    afiks atau imbuhan yang diselipkan pada bagian depan kata dasar dan menjelaskan bentuk itu dengan subjek
    ku, mu, tu
    """

    def disambiguate(self, word):

        matches = re.match(r'^mu(.*)$', word)
        if matches:
            return matches.group(1)

class DisambiguatorPrefixPersonaRuleTu1(object):
    """
    afiks atau imbuhan yang diselipkan pada bagian depan kata dasar dan menjelaskan bentuk itu dengan subjek
    ku, mu, tu
    """

    def disambiguate(self, word):

        matches = re.match(r'^tu(.*)$', word)
        if matches:
            return matches.group(1)
