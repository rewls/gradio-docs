"""
iterable.py (Guides, Gradio Clients And Lite,
             Getting Started With The Python Client)
"""

from gradio_client import Client


client = Client(src="gradio/count_generator")
job = client.submit(3, api_name = "/count")


for o in job:
    print(o)
