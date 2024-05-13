"""
update_message.py (Guides, Getting Started, Sharing Your App)
"""

import gradio as gr


def update_message(request: gr.Request):
    return f"Welcome, {request.username}"


with gr.Blocks() as demo:
    m = gr.Markdown()
    logout_button = gr.Button("Logout", link = "/logout")
    demo.load(update_message, None, m)


demo.launch(auth = [("Abubakar", "Abubakar"), ("Ali", "Ali")])
