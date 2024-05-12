# Quickstart

- Gradio is an open-source Python package that allows you to quickly **build** a demo or web application for your machine learning model, AP, or any arbitrary Python function.

- You can then **share** a link to your demo or web application in just a few seconds using Gradio's built-in sharing features.

- *No JavaScript, CSS, or web hosting experience needed!*

## Installation

- **Prerequisite**: Gradio requires Python 3.8 or higher

- We recommend installing Gradio using `pip`, which is included by default in Python.

    ```sh
    $ pip install gradio
    ```

> ##### Tip
>
> - It is best to install Gradio in a virtual environment.
>
> - See Installing Gradio In A Virtual Environment.

## Building Your Fist Demo

> ##### [first_demo.py](first_demo.py)

> ##### Tip
>
> - We shorten the imported name for `gradio` to `gr` for better readability of code.
>
> - This is a widely adopted convention that you should follow so that anyone working with your code can easily understand it.

> ##### Tip
>
> - When developing locally, you can run your Gradio app in hot reload mode, which automatically reloads the Gradio app whenever you make changes to the file.
>
> To do this, simply type in `gradio` before the name of the file instead of `python`.
>
> - See Developing Faster With Reload Mode.

### Understanding the `Interface` Class

- The `Interface` class is designed to create demos for machine learning models which accept one or more inputs, and return one or more outputs

- The `Interface` class has three core arguments:

    - `fn`: the function to wrap a user interface (UI) around

    - `inputs`

        - the Gradio component(s) to use for the input.

        - The number of components should match the number of arguments in your function.

    - `outputs`

        - the Gradio component(s) to use for the output.

        - The number of components should match the number of return values from your function.

- The `fn` argument

- As we'll see, Gradio includes more than 30 built-in components (such as the `gr.Textbox()`, `gr.Image()`, and `gr.HTML()` components) that are designed for machine learning applications.

> ##### Tip
>
> - For the `inputs` and `outputs` arguments, you can pass in the name of these components as a string or an instance of the class.

- See The `interface` class.

## Sharing Your Demo

- Simply set `share = True` in `launch()`, and a publicly accessible URL will be created for your demo.

- See Sharing your App.

## An Overview of Gradio

- What else does Gradio do?

### Chatbots with `gr.ChatInterface`

- Gradio includes another high-level class, `gr.ChatInterface`, which is specifically designed to create Chatbot UIs.

- See Creating A Chatbot Fast.

### Custom Demos with `gr.Blocks`

- Gradio also offers a low-level approach for designing web apps with more flexible layouts and data flows with the `gr.Blocks` class.

- Blocks allows you to do things like control where components appear on the page, handle complex data flows, and update properties/visibility of components based on user interaction.

- See Blocks And Event Listners.

### The Gradio Python & JavaScript Ecosystem

- Its an entire ecosystem of Python and JavaScript libraries that let build machine learning applications, or query them programmatically, in Python or JavaScript.

- See Gradio Python Client (`gradio_client`): query any Gradio app programmatically in Python.

## What's Next?

- Keep learning about Gradio sequentially using the Gradio Guides.
