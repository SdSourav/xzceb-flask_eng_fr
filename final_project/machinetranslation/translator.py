"""
This module provides functions for translating text between English and French using
IBM Watson Language Translator API.

Functions:

english_to_french: Translates English text to French text.
french_to_english: Translates French text to English text.
"""
import os

from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']
AUTHENTICATOR = IAMAuthenticator(API_KEY)

LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR,
)
LANGUAGE_TRANSLATOR.set_service_url(URL)


def english_to_french(english_text):
    """
    Translates English text to French text using the IBM Watson Language Translator API.

    Parameters:
    - english_text (str): The English text to be translated.

    Returns:
    - french_text (str): The translated French text. If the input English text is None,
      returns None.
    """
    if english_text is None:
        return None

    french_text = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """
    Translates a given text from French to English using IBM Watson Language Translator.

    Args:
        french_text (str): The text to be translated from French to English.

    Returns:
        str: The translated text in English.

    Raises:
        None.
    """
    if french_text is None:
        return None

    english_text = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()['translations'][0]['translation']
    return english_text
