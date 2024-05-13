"""
job.py (Guides, Gradio Clients And Lite, Getting Started With The Python Client)
"""

from gradio_client import Client


client = Client(space = "abidlabs/en2fr")
job = client.submit("Hello", api_name = "/predict")


# Do domething else


print(job.result())
