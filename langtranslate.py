from translate import Translator

def text_translate():
	lang_1= input("Enter the Language you wish to translate from __:")
	lang_2= input("Enter the Language you wish to translate to __:")
	text= input("Enter the Text you wish to translate  __:")
	translator= Translator(lang_1, lang_2)
	translate_text= translator.translate(text)
	print(translate_text)

text_translate()
