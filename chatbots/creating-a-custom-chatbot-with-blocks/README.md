# How to Create a Custom Chatbot with Gradio Blocks

> Gradio Version 4.31.0

## Introduction

- This tutorial will show how to make chatbot UIs from scratch with Gradio's low-level Blocks API.

- This will give you full control over your Chatbot UI.

- You'll start by first creating a simple chatbot to display text, a second one to stream text responses, and finally a chatbot that can handle media files as well.

- **Prerequisite**

    - We'll be using the `gradio.Blocks` class to build our Chatbot demo.

        - See Blcoks and Event Listeners.

    - Please make sure you are using the **latest version** of Gradio:

        ```sh
        $ pip install --upgrade gradio
        ```

## A Simple Chatbot Demo

> ##### [random_chatbot.py](random_chatbot.py)

- There are three Gradio components here:

    - A `Chatbot`, whose value stores the entire history of the conversation, as a list of response pairs between the user and bot.

    - A `Textbox` where the user can type their message, and then hit enter/submit to trigger the chatbot response

    - A `ClearButton` button to clear the Textbox and entire Chatbot history

## Add Streaming to your Chatbot

- We can stream responses so the user doesn't have to wait as long for a message to be generated.

- We can have the user message appear immediately in the chat history, while the chatbot's response is being generated.

> ##### [streaming.py](streaming.py)

- You'll notice that when a user submits their message, we now *chain* three events with `.then()`:

    1. The first method `user()` makes the input field non interactive so that the user can't send another message while the chatbot is responding.

        - Because we want this to happen instantly, we set `queue = False`, which sould skip any queue had it been enabled.

    2. The second method, `bot()`.

    3. The third method makes the input field interactive again so that users can send another message to the bot.

- We enable queueing by running `demo.queue()`, which is required for streaming intermediate outputs.

## Liking / Disliking Chat Messages

- You can add the ability for users to like or dislike messages.

- To add this functionality to your Chatbot, simply attach a `.like()` event to your Chatbot.

- A chatbot that has `.like()` event will automatically feature a thumbs-up icon and a thumbs-down icon next to every bot message.

- The `.like()` method requires you to pass in a function that is called when a user clicks on these icons.

- In your function, you should have an argument whose type is `gr.LikeData`.

- Gradio will automatically supply the parameter to this argument with an object that contains information about the liked or disliked message..

> ##### [like.py](like.py)

## Adding Markdown, Images, Audio, or Videos

- The `gr.Chatbot` component supports a subset of markdown including bold, italics, and code.

- It can handle media files, such as images, audio, and video.

- you can use the `MultimodalTextbox` component to easily upload all types of media files to your chatbot.

- To pass in a media file, we must pass in the file as a tuple of two strings, like this :`(filepath, alt_text)`.

- The `alt_text` is optional, so you can also just pass in a tuple with a single element `(filepath,)`.

> ##### [multimodal.py](multimodal.py)
