from taipy.gui import Gui

status = [
    ("warning", "Task is launched."),
    ("warning", "Taks is waiting."),
    ("error", "Task timeout."),
    ("success", "Task Succeded"),
    ("info", "Process was cancelled.")
]

page = """
<|{status}|status|icons|>
"""

if __name__ == "__main__":
  Gui(page).run(title="Status - With icons")
