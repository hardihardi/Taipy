# Using markdown syntax, passing the values as data
from taipy.gui import Gui
import numpy as np

xx = np.arange(0, 2 * np.pi, 0.01)
data = [{"x": xx,"y": np.sin(xx)}]

# Define a page using Markdown syntax
page_content = """
# Taipy Example
<|{data}|chart|mode=markers|layout={layout}|marker={markers}|>
"""

if __name__ == "__main__":
    Gui(page_content).run(title="Example")