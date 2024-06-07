# Blocks and Event Listeners

- We briefly described the Blocks class in the Quickstart as a way to build custom demos.

## Blocks Structure

> #### [demo.py](demo.py)

- First, note the `with gr.Blocks() as demo:` clause.

    - The Blocks app code will be contained within this clause.

- Next come the Components.

    - Components are automatically added to the Blocks as they are created within the `with` clause.

- Finally, the `click()` event listener.

    - Event listenersdefine the data flow within the app.

    - This dataflow is triggered when the Button is clicked.

    - An event listner can take multiple inputs or outputs.

- You can also attach event listeners using decorators - skip the `fn` argument and assign `inputs` and `outputs` directly:

> ##### [decorator.py](decorator.py)

## Event Listeners and Interactivity

- Any component that acts as an input to an event listener is made interactive.

- Any component that acts as an output isn't made interactive.

- You can override the default behavior and directly configure the interactivity of a Component with the boolean `interactive` keyword argument.

- If a component is constructed with a default value, then it is presumed to be displaying content and is rendered non-interactive. 

## Types of Event Listeners

> ##### [change.py](change.py)

- The `welcome` function is triggered by typing in the Textbox `inp`.

- Different Components support different eventlisteners.

- For example, the `Video` Component supports a `play()` event listener, triggered when user presses play.

- See Gradio Docs for the event listeners for each Component.

## Multiple Data Flows

> ##### [multiple_data_flows.py](multiple_data_flows.py)

## Function Input List vs Dict

- If you'd like to have multiple input components pass data to the function, you have two options on how the function can accept input component values:

    1. as a list of arguments, or

    2. as a single dictionary of values, keyed by the component

- It is a matter of preference which syntax you prefer.

> ##### [function_input.py](function_input.py)

## Function Return List vs Dict

- You may return values for multiple output components either as:

    1. a list of values, or

    2. a dictionary keyed by the component

- You can return a dictionary, with the key corresponding to the output component and the value as the new value.

> ##### [function_return_dict.py](function_return_dict.py)

- This also allows you to skip updating some output components.

## Updating Component Configurations

- We return a new Component, setting the properties we want to change.

> ##### [update_component.py](update_component.py)

- Any arguments we do not set will use their previous values.

## Examples

- You can add examples for your functions.

- Instantiate a `gr.Examples`.

- The constructor of `gr.Examples` takes two required arguments:

    - `examples`: a nested list of examplse, in which the outer list consists of examples and each inner list consists of an input corresponding to each input component

    - `inputs`: the component or list of components that should be populated when the examples are clicked

- You can also set `cache_examples = True`, in which case two additional arguments must be provided.

    - `outputs`: the component or list of components corresponding to the output of the examples

    - `fn`: the function to run to generate the outputs corresponding to the examples.

> ##### [examples.py](examples.py)

- In Gradio 4.0 or later, when you click on examples, not only does the value of the input component update to the example value, but the component's configuration also reverts to the properties with which you constructed the component.

## Running Events Consecutively

- You can also run events consecutively by using the `then` method of an event listener.

- This will run an event after the previous event has finished running.

> ##### [then.py](then.py)

- The `then()` method of an event listener executes the subsequent event regardless of whether the previous event raised any errors.

- If you'd like to only run subsequent events if the previous event executed successfully, use the `.success()` method, which takes the same arguments as `.then()`.

## Running Events Continuously

- You can run events on a fixed schedule using the `every` parameter of the event listener.

- This will run the event `every` number of seconds while the client connection is open.

- If the connection is closed, the event will stop running after the following iteration.

- This does not take into account the runtime of the event itself.

- This parameter does not apply to the `js` function, only the Python function associated with the event listener.

> ##### [every.py](every.py)

- Gathering Event Data

- You can gather specific data about an event by adding the associated event data class as a type hint to an argument in the event listener function.

- For example, event data for `.select()` can be type hinted by a `gradio.SelectData` argument.

- This event is triggered when a user selects some part of the triggering component, and the event data includes information about what the user specifically selected.

> ##### [tic_tac_toe.py](tic_tac_toe.py)

## Binding Multiple Triggers to a Function

- For example, you may want to allow a user to click a submit button, or press enter to submit a form.

- You can do this using the `gr.on` method and passing a list of triggers to the `trigger`.

> ##### [on.py](on.py)

- You can use decorator syntax as well:

> ##### [on_decorator.py](on_decorator.py)

- You can use `gr.on` to create "live" events by binding to the `change` event of components that implement it.

- If you do not specify any trigger, the function will automatically bind to all `change` event of all input components that include a `change` event.

> [live.py](live.py)

- You can follow `gr.on` with `.then`.
