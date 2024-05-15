"""
like.py (Guides, Chatbots, Creating A Custom chatbot With Blocks)
"""

import gradio as gr
import os
import time


def add_message(history, message):
    for x in message["files"]:
        history.append(((x,), None))
    if message["text"] is not None:
        history.append((message["text"], None))
    return history, gr.MultimodalTextbox(value = None, interactive = False)


def bot(history):
    response = "**That's cool!**"
    history[-1][1] = response
    return history


with gr.Blocks() as demo:
    chatbot = gr.Chatbot([], elem_id = "chatbot", bubble_full_width = False)
    chat_input = gr.MultimodalTextbox(
            interactive = True, file_types = ["image"],
            placeholder = "Enter message or upload file...", show_label = False)
    chat_msg = chat_input.submit(add_message, [chatbot, chat_input], [chatbot, chat_input])
    bot_msg = chat_msg.then(bot, chatbot, chatbot, api_name="bot_response")
    bot_msg.then(lambda: gr.MultimodalTextbox(interactive = True), None, [chat_input])


demo.launch()
