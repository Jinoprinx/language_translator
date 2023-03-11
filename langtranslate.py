from translate import Translator

# def langTranslate(text):
# 	lang_1= input("Enter the Language you wish to translate from __:")
# 	lang_2= input("Enter the Language you wish to translate to __:")
# 	text= input("Enter the Text you wish to translate  __:")
# 	translator= Translator(lang_1, lang_2)
# 	translated_text= translator.translate(text)
# 	print(translated_text)
# langTranslate("hello how are you")


#On a second thought
def transLate():
	lang_1= input("enter Language you wish to translate from__:")
	lang_2= input("enter Language you wish to translate to__:")
	text= input("enter the text you wish to translate __:")
	translator= Translator(from_lang=lang_1, to_lang=lang_2)
	print(translator.translate(text))

transLate()