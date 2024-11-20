from taipy.gui import Gui

status = [
    ("warning", "Task is launched."),
    ("warning", "Taks is waiting."),
    ("error", "Task timeout."),
    ("success", "Task Succeded"),
    ("info", "Process was cancelled.")
]

# Info: svg icon (pants.svg)
# success: no icon
# warning: default icon
# error: inline svg icon (red disc)
page = """
<|{status}|status|icons=https://www.svgrepo.com/show/530594/pants.svg;false;true;<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24'><circle cx='12' cy='12' r='10' fill='red'/></svg>|>
"""

if __name__ == "__main__":
  Gui(page).run(title="Status - With mixed icons")
