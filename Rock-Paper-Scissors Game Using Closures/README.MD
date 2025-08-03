# 🪨 Rock-Paper-Scissors Game (Python Closure Version)

This is a command-line implementation of the classic **Rock-Paper-Scissors** game, written in Python using **closures** to maintain game state (score, rounds) without global variables.

The player competes against the computer in as many rounds as they choose. The game keeps track of wins, losses, and ties until the user exits.

---

## ✅ Features

- Built with pure Python (no external libraries except `random`)
- Uses **closures** and `nonlocal` variables to manage game state
- Validates user input (accepts only 1, 2, 3, or 0)
- Displays running score after each round
- Gracefully exits and displays total results

---

## 🎮 How to Play

1. Run the script:
   ```bash
   python rock_paper_scissors.py

