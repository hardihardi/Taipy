# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
# -----------------------------------------------------------------------------------------
# To execute this script, make sure that the taipy-gui package is installed in your
# Python environment and run:
#     python <script>
# -----------------------------------------------------------------------------------------
# Matplotlib scatter chart example
from taipy.gui import Gui, Markdown
import matplotlib.pyplot as plt
import numpy as np

# Define data
employee_performance = [2, 3.5, 2, 3.5, 3, 4]
happiness_scores = [2, 3, 4, 5, 2, 3]

# Calculate sizes based on product of performance and happiness, scaled to 1-100%
sizes = [e * h * 20 for e, h in zip(employee_performance, happiness_scores)]
colors = sizes  # Color based on sizes

# Create the Matplotlib figure
fig, ax = plt.subplots(figsize=(10, 5.2))  # Adjust figsize for a slightly smaller chart
scatter = ax.scatter(employee_performance, happiness_scores, s=sizes,
                     c=colors, cmap="Greens", vmin=min(colors), vmax=max(colors))
ax.set(xlim=(1, 6), xticks=np.arange(1, 7), ylim=(1, 6), yticks=np.arange(1, 7))
ax.set_xlabel('Performance Score')
ax.set_ylabel('Happiness Index')
ax.set_title('Employee Performance vs. Happiness')

# Example labels for bubbles
for i in range(len(employee_performance)):
    ax.text(employee_performance[i], happiness_scores[i], f'Emp {i+1}', fontsize=12, ha='right')

# Scale sizes to percentages
scaled_sizes = [size / max(sizes) * 100 for size in sizes]

# Create legend with employee labels and matching bubble colors and percentages
scaled_sizes = [size / max(sizes) * 100 for size in sizes]
handles = [
    plt.Line2D(
        [0], [0], marker='o', color='w', 
        markerfacecolor=plt.cm.Greens(color / max(colors)),
        markersize=np.sqrt(size) / 1,
        label=f'Emp {i+1} ({int(size)}%)'
    )
    for i, (color, size) in enumerate(zip(colors, scaled_sizes))
]
legend1 = ax.legend(handles=handles, title="Employees and Efficiency (%)",
                     loc="center left", bbox_to_anchor=(1, 0.5), frameon=True, fontsize=10, labelspacing=2)
ax.add_artist(legend1)

# Positioning the legend to avoid clipping
legend1 = ax.legend(handles=handles, title="Employees and Efficiency (%)",
                     loc="center right", bbox_to_anchor=(-0.2, 0.5), frameon=True, fontsize=10, labelspacing=2)
ax.add_artist(legend1)

# Adjust layout to ensure everything fits
plt.tight_layout(rect=[0, 0, 0.75, 1])

# Define Taipy page content
page_content = Markdown("""
    # Matplotlib 2D Scatter Plot
    <|part|content={fig}|class_name=scatter-plot|>
    """,style={
    ".scatter-plot": {
        "display": "block",
        "margin": "auto",
        "height": "560px",
    }
})

if __name__ == "__main__":
    Gui(page_content).run(title="Chart-Scatter-Matplotlib")
