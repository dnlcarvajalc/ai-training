from transformers import pipeline
from word2number import w2n

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")


def text_to_number(text):
    translated_text = translator(text)[0]["translation_text"]
    try:
        return w2n.word_to_num(translated_text)
    except ValueError:
        return "Número no reconocido"


print(text_to_number("veintiuno"))
print(text_to_number("quinientos treinta y siete"))
print(text_to_number("mil doscientos cuarenta y cinco"))
