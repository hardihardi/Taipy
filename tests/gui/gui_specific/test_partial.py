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

import json
import warnings
import time
import pytest
from types import SimpleNamespace

from taipy.gui import Gui, Markdown, State


def test_partial(gui: Gui):
    with warnings.catch_warnings(record=True):
        gui.add_partial(Markdown("#This is a partial"))
        gui.run(run_server=False)
        client = gui._server.test_client()
        response = client.get(f"/taipy-jsx/{gui._config.partial_routes[0]}")
        response_data = json.loads(response.get_data().decode("utf-8", "ignore"))
        assert response.status_code == 200
        assert "jsx" in response_data and "This is a partial" in response_data["jsx"]


def test_partial_update(gui: Gui):
    with warnings.catch_warnings(record=True):
        partial = gui.add_partial(Markdown("#This is a partial"))
        gui.run(run_server=False, single_client=True)
        client = gui._server.test_client()
        response = client.get(f"/taipy-jsx/{gui._config.partial_routes[0]}")
        response_data = json.loads(response.get_data().decode("utf-8", "ignore"))
        assert response.status_code == 200
        assert "jsx" in response_data and "This is a partial" in response_data["jsx"]
        # update partial
        fake_state = SimpleNamespace()
        fake_state._gui = gui
        partial.update_content(fake_state, "#partial updated")  # type: ignore
        response = client.get(f"/taipy-jsx/{gui._config.partial_routes[0]}")
        response_data = json.loads(response.get_data().decode("utf-8", "ignore"))
        assert response.status_code == 200
        assert "jsx" in response_data and "partial updated" in response_data["jsx"]

def test_partial_update_debug_modes(gui: Gui):
    with warnings.catch_warnings(record=True):
        partial = gui.add_partial(Markdown("#Initial content"))
        gui.run(run_server=False, single_client=True)
        client = gui._server.test_client()
        fake_state = SimpleNamespace()
        fake_state._gui = gui

        gui._config.debug = True
        partial.update_content(fake_state, "#Debug mode content")
        response = client.get(f"/taipy-jsx/{gui._config.partial_routes[0]}")
        debug_data = json.loads(response.get_data().decode("utf-8", "ignore"))

        gui._config.debug = False
        partial.update_content(fake_state, "#Non-debug mode content")
        response = client.get(f"/taipy-jsx/{gui._config.partial_routes[0]}")
        non_debug_data = json.loads(response.get_data().decode("utf-8", "ignore"))

        assert "jsx" in debug_data and "jsx" in non_debug_data
        assert debug_data["jsx"] != non_debug_data["jsx"]
        assert "Non-debug mode content" in non_debug_data["jsx"]

def test_rapid_updates(gui: Gui):
    with warnings.catch_warnings(record=True):
        partial = gui.add_partial(Markdown("#Initial content"))
        gui.run(run_server=False, single_client=True)
        client = gui._server.test_client()
        fake_state = SimpleNamespace()
        fake_state._gui = gui

        update_count = 5
        for i in range(update_count):
            partial.update_content(fake_state, f"#Update {i}")
            time.sleep(0.1)

        time.sleep(0.2)

        response = client.get(f"/taipy-jsx/{gui._config.partial_routes[0]}")
        final_data = json.loads(response.get_data().decode("utf-8", "ignore"))
        assert f"Update {update_count - 1}" in final_data["jsx"]

def test_streaming_updates(gui: Gui):
    with warnings.catch_warnings(record=True):
        partial = gui.add_partial(Markdown("#Initial content"))
        gui.run(run_server=False, single_client=True)
        client = gui._server.test_client()
        fake_state = SimpleNamespace()
        fake_state._gui = gui

        update_texts = ["Start", "Middle", "End"]
        for text in update_texts:
            partial.update_content(fake_state, f"#{text}")
            time.sleep(0.1)

        response = client.get(f"/taipy-jsx/{gui._config.partial_routes[0]}")
        final_data = json.loads(response.get_data().decode("utf-8", "ignore"))
        assert "End" in final_data["jsx"]

def test_error_handling(gui: Gui):
    with warnings.catch_warnings(record=True):
        partial = gui.add_partial(Markdown("#Initial content"))
        gui.run(run_server=False, single_client=True)

        invalid_state = SimpleNamespace()
        invalid_state._gui = None
        partial.update_content(invalid_state, "#Should not update")

        assert len(w) > 0
        assert any("callback" in str(warning.message) for warning in w)

def test_concurrent_updates(gui: Gui):
    with warnings.catch_warnings(record=True):
        partial = gui.add_partial(Markdown("#Initial content"))
        gui.run(run_server=False, single_client=True)
        client = gui._server.test_client()
        fake_state = SimpleNamespace()
        fake_state._gui = gui

        from threading import Thread
        import queue

        update_queue = queue.Queue()
        def update_worker():
            for i in range(5):
                partial.update_content(fake_state, f"#Thread update {i}")
                update_queue.put(i)
                time.sleep(0.1)

        threads = [Thread(target=update_worker) for _ in range(3)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        time.sleep(0.2)

        response = client.get(f"/taipy-jsx/{gui._config.partial_routes[0]}")
        final_data = json.loads(response.get_data().decode("utf-8", "ignore"))
        assert "Thread update" in final_data["jsx"]