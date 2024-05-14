# The `Interface` class

- The `gr.Interface` class is a high-level abstraction in Gradio that allows you to quickly create a demo for any Python function simply by specifying the input types and the output types.

- We see that the `Interface` class is initialized with three required parameters:

    - `fn`: the function to wrap a user interface (UI) around

    - `inputs`

        - which Gradio component(s) to use for the input.

        - The number of components should match the number of arguments in your function.

    - `outputs`

        - which Gradio component(s) to use for the output.

        - The number of components components should match the number of return values from your function.

## Components Attributes

- If you use the actual class instead of using the string shortcut, you have access to much more customizability through component attributes

> ##### [component_attribute.py](component_attribute.py)

## Multiple Input and Output Components

- Just as each component in the `inputs` list corresponds to one of the parameters of the function, in order, each component in the `outputs` list corresponds to one of the values returned by the function, in order.

> ##### [multiple_input_output.py](multiple_input_output.py)

## An Image Example

- Gradio supports many types of components, such as `Image`, `DataFrame`, `Video`, or `Label`.

> ##### [sepia_filter.py](sepia_filter.py)

- When using the `Image` component as input, your function will receive a NumPy array with the shape `(height, width, 3)`, where the last dimension represents the RGB values.

- We'll return an image as well in the form of NumPy array.

- You can also set the datatype used by the component with the `type =` keyword argument.

- If you wanted your function to take a file path to an image instead of a NumPy array, the input `Image` component could be written as:

    ```python
    gr.Image(type="filepath", shape=...)
    ```

- Out input `Image` component comes with an edit button, which allows for cropping and zooming into images.

- Manipulating images in this way can help reveal biases or hidden flaws in a machine learning model.

- You can read more about the many components and how to use them in the Gradio docs.

## Example inputs

- You can provide example data that a user can easily load into `Interface`

- To load example data, you can provide a `nested list` to the `examples =` keyword argument of the Interface constructor.

- Each sublist within the outer list represents a data sample, and each element within the sublist represents an input for each input component.

- The format of example data for each component is specified in the Gradio Docs.

> ##### [toy_calculator.py](toy_calculator.py)

- You can load a large dataset into the examples to browse and interact with the dataset through Gradio.

- The examples will be automatically paginated.

    - You can configure this through the `examples_per_page` argument of `Interface`).

- Continue learning about examples in the More On Examples guide.

## Descriptive Content

- `title`: which accepts text and can display it at the very top of interface, and also becomes the page title.

- `description`: which accepts text, markdown or HTML and places it right under the title.

- `article`: which also accepts text, markdown or HTML and places it below the interface.

- If you're using the `Blocks` API instead, you can insert text, markdown, or HTML anywhere using the `gr.Markdown(...)`, or `gr.HTML(...)` components, with descriptive content inside the `Component` constructor.

- Another useful keyword argument is `label =`, which is present in every `Component`.

- This modifies the label text at the top of each `Component`.

- You can also add the `info =` keyword argument to form elements like `Textbox` or `Radio` to provide further information on their usage.

## Additional Inputs within an Accordion

- The `Interface` class takes an `additional_inputs` argument which is similar to `inputs` but any input components included here are not visible by default.

- The additional inputs are passed into the prediction function, in order, after the standard inputs.

- You can customize the appearance of the accordion by using the optional `additional_inputs_accordion` argument, which accepts a string (in which case, it becomes the label of the accordion), or an instance of the `gr.Accordion()` class.

## Flagging

- By default, an `Interface` will have "Flag" button.

- When a user testing your `interface` sees input with interesting output, they can flag the input for you to review.

- Within the directory provided by the `flagging_dir =` argument to the `Interface` constructor, a CSV file will log the flagged inputs.

- If the interface involves file data folders will be created to store those flagged data as well.

- If you wish for the user to provide a reason for flagging, you can pass a list of strings to the `flagging_options` argument of Interface.

- User will have to select one of the strings when flagging, which will be saved as an additional column to the CSV.
