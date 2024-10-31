from taipy.gui import Gui
import json

# Sample JSON data for testing
json_data = {
    "name": "Sample Data",
    "type": "Example JSON",
    "attributes": {
        "id": 123,
        "description": "A simple JSON structure for demonstration",
        "values": [1, 2, 3, 4, 5],
        "nested": {
            "flag": True,
            "count": 10
        }
    }
}

# Define the page with the JSON viewer
page = """
<|{json_data}|json|expandable|>
"""

if __name__ == "__main__":
    Gui(page).run(title="DataNode JSON Viewer Example")
