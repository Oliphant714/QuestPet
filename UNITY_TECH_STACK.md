# QuestPet — Unity Tech Stack Recommendation

This document summarizes recommended technologies, implementation notes, persistence tradeoffs, CI examples, integration options with your existing Python logic, and the exact research prompts used.

## Summary / Recommendation
- Engine: Unity (use the latest Long-Term Support (LTS) release available when you begin development)
- Language: C# (Unity scripting)
- Primary target: Windows Standalone (desktop always-on-top companion). Optionally support macOS/Linux/mobile later.
- Why: Unity provides mature 2D workflows, a powerful animation system, cross-platform portability, and a large ecosystem of packages and tooling — a good fit for QuestPet's sprite-based companion and potential future ports.

## Key Packages and Tools
- Unity packages (via Package Manager)
  - 2D Animation
  - 2D Sprite / SpriteShape
  - Addressables (asset loading & memory management)
  - Input System
  - UI Toolkit (recommended) or uGUI
  - Unity Test Framework (EditMode & PlayMode tests)
- Editor/IDE: Visual Studio (Windows) or Rider
- Version control: Git + Git LFS (store textures, sprite sheets)
- Optional third-party libraries
  - DOTween (tweening, optional)
  - Odin Inspector (editor productivity, optional)
  - LiteDB or SQLite wrappers for Unity (if using embedded DB)

## Persistence Options (tradeoffs)
- JSON files (simple)
  - Pros: Easy to implement, human-readable, portable, minimal dependencies
  - Cons: No querying, less robust for larger structured data, risk of partial writes unless handled carefully
  - Recommended for: Small prototyping and simple save/load of pet state and tasks
- SQLite (embedded)
  - Pros: Structured storage, ACID, easy to migrate, tooling available (SQLite-net, SQLite4Unity3d)
  - Cons: Slightly more complex integration, additional binary dependency
  - Recommended for: Robust local persistence with structured queries and future scaling
- LiteDB (embedded .NET DB)
  - Pros: No native binaries on some targets, document-oriented API (like MongoDB), easy to use from C#
  - Cons: Larger dependency, less ubiquitous than SQLite
- PlayerPrefs
  - Pros: Fast for small key/value pairs
  - Cons: Not suitable for complex data; not recommended for full game state
- Cloud options (PlayFab, Firebase)
  - Pros: Cloud save, analytics, remote config, leaderboards
  - Cons: Requires accounts, network dependency, privacy considerations

Recommendation: Start with JSON for rapid prototyping; migrate to SQLite (or LiteDB) before production for reliability and queryability. Use an abstraction layer (ISaveService) so you can change backend with minimal code changes.

## Always-on-top Desktop Window (Windows)
Unity standalone windows do not expose a built-in "always-on-top" toggle in the player settings. Use a small native call on Windows to set the window as topmost when running standalone:

C# snippet (Windows-only):

```csharp
using System.Runtime.InteropServices;

public class WindowTopmost {
    [DllImport("user32.dll")]
    private static extern bool SetWindowPos(System.IntPtr hWnd, System.IntPtr hWndInsertAfter, int X, int Y, int cx, int cy, uint uFlags);

    private static readonly System.IntPtr HWND_TOPMOST = new System.IntPtr(-1);
    private const uint SWP_NOSIZE = 0x0001;
    private const uint SWP_NOMOVE = 0x0002;

    public static void MakeTopmost() {
        var hwnd = GetUnityWindowHandle();
        SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE);
    }

    private static System.IntPtr GetUnityWindowHandle() {
        // On Windows, Unity's window handle can be retrieved via Process.MainWindowHandle or platform-specific API.
        return System.Diagnostics.Process.GetCurrentProcess().MainWindowHandle;
    }
}
```

Call `WindowTopmost.MakeTopmost()` after the player window has been created (e.g., in a warm-up scene or after first frame). For editor testing, you can no-op this.

## Project Layout (recommended)
```
Assets/
  Scenes/
    Main.unity       # Boot scene (initialize services)
    UI.unity         # Task UI / overlay
  Scripts/
    Core/            # PetCore, TaskManager, SaveService interfaces
    UI/              # UI Toolkit or uGUI controllers
    Audio/
    Animations/
  Addressables/
  Resources/
ProjectSettings/
.gitignore
README.md
```
- Use Addressables for large sprite sheets and optional downloadable content.
- Keep the pet logic modular: `PetCore` (stats, leveling), `TaskManager` (task lifecycle), `PetMind` (decision-making), `PetRenderer` (animation glue).

## Integration with existing Python code
Options:
- Rewrite in C# (recommended)
  - Pros: Best integration, performance, portability, easier testing and debugging within Unity
  - Cons: Requires porting effort
- IPC (local socket / REST / named pipes)
  - Pros: Keeps Python logic as-is, lower risk for logic correctness during migration
  - Cons: Extra process to ship and manage, adds latency, increased complexity for packaging
- Embed Python (pythonnet, or embedding CPython)
  - Pros: Can call Python from C# directly
  - Cons: Complex to set up cross-platform, brittle for Unity builds, native dependency issues

