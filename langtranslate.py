import gradio as gr
from translate import Translator

def transLate(English_text, Choose_language):
	translator= Translator(from_lang="english", to_lang=Choose_language)
	return translator.translate(English_text)

lang= gr.Interface(fn=transLate, inputs=["text", "text"], outputs="text")

lang.launch()