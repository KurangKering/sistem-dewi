import re



class DisambiguatorPrefixRuleN1(object):
    """
    Bentuk dasar diawali /p
    contoh :
    mikir -> pikir
    mukil -> pukil
    mato -> pato
    """

    def disambiguate(self, word):

        matches = re.match(r'^m([aiueo][^aiueo].*)$', word)
        if matches:
            return 'p' + matches.group(1)

class DisambiguatorPrefixRuleN2(object):
    """
    Bentuk dasar diawali /b
    contoh :
    mukil -> Beli
    metak -> betak
    """

    def disambiguate(self, word):

        matches = re.match(r'^m([aiueo][^aiueo].*)$', word)
        if matches:
            return 'b' + matches.group(1)

class DisambiguatorPrefixRuleN3(object):
    """
    Bentuk dasar diawali /t
    contoh :
    nurit -> turit
    nangis -> tangis
    nanam -> tanam
    """

    def disambiguate(self, word):

        matches = re.match(r'^n([aiueo][^aiueo].*)$', word)
        if matches:
            return 't' + matches.group(1)


class DisambiguatorPrefixRuleN4(object):
    """
    Bentuk dasar diawali /d
    contoh :
    napat -> dapat
    """

    def disambiguate(self, word):

        matches = re.match(r'^n([aiueo][^aiueo].*)$', word)
        if matches:
            return 'd' + matches.group(1)


class DisambiguatorPrefixRuleN5(object):
    """
    Bentuk dasar diawali /k
    contoh :
    ngareng  -> Kareng
    ngunci  -> Kunci
    """

    def disambiguate(self, word):

        matches = re.match(r'^ng([aiueo][^aiueo].*)$', word)
        if matches:
            return 'k' + matches.group(1)

class DisambiguatorPrefixRuleN6(object):
    """
    Bentuk dasar diawali /g
    contoh :
    ngoco  -> goco
    ngali  -> gali
    """

    def disambiguate(self, word):

        matches = re.match(r'^ng([aiueo][^aiueo].*)$', word)
        if matches:
            return 'g' + matches.group(1)


class DisambiguatorPrefixRuleN7(object):
    """
    Bentuk dasar diawali /c
    contoh :
    nyela  -> cela
    nyoba  -> coba
    """

    def disambiguate(self, word):

        matches = re.match(r'^ny([aiueo][^aiueo].*)$', word)
        if matches:
            return 'c' + matches.group(1)


class DisambiguatorPrefixRuleN8(object):
    """
    Bentuk dasar diawali /s
    contoh :
    nyoro  -> soro
    nyawit  -> sawit
    """

    def disambiguate(self, word):

        matches = re.match(r'^ny([aiueo][^aiueo].*)$', word)
        if matches:
            return 's' + matches.group(1)


class DisambiguatorPrefixRuleN9(object):
    """
    Bentuk dasar diawali huruf vokal
    contoh :
    ngapan   -> apan
    ngentin  -> entin
    """

    def disambiguate(self, word):

        matches = re.match(r'^ng([aiueo][^aiueo].*)$', word)
        if matches:
            return matches.group(1)


class DisambiguatorPrefixRuleN10(object):
    """
    bentuk dasar bersuku tunggal yang fonem depannya sebuah  konsonan
    contoh :
    ngesit   -> sit
    ngerik  -> rik
    """

    def disambiguate(self, word):
        matches = re.match(r'^nge([^aiueo]*[aiueo]+[^aiueo]*)$', word)
        if matches:
            return matches.group(1)



class DisambiguatorPrefixRuleKa1(object):
    """
    dirangkaikan dengan bentuk dasar fonem depan vokal
    contoh :
    kangada   -> ada
    kangalup  -> alup
    """

    def disambiguate(self, word):

        matches = re.match(r'^kang([aiueo][^aiueo].*)$', word)
        if matches:
            return matches.group(1)


