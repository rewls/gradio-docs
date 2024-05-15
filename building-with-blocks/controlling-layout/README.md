# Controlling Layout

- By default, Components in Blocks are arranged vertically.

- Under the hood, this layout structure uses the flexbox model of web development.

    - See https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox.

## Rows

- Elements within a `with gr.Row` clause will all be displayed horizontally.

- To make every element in a Row have the same height, use the `equal_height` argument of the `style` method.

> ##### [equal_height.py](equal_height.py)

- The widths of elements in a Row can be controlled via a combination of `scale` and `min_width` arguments that are present in every Component.

- `scale` is an integer that defines how an element will take up space in a Row.

- If scale is set to `0`, the element will not expand to take up space.

- If scale is set to 1 or greater, the element will expand.

- Multiple elements in a row will expand proportional to their scale.

> ##### [scale.py](scale.py)

- `min_width` will set the minimum width the element will take.

- The Row will wrap if there isn't sufficient space to satisfy all `min_width` values.

- Lean more about Rows in Row.

## Columns and Nesting

- Components within a Column will be placed vertically atop each other.

- Since the vertical layout is the default layout for Blocks apps anyway, Columns are usually nested within Rows.

> ##### [column.py](column.py)

Learn more about Columns in Column.

## Dimensions

- You can control the height and width of various components, where the parameters are available.

- These parameters accept either a number (interpreted as pixels) or a string.

- Using a string allows the direct application of any CSS unit to the encapsulating Block element, catering to more specific design requirements.

- When omitted, Gradio uses default dimensions suited for most use cases.

> ##### [viewport_width.py](viewport_width.py)

- When using percentage values for dimensions, you may want to define a parent component with an absolute unit (e.g. `px` or `vw`)

> ##### [percentage.py](percentage.py)

- You can apply any valid CSS unit for these parameters.

- For a comprehensive list of CSS units, refer to https://www.w3schools.com/cssref/css_units.php.

## Tabs and Accordions

- You can also create Tabs using the `with gr.Tab('tab_name'):` clause.

- Any component created inside of this clause context appears in that tab.

- Consecutive Tab clauses are grouped together so that a single tab can be selected at one time, and only the components within that Tab's context are shown.

> ##### [tab.py](tab.py)

- The `gr.Accordion('label')` is a layout that can be toggled open or closed.

- Any components that are defined inside of a `with gr.Accordion('label'):` will be hidden or shown when the accordion's toggle icon is clicked.

- See Tab and Acordion.

## Visibility

- Both components and Layout elements have a `visible` argument.

> ##### [visibility.py](visibility.py)

## Variable Number of Outputs

- By adjusting the visibility of components in a dynamic way, it is possible to create demos with Gradio that support a *variable numbers of outputs*.

> ##### [variable_outputs.py](variable_outputs.py)

## Defining and Rendering Components Separately

- In some cases, you might want to define components before you actually render them in your UI.

- The solution is to define components outside of the `gr.Blocks()` scope and use the component's `.render()` method wherever you'd like it placed in the UI.

> ##### [render.py](render.py)
