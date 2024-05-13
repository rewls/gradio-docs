"""
status.py (Guides, Gradio Clients And Lite,
           Getting Started With The Python Client)
"""

from gradio_client import Client

client = Client(src = "gradio/calculator")
job = client.submit(5, "add", 4, api_name = "/predict")
print(job.status())
