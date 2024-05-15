# Chatbot

> Gradio 4.31.0

## Description

- Supports a subset of Markdown including bold, italics, code, tables.

- Also supports audio/video/image files, which are displayed in the Chatbot, and other kinds of files which are displayed as links

## Behavior

- As input component

    - Passes the messages in the chatbot as a `list[list[str | None | tuple]]`.

    - The inner list has 2 elements: the user message and the response message.

    - Each message can be (1) a string in valid Markdown, (2) a tuple if there are displayed files: (a filepath or URL to a file, [optional string alt text]), or (3) None, if there is no message displayed.

    - Your function should accept one of these types:

        ```python
        def predict(value: list[list[str | tuple[str] | tuple[str, str] | None]] | None)
        ...
        ```

- As output component

    - expects a `list[list[str | None | tuple]]`.

    - The inner list should have 2 elements: the user message and the response message.

    - The individual messags can be (1) strings in valid Markdown, (2) tuples if sending files: (a filepath or URL to a file, [optional string alt text]) -- if the file is image/video/audio, it is displayed in the Chatbot, or (3) None, in which case the message is not displayed.

    - Your function should return one of these types:

        ```python
        def predict(...) -> list[list[str | tuple[str] | tuple[str, str] | None] | tuple] | None
            ...
            return value
        ```

## Initialization

### `value`

- list[list[str | tuple[str] | tuple[str | Path, str] | None]] | Callable | None

- default: None

- Default value to show in chatbot.

- If callable, the function will be called whenever the app loads to set the initial value of the component.
