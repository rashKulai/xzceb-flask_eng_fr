"""This is a translator module"""
from deep_translator import MyMemoryTranslator
def english_to_french(english_text):
    """This class does english to french translation"""
    #write the code here
    frenchtext= MyMemoryTranslator(source="english",target='fr-CA').translate(text=english_text)
    return frenchtext


def french_to_english(french_text):
    """This class does french to french english"""
    #write the code here
    englishtext= MyMemoryTranslator(source="fr-CA",target='english').translate(text=french_text)
    return englishtext
