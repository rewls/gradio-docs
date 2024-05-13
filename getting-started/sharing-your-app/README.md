# Sharing Your App

## Sharing Demos

- Gradio demos can be easily shared publicly by setting `share = True` in the `launch()` method.

- Although the link is served through the Gradio Share Servers, these servers are only a proxy for your local server, and do not store any data sent through your app.

- Share links expire after 72 hours.

- It is also possible to set up your own Share Server on your own cloud server to overcome this restriction.

    - See https://github.com/huggingface/frp/.

> ##### Tip
>
> - Make sure not to expose any sensitive information through the functions you write, or allow any critical changes to occur on your device.
>
> - Or you can add authentication to your Gradio app as discussed below.

- Note that by default, `share = False`, which means that your server is only running locally.

- This is the default, except in Google Colab notebooks, where share links are automatically created.

- As an alternative to using share links, you can use SSH port-forwarding to share your local server with specific users.

    - See https://www.ssh.com/academy/ssh/tunneling-example.

## API Page

- You can use almost any Gradio app as an API!

- In the footer of a Gradio app, you'll see a "Use via AP" link.

- This is a page that lists the endpoints that can be used to query the Gradio app, via our supported clients: either the Python client, or the JavaScript client.

- For each endpoint, Gradio automatically generates the parameters and their types.

- The endpoints are automatically created when you launch a Gradio `Interface`.

- If you are using Gradio `Blocks`, you can also set up a Gradio API page, though we recommend that you explicitly name each event listener, such as

    ```python
    btn.click(add, [num1, num2], output, api_name = "addition")
    ```

- This will add and document the endpoint `/api/addition/` to the automatically generated AP page.

- Otherwise, your API endpoints will appear as "unnamed" endpoints.

## Accessing the Network Request Directly

- When a user makes a prediction to your app, you may need the underlying network request, in order to get the request headers (e.g. for advanced authentication), log the client's IP address, getting the query parameters, or for other reasons.

- Graadio supports this in a similar manner to FastAPI: simply add a function parameter whose type hint is `gr.Request` and Gradio will pass in the network request as that parameter.

> ##### [echo.py](echo.py)

- If your function is called directly instead of through the UI (this happens, for example, when examples are cached, or when the Gradio app is called via API), then `request` will be `None`.

- You should handle this case explicitly to ensure that your app does not throw any errors.

- That is why we have the explicit check `if request`.

## Authentication

### Password-protected app

- With the `auth =` keyword argument in the `launch()` method, you can provide a tuple with a username and password, or a list of acceptable username/password tuples. 

- For more complex authentication handling, you can even pass a function that takes a username and password as arguments, and returns `True` to allow access, `False` otherwise.

- If you have multiple users, you may wish to customize the content that is shown depending on the user that is logged in.

- You can retrieve the logged in user by accessing the network request directly as discussed above, and then reading the `.username` attribute of the request.

> ##### [update_message.py](update_message.py)

- For authentication to work properly, third party cookies must be enabled in your browser.

- This is not the case by default for Safari or for Chrome Incognito Mode.

- If users visit the `/logout` page of your Gradio app, they will automatically be logged out and session cookies deleted.

- Gradio's built-in authentication does not offer robust security features for applications that require stringent access controls (e.g. multi-factor authentication, rate limiting, or automatic lockout policies).

## Security and File Access

- Sharing your Gradio app with others **exposes** certain files on the host machine to users of your Gradio app.

- In particular, Gradio apps ALLOW users to access to four kinds of files:

    - Temporary files created by Gradio.

        - These are files that created by Gradio as part of running your prediction function.

        - You can customize the location of temporary cache files created by Gradio by setting the environment variable `GRADIO_TEMP_DIR` to an absolutee path.

        - You can delete the files created by your app when it shuts down with the `delete_cache` parameter of `gradio.Blocks`, `gradio.Interface`, and `gradio.ChatInterface`.

        - This parameter is a tuple of integers of the form `[frequency, age]` where `frequency` is how often to delete files and `age` is the time in seconds since the file was last modified.

    - Cache examples created by Gradio.

        - These are files that are created by Gradio as part of caching examples for faster runtimes, if you set `cache_examples = True` or `cache_examples = "lazy"` in `gr.Interface()`, `gr.ChatInterface()` or in `gr.Examples()`.

        - By default, these files are saved in the `gradio_cache_examples/` subdirectory within your app's working directory.

        - You can customize the location of cached example files created by Gradio by setting the environment variable `GRADIO_EXAMPLES_CACHE` to an absolute path or a path relative to your working directory.

    - Files that you explicitly allow via the `allowed_paths` parameter in `launch()`.

        - This parameter allows you to pass in a list of additional directories or exact filepaths you'd like to allow users to have access to.

        - By default, this parameter is an empty list.

    - Static files that you explicitly set via the `gr.set_static_paths` function.

        - This parameter allows you to pass in a list of directories or filenames that will be considered static.

        - This means that they will not be copied to the cache and will be served directly from your computer

        - This can help save disk space and reduce the time your app takes to launch but be mindful of possible security implications.

- Gradio DOES NOT ALLOW access to:

    - Files that you explicitly block via the `blocked_paths` parameter in `launch()`.

        - You can pass in a list of additional directories or exact filepaths to the `blocked_paths` parameter in `launch()`.

        - This parameter takes precedence over the files that Gradio exposes by default or by the `allowed_paths`.

    - Any other paths on the host machine.

- You can set a maximum file size for uploads this with the `max_file_size` parameter of `.launch`.

> ##### [upload.py](upload.py)
