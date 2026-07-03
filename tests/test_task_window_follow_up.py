import tempfile
import unittest
from pathlib import Path

from personality2.TaskManager import TaskManager
from personality2.TaskWindow import TaskWindow


class DummyRenderer:
    def __init__(self):
        self.brought_to_front = False

    def bring_to_front(self):
        self.brought_to_front = True


class DummyAnimationRenderer:
    def __init__(self):
        self.current_state = None

    def set_state(self, state):
        self.current_state = state


class TaskWindowFollowUpTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.storage_path = Path(self.temp_dir.name) / "tasks.json"
        self.task_manager = TaskManager(storage_path=self.storage_path)
        self.renderer = DummyRenderer()
        self.window = TaskWindow(self.task_manager)
        self.window.pet_renderer = self.renderer

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_task_manager_persists_and_loads_tasks(self):
        self.task_manager.add_task("Write notes", "Persist me", difficulty="hard")
        self.task_manager.save_state()

        reloaded = TaskManager(storage_path=self.storage_path)
        self.assertEqual(len(reloaded.active_tasks), 1)
        self.assertEqual(reloaded.active_tasks[0].title, "Write notes")
        self.assertEqual(reloaded.active_tasks[0].difficulty, "hard")

    def test_close_returns_to_pet(self):
        class FakeWindow:
            def destroy(self):
                self.destroyed = True

        self.window.window = FakeWindow()
        self.window.close()

        self.assertTrue(self.renderer.brought_to_front)

    def test_autosave_on_add_edit_delete_and_complete(self):
        self.task_manager.add_task("First", "Task one")
        self.task_manager.save_state()

        self.task_manager.add_task("Second", "Task two")
        self.task_manager.save_state()

        loaded = TaskManager(storage_path=self.storage_path)
        self.assertEqual(len(loaded.active_tasks), 2)


if __name__ == "__main__":
    unittest.main()