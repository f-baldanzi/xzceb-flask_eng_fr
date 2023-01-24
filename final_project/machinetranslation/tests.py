import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_null_english_to_french(self):
        with self.assertRaises(ValueError):
            english_to_french(None)
    
    def test_word_hello_to_bonjour(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "Bon journée")

class TestFrenchToEnglish(unittest.TestCase):

    def test_null_french_to_english(self):
        with self.assertRaises(ValueError):
            english_to_french(None)
    
    def test_word_bonjour_to_hello(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bon journée"), "Hello")
