"""
change.py (Guides, Building With Block, Blocks And Event Listeners)
"""

import gradio as gr

def welcome(name):
    return f"Welcome to Gradio, {name}!"

with gr.Blocks() as demo:
    gr.Markdown(
            """
            # Hello World!
            Start typing below to see the output.
            """)
    inpt = gr.Textbox(placeholder = "What is your name?")
    out = gr.Textbox()
    inp.change(welcome, inpt, out)


demo.launch()
