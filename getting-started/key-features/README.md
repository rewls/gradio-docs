# Key Features

> Gradio Version 4.31.0

- This guide is intended to be a high-level overview of various things that you should be aware of as you build your demo.

## Components

- Gradio includes more than 30 pre-built components that can be used as inputs or outputs in your demo with a single line of code.

- These components correspond to common data types in machine learning and data science, e.g. the `gr.Image` component is designed to handle input or output images, the `gr.Label` component displays classification labels and probabilities, the `gr.Plot` component displays various kinds of plots, and so on.

- Each component includes various constructor attributes that control the properties of the component.

### Static and Interactive Components

- Every component has a *static* version that is designed to *display* data, and most components also have an *interactive* version designed to let users input or modify the data.

- Typically, Gradio automatically figures out whether the component should be static or interactive based on whether it is being used as an input or output.

- However, you can set this manually using the `interactive` argument that every component supports.

### Preprocessing and Postprocessing

- When a component is used as an input, Gradio automatically handles the *preprocessing* needed to convert the data from a type sent by the user's browser to a form that can be accepted by your function.

- Similarly, when a component is used as an output, Gradio automatically handles the *postprocessing* needed to convert the data from what is returned by your function to a form that can be displayed in the user's browser.

- You can control the *preprocessing* using the component's parameters when constructing the component.

- Gradio automatically recognizes the format of the returned data and postprocesses it appropriately into a format that can be displayed by the browser.

- Take a look at the Gradio Documentation to see all the parameters for each Gradio component.

## Streaming outputs

- You can supply a `generator` function into Gradio instead of a regular function.

- Instead of a single `return` value, a function should `yield` a series of values instead.

- Usually the `yield` statement is put in some kind of loop.

- Here's an example of an generator that simply counts up to a given number:

    ```python
    def my_generator(x):
        for i in range(x):
            yield i
    ```

- For example, here's a (fake) image generation model that generates noise for several steps before outputting an image using the `gr.Interface` class:

    > ##### [fake_diffusion.py](fake_diffusion.py)

- You supply a generator into Gradio the same way as you would a regular function.

## Streaming inputs

- Similarly, Gradio can handle streaming inputs, e.g. a live audio stream that can gets transcribed to text in real time, or an image generation model that reruns every time a user types a letter in a textbox.

- See Reactive Interfaces

## Alert modals

- To raise alerts to the user, raise a `gr.Error("custom message")` to display an error message.

- You can also issue `gr.Warning("message")` and `gr.Info("message")` by having them as standalone lines in your function, which will immediately display modals while continuing the execution of your function.

- Queueing needs to be enabled for this to work.

- Note below how the `gr.Error` has to be raised, while the `gr.Warning` and `gr.Info` are single lines.

    ```python
    def start_process(name):
        gr.Info("Starting process")
        if name is None:
            gr.Warning("Name is empty")
        ...
        if success == False:
            raise gr.Error("Process failed")
    ```

## Styling 

- You can choose from a variety of themes, or create your own.

- To do so, pass the `theme = ` kwarg to the `Interface` constructor.

- Gradio comes with a set of prebuilt themes which you can load from `gr.themes.*`.

- You can extend these themes or create your own themes from scratch - see the Theming Guide.

- For additional styling ability, you can pass any CSS (as well as custom JavaScript) to your Gradio application.

    - See Custom CSS and JS.

## Progress bars

- Gradio supports the ability to create custom Progress Bars so that you have customizability and control over the progress update that you show to the user.

- Simply add an argument to your method that has a default value of a `gr.Progress` instance.

- Then you can update the progress levels by calling this instance directly with a float between 0 and 1, or using the `tqdm()` method of the `Progress` instance to track progress over an iterable.

> ##### [slowly_reverse.py](slowly_reverse.py)

- If you use the `tqdm` library, your can even report progress updates automatically from any `tqdm.tqdm` that already exists within your function by setting the default argument as `gr.Progress(track_tqdm = True)`!

## Batch functions

- Batch functions are just functions which take in a list of inputs and return a list of predictions.

- The advantage of using batched functions is that if you enable queuing, the Gradio server can automatically *batch* incoming requests and process them in parallel, potentially speeding up your demo.

> ##### [trim_words_interface.py](trim_words_interface.py)

> ##### [trim_words_blocks.py](trim_words_blocks.py)
