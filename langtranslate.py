from translate import Translator


#lang_1= input("Enter the Language you wish to translate from __:")
#lang_2= input("Enter the Language you wish to translate to __:")
#text= input("Enter the Text you wish to translate  __:")
#translator= Translator(lang_1, lang_2)
#translated_text= translator.translate(text)
#print(translated_text)

#On a second thought
def transLate(lang_1, lang_2, text):
	translator= Translator(lang_1, lang_2)
	translated_text= translator.translate(text)
	print(translated_text)

transLate("english", "spanish", "hello how are you")