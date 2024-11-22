from taipy.gui import Gui, Icon

msgs = [
    ["1", "msg 1", "Alice", None],
    ["2", "msg From Another unknown User", "Charles", None],
    ["3", "This from the sender User", "taipy", "./beatrix-avatar.png"],
    ["4", "And from another known one", "Alice", None],
]
users = [
    ["Alice", Icon("./alice-avatar.png", "Alice avatar")],
    ["Charles", Icon("./charles-avatar.png", "Charles avatar")],
    ["taipy", Icon("./beatrix-avatar.png", "Beatrix avatar")],
]


def on_action(state, id: str, payload: dict):
    (reason, varName, text, senderId, imageData) = payload.get("args", [])
    msgs.append([f"{len(msgs) +1 }", text, senderId, imageData])
    state.msgs = msgs


page = """
<|{msgs}|chat|users={users}|allow_send_images|>
"""

if __name__ == "__main__":
    Gui(page).run(title="Chat - Images")
