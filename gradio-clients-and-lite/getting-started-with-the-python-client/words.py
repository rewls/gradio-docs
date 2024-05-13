"""
words.py (Guides, Gradio Clients And Lite,
          Getting Started With The Python Client)
Maintain a list of words that a user has submitted in a gr.State component
"""

import gradio as gr

def count(word, list_of_words):
    return list_of_words.count(word), list_of_words + [word]

with gr.Blocks() as demo:
    words = gr.State([])
    textbox = gr.Textbox()
    number = gr.Number()
    textbox.submit(count, inputs = [textbox, words], outputs = [number, words])


demo.launch()
