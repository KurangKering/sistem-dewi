import re

class PrecedenceAdjustmentSpecification(object):
    def is_satisfied_by(self, value):
        regex_rules = [
            r'^be(.*)lah$',
            r'^be(.*)an$',
            r'^me(.*)i$',
            r'^di(.*)i$',
            r'^pe(.*)i$',
            r'^ter(.*)i$',
        ]

        for rule in regex_rules:
            if re.match(rule, value):
                return True

        return False



