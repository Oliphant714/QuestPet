---
name: questpet-story-planning
description: >
  Use this skill whenever creating, reviewing, or expanding feature stories for QuestPet.
  Triggers: any request to write a new story, fill out a _TEMPLATE.md, plan a feature,
  generate acceptance criteria, write functional requirements, or review an existing story
  for completeness. Also triggers when asked to reason about feature sequencing,
  dependencies between modules, or which story to implement next.
model: claude-opus-4-6
---

# QuestPet — Story Planning Skill

## Purpose

This skill configures the AI to act as a senior product/engineering planner for QuestPet.
It ensures every story produced follows the project template exactly, stays grounded in
the actual codebase, and is independently deployable.

---

## Project Context

**QuestPet** is a Python desktop companion app that gamifies task completion via a
sprite-based pet. Key modules:

| File | Responsibility |
|---|---|
| `personality2/Task.py` | Task data model — `id`, `title`, `description`, `difficulty`, `due`, `xp_reward`, `completed` |
| `personality2/TaskManager.py` | CRUD, streak tracking, `award_xp`, `save_state`, `load_state` (JSON) |
| `personality2/TaskWindow.py` | Tkinter UI — active/completed listboxes, add/edit/delete/complete buttons |
| `personality2/PetCore.py` | `level`, `xp`, `xp_to_next`, `growth_points`, `gain_xp`, `level_up` |
| `personality2/PetMind.py` | Mode FSM — play/assist/observe, auto vs manual override |
| `personality2/PetEventRouter.py` | Wires task events → XP gain → animation → voice line |
| `personality2/PetVoice.py` | Dialogue lines keyed by event + mode |
| `personality2/PetAnimation.py` | Delegates to `PetRenderer.set_state` |
| `personality2/PetRenderer.py` | Pygame sprite rendering, always-on-top Win32 window |
| `main.py` | Wires all components together |

Persistence: `questpet_tasks.json` in the project root (JSON, written by `TaskManager.save_state`).

---

## Template Rules

Every story MUST follow `_TEMPLATE.md` exactly — 19 numbered sections. Adapt each section
to QuestPet's context:

- Sections 6 (Non-Functional), 9 (API Surface), and 17 (Docs/Training) may be brief
  ("N/A — desktop app, no network API") but must not be omitted.
- Section 8 (Data Model) maps to JSON schema changes in `questpet_tasks.json` or new
  `Task`/`PetCore` fields — not SQL.
- Section 10 (UI/UX) maps to Tkinter widgets, not web components.
- Section 11 (AI/ML) is skipped unless the story involves Claude API calls.
- Severity: BLOCKER = app crashes or data lost; MAJOR = core loop broken; MINOR = polish.
- Effort: use XS/S/M/L/XL — don't invent new sizes.
- Feature IDs follow the pattern `{folder-number}.{story-number}` (e.g. `1.1`, `2.3`).

---

## Story Independence Rule

Each story must be **independently deployable** — a developer should be able to implement
it, run the app, and verify it works without waiting for any sibling story in the same
folder. If a story depends on another, list it in section 13 and the metadata `Depends on`
field.

---

## Acceptance Criteria Format

Always Given/When/Then. Each AC must be automatable in principle (pytest or manual
test script). Minimum 3 ACs per story.

---

## Workflow for Story Generation

1. Read the relevant feature folder name and existing stories to avoid duplication.
2. Identify which existing files in `personality2/` are touched.
3. Fill every section — do not leave placeholder text from the template.
4. Write FR entries as MUST/SHOULD/MAY (RFC 2119).
5. Check: is this story independently deployable? If not, split it.

---

## Feature Folder Map

| Folder | Feature Area | Owner |
|---|---|---|
| `persistence/` | Save/load state to disk | TaskManager |
| `task-management/` | CRUD, deadlines, filtering | TaskManager + TaskWindow |
| `xp-and-leveling/` | XP rewards, level-up, growth points | PetCore + PetEventRouter |
| `pet-behavior/` | Mood FSM, voice lines, animations | PetMind + PetVoice + PetAnimation |
| `ui-task-window/` | Tkinter window layout, sidebar, tabs | TaskWindow |
| `instinct-system/` | Play/Assist/Observe mode switching | PetMind + PetEventRouter |
