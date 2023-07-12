from machinetranslation import translator
import unittest

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(translator.english_to_french('Hello'),'Hello')

class TestFrenchToEnglish(unittest.TestCase):
     def test2(self):
        self.assertEqual(translator.french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(translator.frenchtoenglish('Bonjour'),'Bonjour')

unittest.main()