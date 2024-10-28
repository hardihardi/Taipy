from taipy.gui import Gui

# Read the saved HTML chart
with open("chart.html", "r") as f:
    html_str = f.read()

# Define the page content with the interactive chart
page_md = f"""
# Taipy Matplotlib Enhanced 2D Scatter Plot Page

This page contains an enhanced 2D scatter plot created with Matplotlib:

<figure style="width: 100%; height: auto; display: flex; justify-content: center;">
    {html_str}
</figure>

## Code

The following Python code was used to generate the chart:

```python
import matplotlib.pyplot as plt
import numpy as np
import mpld3

plt.style.use('_mpl-gallery')

# Make the data
np.random.seed(3)
x = np.random.uniform(1, 6, 24)  # Random x values within 1-6
y = np.random.uniform(1, 6, 24)  # Random y values within 1-6

# Size and color
sizes = np.random.uniform(300, 800, len(x))  # Adjusted sizes for better fit
colors = np.random.uniform(50, 100, len(x))  # Greenish colors

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(x, y, s=sizes, c=colors, cmap="Greens", vmin=30, vmax=80)
ax.set(xlim=(1, 6), xticks=np.arange(1, 7), ylim=(1, 6), yticks=np.arange(1, 7))

# Add axis labels
ax.set_xlabel('Performance Score')
ax.set_ylabel('Happiness Index')
ax.set_title('Employee Performance vs. Happiness')

# Example labels for bubbles
for i in range(len(x)):
    ax.text(x[i], y[i], f'Employee {i+1}', fontsize=9, ha='right')

# Create legend for bubble sizes
legend_labels = np.unique(np.round(sizes, decimals=-1))
for label in legend_labels:
    ax.scatter([], [], c='g', alpha=0.5, s=label, label=str(int(label)))

legend1 = ax.legend(title="Bubble Size (Efficiency)", loc="upper right", frameon=True, fontsize=10)
ax.legend(title="Bubble Size (Efficiency)", scatterpoints=1, labelspacing=1.5)
ax.add_artist(legend1)

# Convert the plot to an interactive HTML
html_str = mpld3.fig_to_html(fig)

# Save the HTML to a file
with open("chart.html", "w") as f:
    f.write(html_str)

# Show the plot in a browser
mpld3.show()
\```

\```

Gui(page_md).run()
