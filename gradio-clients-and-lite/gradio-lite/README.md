# Gradio-Lite: Serverless Gradio Running Entirely in Your Browser

> Gradio Version 4.31.0

- Traditionally, Gradio applications have relied on server-side infrastructur to run.

- Enter Gradio-lite (`@gradio/lite`): a library that leverages Pyodide to bring Gradio directly to your browser.

## What is `@gradio/lite`?

- `@gradio/lite` is a JavaScript library that enables you to run Gradio applications directly within your web browser.

- It achieves this by utilizing Pyodide, a Python runtime for WebAssembly, which allows Python code to be executed in the browser environment.

- With `@gradio/lite`, you can write regular Python code for your Gradio applications, and they will run seamlessly in the browser without the need for serverside infrastructure.

## Getting Started

- Let's build a "Hello World" Gradio app in `@gradio/lite`

### 1. Import JS and CSS

- Importing the JavaScript and CSS corresponding to the `@gradio/lite` package by using the following code:

```html
<html>
	<head>
		<script type = "module" crossorigin
		src = "https://cdn.jsdelivr.net/npm/@gradio/lite/dist/lite.js">
		</script>
		<link rel = "stylesheet"
		      href = "https://cdn.jsdelivr.net/npm/@gradio/lite/dist/lite.css"/>
	</head>
</html>
```

### 2. Create the `<gradio-lite>` tags

- Somewhere in the body of your HTML page, create opening and closing `<gradio-lite>` tags.

- You can add the `theme` attribute to the `<gradio-lite>` tag to force the theme to be dark or light.

    - by default, it respects the system theme.

### 3. Write your Gradio app inside of the tags

- Now write your Gradio app as you sould normally, in Python.

- Keep in mind that since this is Python, whitespace and indentations matter.

- You should now be able to open your HTML page in the browser and see the Gradio app rendered.

- Note on debugging

    - To see any errors in your Gradio-lite application, open the inspector in your web browser.

## More Examples: Adding Additional Files and Requirements

### Multiple Files

- Use `<gradio-file>` tag.

- You can have as many `<gradio-file>` tags as you want, but each one needs to have a `name` attribute and the entry point to your Gradio app should have the `entrypoint` attribute.

> ##### [multiple-files.html](multiple-files.html)

### Additional Requirements

- If your Gradio app has additional requirements, it is usually possible to install them in the browser using micropip.

    - See https://pyodide.org/en/stable/usage/loading-packages.html#loading-packages.

- We've created a wrapper to make this particularly convenient: simply list your requirements in the same syntax as a `requirements.txt` and enclose them with `<gradio-requirements>` tags.

### SharedWorker mode

- By default, Gradio-Lite executes Python code in a Web Worker with Pyodide runtime, and each Gradio-Lite app.

- It has some benefits such as environment isolation.

- However, when there are many Gradio-Lite apps in the same page, it may cause performance issues such as high memory usage because each app has its own worker and Pyodide runtime.

- In such cases, you can use the **SharedWorker mode** to share a single Pyodide runtime in a SharedWorker among multiple Gradio-Lite apps.

- To enable the SharedWorker mode, set the `shared-worker` attribute to the `<gradio-lite>` tag.

- When using the SharedWorker mode, you should be aware of the following point:

    - The apps share the same Python environment, which means that they can access the same modules and objects.

    - The file system is shared among the apps, while each app's files are mounted in each home directory, so each app can access the files of other apps.

### Code and Demo Playground

- If you'd like to see the code side-by-side with the demo just pass in the `playground` attribute to the gradio-lite element.

- This will create an interactive playground that allows you to change the code and update the demo.

- If you're using playground, you can also set layout to either 'vertical' or 'horizontal' which will determine if the code editor and preview are side-by-side or on top of each other.

> ##### [playground.html](playground.html)

## Benefits of Using `@gradio/lite`

### 1. Serverless Deployment

### 2. Low Latency

- By running in the browser, @gradio/lite offers low-latency interactions for users.

- There's no need for data to travel to and from a server, resulting in faster responses and a smoother user experience.

### 3. Privacy and Security

- User data remains on their device, providing peace of mind regarding data handling.

### Limitations

- Currently, the biggest limitation in using `@gradio/lite` is that your Gradio apps will generally take more time (usually 5-15 seconds) to load initially in the browser.

- Not every Python package is supported by Pyodide.
