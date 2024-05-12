"""
trim_words_blocks.py (Guide, Getting Started, Key Features)
"""

import time
import gradio as gr


def trim_words(words, lens):
    trimmed_words = []
    time.sleep(5)
    for w, l in zip(words, lens):
        trimmed_words.append(w[:int(l)])
    print(trimmed_words)
    return [trimmed_words]


with gr.Blocks() as demo:
    with gr.Row():
        word = gr.Textbox(label = "word")
        leng = gr.Number(label = "leng")
        output = gr.Textbox(label = "Output")
    with gr.Row():
        run = gr.Button()


    event = run.click(trim_words, [word, leng], output, batch = True,
                      max_batch_size = 16)


demo.launch()
