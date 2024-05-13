"""
callback.py (Guides, Gradio Clients And Lite,
             Getting Started With The Python Client)
"""

from gradio_client import Client
import time


def print_result(x):
    print(f"The translated result is: {x}")


client = Client("abidlabs/en2fr")


job = client.submit("Hello", api_name="/predict", result_callbacks = [print_result])


# Do something else


time.sleep(5)
