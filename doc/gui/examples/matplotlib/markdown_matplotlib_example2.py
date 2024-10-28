# Using markdown syntax, saving the graph as an image and then displaying it
from taipy.gui import Gui
import matplotlib.pyplot as plt
import numpy as np

# Basic Matplotlib Chart
fig = plt.figure(figsize=(5, 4))
xx = np.arange(0, 2 * np.pi, 0.01)
plot = fig.subplots(1, 1)
plot.fill(xx, np.sin(xx), facecolor="none", edgecolor="purple", linewidth=2)
file_path = 'taipy\doc\gui\examples\matplotlib\images\graph.png'
plt.savefig(file_path)

# Define a page using Markdown syntax
page_content = """
# Taipy Example for Matplotlib Integration
<|{file_path}|image|>
"""

if __name__ == "__main__":
    Gui(page_content).run(title="Matplotlib Example")

#<|{plot}|chart|x=x|y=y|title=Matplotlib_Example|>