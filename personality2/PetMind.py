class PetMind:
	MODES = ("play", "assist", "observe")

	def __init__(self):
		self.current_mode = "observe"
		self.manual_override = False
		self.last_event = None
		self.idle_events = 0
		self.task_completion_events = 0
		self.overdue_events = 0
		self.mode_reason = "startup"

	def set_mode(self, mode, manual=True, reason=None):
		normalized_mode = mode.lower()
		if normalized_mode not in self.MODES:
			raise ValueError(f"Unknown instinct mode: {mode}")

		self.current_mode = normalized_mode
		self.manual_override = manual
		if reason is not None:
			self.mode_reason = reason
		return self.current_mode

	def set_auto_mode(self, mode=None, reason=None):
		if mode is None:
			mode = self._auto_mode_from_state()
		return self.set_mode(mode, manual=False, reason=reason or "automatic selection")

	def get_mode(self):
		return self.current_mode

	def describe_mode(self):
		mode_label = self.current_mode.title()
		prefix = "Manual" if self.manual_override else "Auto"
		return f"{prefix}: {mode_label}"

	def _auto_mode_from_state(self):
		if self.overdue_events > 0:
			return "assist"
		if self.idle_events >= 2:
			return "observe"
		if self.task_completion_events > self.idle_events:
			return "play"
		return "observe"

	def on_task_complete(self, task=None, task_manager=None):
		self.task_completion_events += 1
		self.last_event = "task_complete"

		if self.manual_override:
			return self.current_mode

		if task_manager is not None and hasattr(task_manager, "get_overdue_tasks"):
			if task_manager.get_overdue_tasks():
				return self.set_mode("assist", manual=False, reason="overdue tasks need attention")

		if task_manager is not None and getattr(task_manager, "streak", 0) >= 3:
			return self.set_mode("play", manual=False, reason="completion streak")

		return self.set_mode("play", manual=False, reason="task completed")

	def on_idle(self, task_manager=None):
		self.idle_events += 1
		self.last_event = "idle"

		if self.manual_override:
			return self.current_mode

		if task_manager is not None and hasattr(task_manager, "get_overdue_tasks"):
			if task_manager.get_overdue_tasks():
				return self.set_mode("assist", manual=False, reason="idle with overdue tasks")

		if self.idle_events >= 2:
			return self.set_mode("observe", manual=False, reason="idle observation")

		return self.set_mode("observe", manual=False, reason="idle")

	def on_overdue_task(self, task=None, task_manager=None):
		self.overdue_events += 1
		self.last_event = "overdue"

		if self.manual_override:
			return self.current_mode

		return self.set_mode("assist", manual=False, reason="overdue task")
