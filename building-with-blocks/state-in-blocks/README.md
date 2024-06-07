# State in Blocks

## Global State

- Global state in Blocks works the same as in Interface.

- Any variable created outside a function call is a reference shared between all users..

## Session State

- Gradio supports session state, where data persists across multiple submits within a page session, in Blocks apps as well.

- To reiterate, session data is *not* shared between different users of your model.

- To store data ina session state, you need to do three things:

    1. Create a `gr.State()` object.

        - If there is a default value to this stateful object, pass that into the constructor.

    2. In the event listener, put the `State` object as an input and output.

    3. In the event listener function, add the variable to the input parameters and the return value.

> ##### [hangman.py](hangman.py)
