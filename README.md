**Rock Paper Scissors – Pygame**

A simple Rock Paper Scissors game built with Python and Pygame where the player competes against the computer. The game includes a graphical interface, score tracking, and a reset system after winning.

<img width="472" height="679" alt="Screenshot 2026-02-23 at 10 55 36 PM" src="https://github.com/user-attachments/assets/39401f73-12e9-4d53-b397-e1fe48291edf" />
<img width="467" height="678" alt="Screenshot 2026-02-23 at 10 55 18 PM" src="https://github.com/user-attachments/assets/b6ebe9e3-507a-47aa-9d83-141e8b673336" />
<img width="466" height="678" alt="Screenshot 2026-02-23 at 10 55 04 PM" src="https://github.com/user-attachments/assets/88d3fe20-9645-4d8a-af51-93e241ce0d8a" />

**Features:**

Interactive GUI built with Pygame

Player vs Computer gameplay

Random computer choices

Score tracking (first to 3 wins)

Game Over screen

Reset button to start a new game

Custom images and fonts

**Rock-Paper-scissors**
│
├── Test.py          # Main game file
├── Button.py        # Reset button class
├── Papers.py        # Paper object
├── Rocks.py         # Rock object
├── Scissors.py      # Scissors object
└── assets/          # Images, fonts, background

**How to Run the Game**

1. Install pygame:

pip install pygame

2. Run the main file:

python Test.py

**Program Flow:**
Game starts 
↓
Window, images, and fonts load
↓
Player clicks Rock / Paper / Scissors
↓
Computer randomly selects an option
↓
Program compares choices
↓
Winner is decided and score updates
↓
If score reaches 3
↓
Gameover() runs
↓
Reset button appears
↓
Player clicks Reset
↓
GameReset() runs
↓
Score resets and game restarts

