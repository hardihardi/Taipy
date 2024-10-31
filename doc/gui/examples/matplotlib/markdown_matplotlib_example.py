#Using markdown syntax
import matplotlib.pyplot as plt
import numpy as np

from taipy.gui import Gui, Markdown

fig = plt.figure(figsize=(5,4))
xx = np.arange(0, 2 * np.pi, 0.01)
plot = fig.subplots(1, 1)
plot.fill(xx, np.sin(xx), facecolor="none", edgecolor="purple", linewidth=2)

# Define a page using Markdown syntax
page_content = Markdown("""
# Taipy Example for Matplotlib Integration using Markdown Syntax
<|part|content={fig}|class_name=matplotlib_example|>
""",style={
    ".matplotlib_example": {
        "display": "inline-flex",
        "width": "520px",
        "height": "420px"
    }}
)

if __name__ == "__main__":
    Gui(page_content).run(title="Matplotlib Example")
