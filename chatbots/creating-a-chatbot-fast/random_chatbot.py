"""
random_chatbot.py (Guides, Chatbots, Creating A Chatbot Fast)
Write a chat function that responds Yes or No randomly
"""

import random


def random_response(message, history):
    return random.choice(["Yes", "No"])


import gradio as gr


gr.ChatInterface(random_response).launch()