class DisambiguatorPrefixRuleKa2(object):
    """
    Penggabungan prefiks ka- dengan fonem dasar dengan fonem depan /b
    contoh :
    Kamengkak   -> Bengkak
    kamaeng  -> Baeng
    """

    def disambiguate(self, word):

        matches = re.match(r'^kam([aiueo][^aiueo].*)$', word)
        if matches:
            return 'b' + matches.group(1)

class DisambiguatorPrefixRuleKa3(object):
    """
    Penggabungan prefiks ka- dengan fonem dasar dengan fonem depan /ds
    contoh :
    kanapat   -> Dapat
    kaningin  -> Dingin
    """

    def disambiguate(self, word):

        matches = re.match(r'^kan([aiueo][^aiueo].*)$', word)
        if matches:
            return 'd' + matches.group(1)

class DisambiguatorPrefixRuleKa4(object):
    """
    Penghilangan prefix ka-
    contoh :
    kapukil   -> pukil
    """

    def disambiguate(self, word):

        matches = re.match(r'^ka([^aiueo].*)$', word)
        if matches:
            return matches.group(1)

class DisambiguatorPrefixRuleBa1(object):
    """
    bentuk dasar bersuku dua
    contoh :
    bar-otak   -> otak
    """

    def disambiguate(self, word):

        matches = re.match(r'^bar([^aiueo]*[aiueo]+[^aiueo]*[aiueo]+[^aiueo]*)$', word)
        if matches:
            return matches.group(1)



class DisambiguatorPrefixRuleBa2(object):
    """
    bentuk dasar bersuku tunggal yang fonem depannya sebuah  konsonan
    contoh :
    baretin   -> tin
    baredo  -> do
    """

    def disambiguate(self, word):
        matches = re.match(r'^bare([^aiueo]*[aiueo]+[^aiueo]*)$', word)
        if matches:
            return matches.group(1)


class DisambiguatorPrefixRulePa1(object):
    """
    prefiks pa- diikuti bentuk dasar bersuku dua
    contoh :
    paroras   -> oras
    """

    def disambiguate(self, word):
        matches = re.match(r'^par([^aiueo]*[aiueo]+[^aiueo]*[aiueo]+[^aiueo]*)$', word)
        if matches:
            return matches.group(1)


class DisambiguatorPrefixRulePa2(object):
    """
    prefiks pa- diikuti bentuk dasar bersuku dua
    contoh :
    pang-kenang   -> kenang
    """

    def disambiguate(self, word):
        matches = re.match(r'^pang([^aiueo]+[aiueo]+[^aiueo]*[aiueo]+[^aiueo]*)$', word)
        if matches:
            return matches.group(1)

class DisambiguatorPrefixRulePa3(object):
    """
    prefiks pa- diikuti bentuk dasar bersuku dua
    contoh :
    pangeneng   -> eneng
    """

    def disambiguate(self, word):
        matches = re.match(r'^pang([^aiueo]*[aiueo]+[^aiueo]*[aiueo]+[^aiueo]*)$', word)
        if matches:
            return matches.group(1)



class DisambiguatorPrefixRulePa4(object):
    """
    prefiks pa- diikuti bentuk dasar bersuku tunggal fonem awal konsonan
    contoh :
    pange-sat   -> sat
    """

    def disambiguate(self, word):
        matches = re.match(r'^pange([^aiueo]+[aiueo]+[^aiueo]*)$', word)
        if matches:
            return matches.group(1)


class DisambiguatorPrefixRulePa5(object):
    """
    prefiks pa- dirangkaikan dengan bentuk dasar yang fonem awalnya adalah konsonan /b
    contoh :
    pameang   -> beang
    """

    def disambiguate(self, word):
        matches = re.match(r'^pam([aiueo].*)$', word)
        if matches:
            return 'b' + matches.group(1)


