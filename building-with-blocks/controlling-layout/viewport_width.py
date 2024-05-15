"""
viewport_width.py (Guides, Building With Blocks, Controlling Layout)
Use of viewport width (vw)
"""

import gradio as gr


with gr.Blocks() as demo:
    im = gr.ImageEditor(width = "50vw")


demo.launch()
