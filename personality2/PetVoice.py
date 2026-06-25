import random


class PetVoice:
	def __init__(self):
		self.lines = {
			"task_complete": {
				"play": ["Nice! Let's keep going.", "That was fast. On to the next one."],
				"assist": ["Good progress. I can help keep the pace.", "That task is down. Let's stay focused."],
				"observe": ["Noted. Another task is complete.", "I saw that one finish. Solid work."],
			},
			"level_up": {
				"play": ["We grew! Let's use that momentum.", "Level up. That feels good."],
				"assist": ["Growth unlocked. I’ll stay close and steady.", "Level up achieved. We can build from here."],
				"observe": ["Level up recorded.", "A new level has been reached."],
			},
			"idle": {
				"play": ["Need a nudge? Let's pick one small task.", "I'm ready when you are. Let's move."],
				"assist": ["I’m watching for anything that needs attention.", "Let’s check for the next useful step."],
				"observe": ["Observing quietly for now.", "I’m taking in the pace of the day."],
			},
			"overdue": {
				"play": ["Something slipped. Let's recover it.", "A task is overdue. Let's get back on track."],
				"assist": ["I found an overdue task. Let's handle it now.", "This needs attention. I’m staying on it."],
				"observe": ["An overdue task was detected.", "I noticed a task has passed its due time."],
			},
		}

	def get_line(self, event_name, mode="observe", context=None):
		normalized_event = event_name.lower()
		normalized_mode = (mode or "observe").lower()
		event_lines = self.lines.get(normalized_event, {})
		options = event_lines.get(normalized_mode) or event_lines.get("observe") or []

		if not options:
			return ""

		text = random.choice(options)
		context = context or {}
		return text.format(**context)
