# 🔢 Number Guessing Game (Zahlen Ratespiel)

A simple console-based number guessing game written in Python.

**Please note: The game's interface and all prompts are entirely in German.**

---

## 🌟 Features

* **Simple Gameplay:** Try to guess a random number between 1 and 10.
* **Immediate Feedback:** Get instant notification if your guess is correct or incorrect.
* **Replay Option:** Easily choose to play again after an attempt.
* **Colored Output:** Uses ANSI escape codes to highlight the correct number in blue after a failed attempt (visible in most modern terminals).

---

## 🚀 Getting Started

### Prerequisites

You only need **Python 3** installed on your system. No external libraries are required as it only uses the built-in `random` module.

### Installation and Running

1.  **Clone the repository** (or save the code above as a Python file, e.g., `guess_game.py`).
2.  **Navigate to the directory** where you saved the file.
3.  **Run the script** from your terminal:

    ```bash
    python guess_game.py
    ```

---

## 🎮 How to Play (in German)

1.  The game will prompt you to guess a number: `Rate eine Zahl zwischen 1 und 10: ` (Guess a number between 1 and 10).
2.  Enter your guess and press Enter.
3.  **If correct:** You win! (`Richtig! 🎉`) and the game ends.
4.  **If incorrect:** The correct number is revealed, and you are asked if you want to play again: `Erneut Versuchen? [y|n]: ` (Try again? [y|n]).
    * Enter `y` to start a new round with a new random number.
    * Enter `n` to quit the game (`Das Spiel wird beendet.`).
