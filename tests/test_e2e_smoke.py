import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from personality2.PetAnimation import PetAnimation
from personality2.PetCore import PetCore
from personality2.PetEventRouter import PetEventRouter
from personality2.PetMind import PetMind
from personality2.PetVoice import PetVoice
from personality2.TaskManager import TaskManager


class DummyRenderer:
    def __init__(self):
        self.current_state = None

    def set_state(self, state):
        self.current_state = state


class QuestPetSmokeTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.storage_path = Path(self.temp_dir.name) / "tasks.json"
        self.task_manager = TaskManager(storage_path=self.storage_path)
        self.core = PetCore()
        self.mind = PetMind()
        self.voice = PetVoice()
        self.renderer = DummyRenderer()
        self.animation = PetAnimation(self.renderer)
        self.router = PetEventRouter(self.core, self.mind, self.voice, self.animation, task_manager=self.task_manager)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_user_flow_from_task_creation_to_idle(self):
        task = self.task_manager.add_task("Ship lab", "Finish the QuestPet lab work", due=datetime.now())

        xp = self.task_manager.complete_task(task.id)
        task_response = self.router.on_task_completed(xp, task=task)
        idle_response = self.router.on_idle()

        self.assertTrue(task.completed)
        self.assertGreater(xp, 0)
        self.assertEqual(self.renderer.current_state, "idle")
        self.assertTrue(task_response)
        self.assertTrue(idle_response)


if __name__ == "__main__":
    unittest.main()
