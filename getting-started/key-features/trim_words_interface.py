"""
trim_words_interface.py (Guide, Getting Started, Key Features)
"""

import time
import gradio as gr


def trim_words(words, lens):
    trimmed_words = []
    time.sleep(5)
    for w, l in zip(words, lens):
        trimmed_words.append(w[:int(l)])
    return [trimmed_words]


demo = gr.Interface(fn = trim_words, inputs = ["textbox", "number"],
                    outputs = ["textbox"], batch = True, max_batch_size = 16)


demo.launch()
