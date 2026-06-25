import unittest
from datetime import datetime, timedelta

from personality2.PetAnimation import PetAnimation
from personality2.PetCore import PetCore
from personality2.PetEventRouter import PetEventRouter
from personality2.PetMind import PetMind
from personality2.PetVoice import PetVoice
from personality2.Task import Task
from personality2.TaskManager import TaskManager


class FakeRenderer:
    def __init__(self):
        self.current_state = None

    def set_state(self, state):
        self.current_state = state


class InstinctSystemIntegrationTests(unittest.TestCase):
    def setUp(self):
        Task.next_id = 1
        self.core = PetCore()
        self.mind = PetMind()
        self.voice = PetVoice()
        self.renderer = FakeRenderer()
        self.animation = PetAnimation(self.renderer)
        self.task_manager = TaskManager()
        self.router = PetEventRouter(self.core, self.mind, self.voice, self.animation, task_manager=self.task_manager)

    def test_task_completion_routes_through_play_mode(self):
        task = self.task_manager.add_task("Finish notes", "Wrap up the session", difficulty="medium")

        xp = self.task_manager.complete_task(task.id)
        response = self.router.on_task_completed(xp, task=task)

        self.assertTrue(task.completed)
        self.assertGreater(xp, 0)
        self.assertEqual(self.mind.get_mode(), "play")
        self.assertEqual(self.renderer.current_state, "walking_right")
        self.assertTrue(response)

    def test_idle_switches_to_observe_mode(self):
        response = self.router.on_idle()

        self.assertEqual(self.mind.get_mode(), "observe")
        self.assertEqual(self.renderer.current_state, "idle")
        self.assertTrue(response)

    def test_overdue_task_switches_to_assist_mode(self):
        overdue_task = self.task_manager.add_task(
            "Submit report",
            "This should be overdue",
            due=datetime.now() - timedelta(days=1),
        )

        overdue_tasks = self.task_manager.get_overdue_tasks()
        self.assertIn(overdue_task, overdue_tasks)

        response = self.router.on_overdue_task(task=overdue_task)

        self.assertEqual(self.mind.get_mode(), "assist")
        self.assertEqual(self.renderer.current_state, "walking_left")
        self.assertTrue(response)

    def test_manual_mode_stays_fixed_through_events(self):
        self.router.set_mode("assist")
        task = self.task_manager.add_task("Manual check", "Confirm manual mode")
        xp = self.task_manager.complete_task(task.id)

        response = self.router.on_task_completed(xp, task=task)

        self.assertEqual(self.mind.get_mode(), "assist")
        self.assertEqual(self.renderer.current_state, "walking_left")
        self.assertTrue(response)


if __name__ == "__main__":
    unittest.main()