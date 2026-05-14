# QuestPet

> Completion of this code was accelerated by AI and contributed to by my wife.

## Overview

**QuestPet** is a prototype desktop companion designed to blend productivity tracking, gamification, and personality-driven interaction. At its core, QuestPet is a growing digital creature (currently a blob) that reacts to user behavior such as completing tasks, idling, and investing in self-improvement.

Unlike a traditional AI assistant, QuestPet is intentionally built as a **state-driven desktop pet**: it observes patterns, forms a personality over time, and responds emotionally and contextually without relying on large language models. The long-term goal is to create a digital companion that feels alive, supportive, and occasionally challenging—without ever being harsh or mean.

## Features

- **Task Management**: Create, track, and complete quests with difficulty levels (easy, medium, hard)
- **XP & Leveling System**: Earn experience points by completing tasks and level up your pet
- **Personality Development**: Your pet develops traits based on your actions and stat allocation choices
- **Animated Sprites**: Multiple sprite-based animations including idle, sleeping, walking, and transitions
- **Streak Tracking**: Build daily completion streaks for motivation and bonus rewards
- **Desktop Companion**: Always-on-top window stays visible while you work
- **State-Based AI**: Pet responds based on internal emotional state, not language models

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- **Python 3.10+**
- **Pygame** (for graphics and rendering)
- **pywin32** (Windows API libraries for window management)

### Setup

1. Clone or download the QuestPet project files
2. Navigate to the project directory
3. Install required dependencies:

```bash
pip install pygame pywin32
```

## Usage

### Running the Application

```bash
python main.py
```

This launches the QuestPet window as an always-on-top desktop companion.

### How to Play

1. **Launch the application** to open the QuestPet window
2. **View active tasks** in the task manager window
3. **Select a task** and click "Complete Task" to earn XP for your pet
4. **Watch your pet grow** as you level up and earn growth points
5. **Allocate growth points** to develop your pet's personality through stat distribution
6. **Observe reactions** - your pet displays different animations and behaviors based on your actions
7. **Leave it idle** to see idle animations and personality-driven responses

## Project Structure

```
QuestPet/
├── main.py                    # Entry point
├── pet_renderer.py            # Legacy pet rendering
├── recycling.py               # Utility functions
├── personality2/              # Main application package
│   ├── PetCore.py            # Pet stats and leveling system
│   ├── PetRenderer.py        # Pygame-based sprite rendering
│   ├── PetAnimation.py       # Animation state management
│   ├── PetEventRouter.py     # Event handling and routing
│   ├── PetMind.py            # Pet decision making logic
│   ├── PetVoice.py           # Pet dialogue and messaging system
│   ├── TaskManager.py        # Task management and XP calculations
│   ├── Task.py               # Individual task class definition
│   └── TaskWindow.py         # Task UI interface window
├── visuals/                   # Graphics and animation assets
│   └── assets/
│       └── blob/             # Blob creature sprite animations
│           ├── idle/
│           ├── sleeping/
│           ├── idle_to_sleeping/
│           ├── sleeping_to_idle/
│           ├── walking_left/
│           └── walking_right/
└── README.md
```

## Development Environment

To recreate the development environment, you need:

- **Python 3.10+**
- **Pygame** (graphics rendering)
- **pywin32** (Windows window management)
- **Python Standard Library**: random, datetime, uuid, os

### Core Dependencies

- `pygame` - Sprite rendering and animation
- `win32gui`, `win32con`, `win32api` - Windows window management
- `datetime` - Task deadline tracking
- `uuid` - Unique task identification

## Technical Details

### Core Systems

- **PetCore**: Manages pet progression (level, XP, growth points), handles leveling-up mechanics
- **TaskManager**: Manages active/completed tasks, tracks daily streaks, calculates XP rewards based on difficulty and urgency
- **PetRenderer**: Uses Pygame to render sprites with transparency support for desktop overlay
- **Animation System**: State-based animation with smooth transitions (idle → sleeping, walking, etc.)

### XP Reward System

- **Base XP**: Easy tasks (10 XP), Medium tasks (20 XP), Hard tasks (40 XP)
- **Urgency Bonus**: Tasks due within 24 hours (+10 XP), within 72 hours (+5 XP)
- **Streak Multiplier**: Bonus multiplier increases based on consecutive daily completions

## Resources

The following websites were useful in developing this software:

- [Python Official Documentation](https://docs.python.org/)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Game Design Patterns – State Machines](https://gameprogrammingpatterns.com/state.html)
- [Human-Centered AI Design](https://www.nngroup.com/articles/ai-design/)

## Future Work

The following items are planned for future development:

- [ ] Implement an Instinct System (Play / Assist / Observe modes)
- [ ] Add emotional decay and cooldowns for pet behavior callouts
- [ ] Improve UserState modeling (stress, focus, motivation tracking)
- [ ] Introduce multiple creature types (dragon, golem, puppicorn)
- [ ] Add on-screen movement and interactive desktop interactions
- [ ] Integrate screen-reading for automatic task detection
- [ ] Optional AI-generated dialogue layer (hybrid system)
- [ ] Persist user and creature state between sessions
- [ ] Improve UI layout and visual feedback
- [ ] Add customization options for pet appearance and behavior

## Credits

- **Concept & Development**: Main developer
- **AI Assistance**: Code acceleration and implementation support
- **Special Thanks**: My wife's contributions and support ❤️
