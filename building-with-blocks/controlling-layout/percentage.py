"""
percentage.py (Guides, Building With Blocks, Controlling Layout)
"""

import gradio as gr


css = """
.container {
    height: 100vh;
}
"""


with gr.Blocks(css = css) as demo:
    with gr.Column(elem_classes = ["container"]):
        name = gr.Chatbot(value = [["1", "2"]], height = "70%")


demo.launch()