Recommendation: Port deterministic game logic (XP calculations, task rules) to C# and keep Python code as a reference. If you need a short-term bridge, use a local IPC socket for prototyping.

## UI Choice: UI Toolkit vs uGUI
- UI Toolkit
  - Pros: Modern, faster runtime performance, CSS-like styling, good for tool-like overlays
  - Cons: Newer; smaller ecosystem of third-party widgets
- uGUI
  - Pros: Mature, many examples and assets available
  - Cons: Less performant for complex dynamic UIs

Recommendation: Use **UI Toolkit** for a lightweight desktop overlay and more maintainable UI code; choose uGUI if you need quick prototyping or existing uGUI experience.

## Testing & CI
- Use Unity Test Framework for unit and integration tests.
- CI: GitHub Actions with `game-ci/unity-builder` (or similar) to run tests and produce builds.

Example GitHub Actions snippet (minimal):

```yaml
name: Unity CI
on: [push]
jobs:
  build:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Unity
        uses: game-ci/unity-builder@v2
        with:
          unityVersion: 2023.3.0f1 # set to the LTS you use
      - name: Run EditMode tests
        run: |
          # example command; adapt to your runner
          unity -runTests -testPlatform EditMode -logFile -
      - name: Build Windows
        uses: game-ci/unity-builder@v2
        with:
          targetPlatform: Win64
```

Adjust versions and actions to the specific LTS you choose.

## Git / LFS
- `.gitignore`: exclude `Library/`, `Temp/`, `Build/`, `obj/` and other generated folders
- Use `git lfs track "*.png" "*.psd" "*.wav"` and commit `.gitattributes`

## Security & Privacy
- Keep user data local unless you add cloud sync and inform users.
- If using cloud services, add opt-in and clear privacy notes.

## Quick Setup Steps (local development)

```bash
# Create project (manual in Unity Hub) or via CLI
# Initialize git
git init
git lfs install
# Track assets
git lfs track "*.png" "*.psd" "*.wav"
```

## Research Prompts (exact)
1.
```
For a desktop always-on-top companion app with 2D sprite animations and task management, recommend a Unity-based tech stack: which Unity LTS version to use, C# settings, persistence choices (JSON vs SQLite vs PlayerPrefs vs embedded DB), recommended Unity packages (Addressables, 2D Animation, Input System), and deployment targets. Include pros/cons and estimated learning curve.
```

2.
```
Compare persistence options for saving game state in Unity: JSON files, SQLite, PlayerPrefs, LiteDB, and cloud solutions (PlayFab, Firebase). For a single-user Windows desktop app, which is best and why? Explain tradeoffs for reliability, ease of implementation, and migration to cloud.
```

3.
```
List Unity packages and third-party libraries useful for a 2D desktop companion: sprite animation, state machines, asset management, animation blending, and desktop always-on-top behavior on Windows. Provide implementation notes or links.
```

4.
```
Recommend a project layout and workflow for QuestPet in Unity: scene organization, asset folders, Addressables usage, Git + Git LFS setup, and editor/runtime settings to optimize startup time and memory for an always-on-top desktop app.
```

5.
```
Provide a minimal GitHub Actions CI configuration to run Unity EditMode tests and produce a Windows standalone build. Include necessary action steps and secrets.
```

6.
```
If I have existing Python code (task logic, XP calculation), what are the best ways to integrate it with Unity: rewrite in C#, use IPC (local socket), or embed Python (pythonnet)? Compare pros/cons and recommend an approach for portability.
```

7.
```
Which Unity UI system is better for a small desktop overlay: UI Toolkit or uGUI? Compare pros/cons for runtime overlays and maintainability in a 2D sprite-based app.
```

8.
```
Provide recommended Unity project settings for a small always-on-top desktop app (scripting runtime, API compatibility level, serialization settings, build settings) to minimize size and maximize stability.
```

9.
```
Draft a 200–300 word project summary describing QuestPet (purpose, key features, why Unity is chosen), suitable for assignment submission.
```

## Draft Project Summary (200–300 words)

QuestPet is an intimate desktop companion designed to turn productivity into play. The application runs as a lightweight always-on-top desktop window that hosts a small 2D creature which grows, reacts, and forms a personality based on the user's task behavior. Users create and complete quests with difficulty and urgency ratings; completing tasks grants XP and growth points that shape the pet's traits and unlock new animations and behaviors. The system tracks streaks and urgency, provides XP bonuses, and offers a stat allocation system for personality development.

Unity was chosen as the primary engine because it streamlines 2D sprite workflows, provides a mature animation system, and scales easily to other platforms if desired later. Using Unity and C# allows the QuestPet team to move animation, input, UI, and rendering into a single well-supported environment while leveraging Addressables for efficient asset management, the 2D Animation package for expressive sprite work, and the Unity Test Framework for maintainability. For persistence, QuestPet starts with JSON-based saves for fast prototyping and can migrate to an embedded SQLite or LiteDB backend for reliability and structured queries. This stack balances rapid iteration with a clear upgrade path toward robustness, cross-platform reach, and optional cloud features like remote saves and analytics. The result is a highly visual, responsive, and extensible foundation for a playful productivity companion.