class DisambiguatorPrefixRulePa6(object):
    """
    prefiks pa- dirangkaikan dengan bentuk dasar yang fonem awalnya adalah konsonan /s
    contoh :
    panyisir   -> sisir
    """

    def disambiguate(self, word):
        matches = re.match(r'^pany([aiueo].*)$', word)
        if matches:
            return 's' + matches.group(1)


class DisambiguatorPrefixRulePa7(object):
    """
    prefiks pa- dirangkaikan dengan bentuk dasar yang fonem awalnya adalah konsonan /t
    contoh :
    panamuk   -> tamuk
    """

    def disambiguate(self, word):
        matches = re.match(r'^pan([aiueo].*)$', word)
        if matches:
            return 't' + matches.group(1)


class DisambiguatorPrefixRuleSa1(object):
    """
    Perangkaian prefiks sa- dengan bentuk dasar bersuku dua  mengakibatkan  penambahan sebuah fonem nasal di antara  prefiks sa- dan bentuk dasarnya
    contoh :
    sangkurang   -> kurang
    """

    def disambiguate(self, word):
        matches = re.match(r'^(sang|san|sam)([^aiueo]*[aiueo]+[^aiueo]*[aiueo]+[^aiueo]*)$', word)
        if matches:
            return matches.group(2)



class DisambiguatorPrefixRuleSa2(object):
    """
    prefiks sa-dirangkaikan dengan bentuk dasar bersuku kata tunggal dengan fonem depan konsonan / n / ditambahkan di antara prefiks sa- dan bentuk dasarnya
    contoh :
    sange   -> sat
    """

    def disambiguate(self, word):
        matches = re.match(r'^sange([^aiueo]*[aiueo]+[^aiueo]*)$', word)
        if matches:
           return matches.group(1)


class DisambiguatorPrefixRuleSa3(object):
    """
    prefiks sa- bergabung dengan bentuk dasar bersuku dua yang fonem depannya adalah konsonan / b
    contoh :
    samalik   -> balik
    """

    def disambiguate(self, word):
        matches = re.match(r'^sam([aiueo]+[^aiueo]*[aiueo]+[^aiueo]*)$', word)
        if matches:
            return 'b' + matches.group(1)


class DisambiguatorPrefixRuleSa4(object):
    """
    prefiks sa- bergabung dengan bentuk dasar bersuku dua yang fonem depannya adalah konsonan / d
    contoh :
    sanadi   -> dadi
    """

    def disambiguate(self, word):
        matches = re.match(r'^san([aiueo]+[^aiueo]*[aiueo]+[^aiueo]*)$', word)
        if matches:
            return 'd' + matches.group(1)


class DisambiguatorPrefixRuleSa5(object):
    """
    prefiks sa- bergabung dengan bentuk dasar bersuku dua yang fonem depannya adalah konsonan / g
    contoh :
    sangila   -> Gila
    """

    def disambiguate(self, word):
        matches = re.match(r'^san([^aiueo]+[aiueo]+[^aiueo]+[aieuo]+)$', word)
        if matches:
            return  matches.group(1)


class DisambiguatorPrefixRuleTu1(object):
    """
    penghilangan fonem terhadap kata dasar
    contoh :
    Tutetak   -> tetak
    """

    def disambiguate(self, word):
        matches = re.match(r'^tu(.*)$', word)
        if matches:
            return  matches.group(1)


class DisambiguatorPrefixRuleYa1(object):
    """
    penghilangan fonem terhadap kata dasar
    contoh :
    Yabawa   -> bawa
    """

    def disambiguate(self, word):
        matches = re.match(r'^ya(.*)$', word)
        if matches:
            return  matches.group(1)



class DisambiguatorPrefixRuleMa1(object):
    """
    penghilangan fonem terhadap kata dasar
    contoh :
    malentak   -> lentak
    """

    def disambiguate(self, word):
        matches = re.match(r'^ma(.*)$', word)
        if matches:
            return  matches.group(1)

