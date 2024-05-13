"""
outputs.py (Guides, Gradio Clients And Lite,
           Getting Started With The Python Client)
"""

from gradio_client import Client
import time


client = Client(src = "gradio/count_generator")
job = client.submit(3, api_name = "/count")
while not job.done():
    time.sleep(0.1)
print(job.outputs())
