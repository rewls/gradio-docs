# Getting Started with the Gradio Python client

- The Gradio Python client makes it very easy to use any Gradio app as an APi.

> ##### [transcribe.py](transcribe.py)

- Although the Client is mostly used with apps hosted on Hugging Face Spaces, your app can be hosted anywhere.

- Prerequisites

    - It is helpful to have general familiarity with Gradio's concepts of input and output components.

## Installation

- If you already have a recent version of `gradio`, then the `gradio_client` is included as a dependency.

- The lightweight `gradio_client` package can be installed from pip and is tested to with Python versions 3.9 or higher:

    ```python
    $ pip install --upgrade gradio_client
    ```

## Connecting a general Gradio app

- Just provide the full URL instead, including the "http://" or "https://".

## Inspecting the API endpoints

- Once you have connected to a Graadio app, you can view the APIs that are available to you by calling the `Client.view_api()` method.

> ##### [transcribe_view_api.py](transcribe_view_api.py)

- We should call the `.predict()` method, providing a parameter `input_audio` of type `str`, which is a `filepath or URL`.

- We should also provide the `api_name = '/predict'` argument to the `predict()` method.

- This isn't necessary if a Gradio app has only 1 named endpoint.

## The "View AP" Page

- You can click on the "Use via API" link in the footer of the Gradio app, which shows us the same information, along with example usage.

- The View API page also includes an "API Recorder" thatlets you interact with the Gradio UI normally and converts your interactions into the corresponding code to run with the Python Client.

## Making a prediction

- The simplest way to make a prediction is simply to call the `.predict()` function with the appropriate arguments.

- It is recommended to provide key-word arguments instead of positional arguments

- This allows you to take advantage of default arguments.

- The default value is the initial value of the corresponding Gradio component.

- If the component does not have an initial value, but if the corresponding argument in the predict function has a default value of `None`, then that parameter is also optional in the client.

- For providing files or URLs as inputs, you should pass in the file path or URL to the file enclosed within `gradio_client.file()`.

- This takes care of uploading the file to the Gradio server and ensures that the file is preprocessed correctly.

## Running jobs asynchronously

- We should note that `.predict()` is a *blocking* operation as it waits for the operation to complete before returning the prediction.

- In many cases, you may be better off letting the job run in the background until you need the results of the prediction.

- You can do this by creating a `Job` instance using the `.submit()` method, and then later calling `.result()` on the job to get the result.

> ##### [job.py](job.py)

## Adding callbacks

- Alternatively, one can add one or more callbacks to perform actions after the job has completed running.

> ##### [callback.py](callback.py)

## Status

- The `Job` object also allows you to get the status of the running job by calling the `.status()` method.

- This returns a `StatusUpdate` object with the following attributes:

    - `code`

        - the status code, one of a set of defined strings representing the status.

        - See the `utils.Status` class.

    - `rank`: the current position of this job in the queue

    - `success`: a boolean representing whether the job competed successfully

    - `time`: the time that the status was generated

> ##### [job.py](job.py)
    
- The `Job` class also has a `.done()` instance method which returns a boolean indicating whether the job has competed.

## Cancelling Jobs

- The `Job` class also has a `.cancel()` instance method that cancels jobs that have been queued but not started.

## Generator Endpoints

- Some Gradio API endpoints do not return a single value, rather they return a series of values.

- You can get the series of values that have been returned at any time from such a generator endpoint by running `job.outputs()`.

> ##### [outputs.py](outputs.py)

- Running `job.result()` on a generator endpoint only gives you the *first* value returned by the endpoint.

- The `Job` object is also iterable, which means you can use it to display the results of a generator function as they are returned from the endpoint.

> ##### [iterable.py](iterable.py)

- You can also cancel jobs that have iterative outputs, in which case the job will finish as soon as the current iteration finishes running.

## Demos with Session State

- Gradio demos can include session state, which provides a way for demos to persist information from user interactions within a page session.

    - See State In Blocks.

> ##### [words.py](words.py)

- The Python client handles state automatically for you - as you make a series of requests, the returned state from one request is stored internally and automatically supplied for the subsequent request.

- If you'd like to reset the state, you can do that by calling `Client.reset_session()`.
