# How to Create a Chatbot with Gradio

> Gradio Version 4.29.0

## Introduction

- This tutorial uses `gr.ChatInterface()`, which is a high-level abstraction that allows you to create your chatbot UI fast, often with a single line of code.

- We'll start with a couple of simple examples, and then show how to use `gr.ChatInterface()` with real language models from several popular APs and libraries, including `langchain`, `openai`, and Hugging Face.

- **Prerequisites**: please make sure you are using the **latest version** of Gradio:

    ```sh
    $ pip install --upgrade gradio
    ```

## Defining a chat function

- When working with `gr.ChatInterface()`, the first thing you should do is define your chat function.

- Your chat function should take two arguments: `message` and then `history`.

    - `message`: a `str` representing the user's input.

    - `history`

        - a `list` of `list` representing the conversations up until that point.

        - Each inner list consists of two `str` representing a pair: `[user input, bot response]`.

- Your function should return a single string response, which is the bot's response to the particular user input `message`.

- Your function can take into account the `history` of messages, as well as the current message.

## Example: a chatbot that responds yes or no

- We can plug a chat function into `gr.ChatInterface()` and call the `.launch()` method to create the web interface.

> ##### [random_chatbot.py](random_chatbot.py)

## Another example using the user's input and history

> ##### [argument_chatbot.py](argument_chatbot.py)

## Streaming chatbots

- In your chat function, you can use `yield` to generate a sequence of partial responses, each replacing the previous ones.

> ##### [streaming_chatbot.py](streaming_chatbot.py)

> ##### Tip
>
> - While the response is streaming, the "Submit" button turns into a "Stop" button that can be used to stop the generator function.
>
> - You can customize the appearance and behavior of the "Stop" button using the `stop_btn` parameter.

## Customizing your chatbot

- If you're familiar with Gradio's `Interface` class, the `gr.ChatInterface` includes many of the same arguments that you can use to customize the look and feel of your Chatbot.

- For example, you can:

    - add a title and description above your chatbot using `title` and `description` arguments.

    - add a theme or custom css using `theme` and `css` arguments respectively.

    - add `examples` and even enable `cache_examples`, which make it easier for users to try it out.

    - You can change the text or disable each of the buttons that appear in the chatbot interface: `submit_btn`, `retry_btn`, `undo_btn`, `clear_btn`.

- If you want to customize the `gr.Chatbot` or `gr.Textbox` that compose the `ChatInterface`, then you can pass in your own chatbot or textbox as well.

> ##### [custom_chatbot.py](custom_chatbot.py)

- In particular, if you'd like to add a "placeholder" for your caht interface, which appears before the user has started chatting, you can do so using the `placeholder` argument of `gr.Chatbot`, which accepts Markdown or HTML.

- The placeholder appears vertically and horizontally centered in the chatbot.

## Additional Inputs

- You may want to add additional parameters to your chatbot and expose them to your users through the Chatbot UI.

- The `ChatInterface` class supports an `additional_inputs` parameter which can be used to add additional input components.

- The `additional_inputs` parameters accepts a component or a list of components.

- You can pass the component instances directly, or use their string shortcuts.

- If you pass in component instances, and they have *not* already been rendered, then the components will appear underneath the chatbot within a `gr.Accordion()`.

- You can set the label of this accordion using the `additional_inputs_accordion_name` parameter.

> ##### [additional_inputs_chatbot.py](additional_inputs_chatbot.py)

- If the components you pass into the `additional_inputs` have already been rendered in a parent `gr.Blocks()`, then they will *not* be re-rendered in the accordion.


> ##### [render_additional_inputs_chatbot.py](render_additional_inputs_chatbot.py)

- If you need to create something even more custom, then its best to construct the chatbot UI using the low-level `gr.Blocks()` API.

    - See Creating A Custom Chatbot With Blocks.

## Using your chatbot via an API

- Once you've built your Gradio chatbot and are hosting it somewhere, then you can query it with a simple API at the `/chat` endpoint.

- The endpoint just expects the user's message, and will return the response, internally keeping track of the messages sent so far.

- To use the endpoint, you should use either the Gradio Python Client or the Gradio JS client.
