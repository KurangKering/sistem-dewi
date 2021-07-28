from django.test import TestCase, Client
from library.algorithms.stemming.Stemmer.StemmerFactory import StemmerFactory
from library.algorithms.stemming.Dictionary.ModelDatabase import ModelDatabase
from library.algorithms.stemming.Dictionary.FileDatabase import FileDatabase

# Create your tests here.
#
#

class StemmerTests(TestCase):
    def test_stemmer(self):
        factory_stemmer = StemmerFactory()
        kamusDatabase = FileDatabase()
        stemmer = factory_stemmer.create_stemmer(False, kamusDatabase)
        result = stemmer.stem('mikir')
        return self.assertEqual('pikir', result)

