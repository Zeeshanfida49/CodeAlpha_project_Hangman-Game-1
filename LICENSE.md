# 🕹️ Hangman Game (Python Console Version)

This is a simple **text-based Hangman game** implemented in Python. The player has to guess a randomly selected word one letter at a time. The player can make up to 6 incorrect guesses before the game ends.

## 🎯 Features

- Predefined list of words to guess from.
- Random word selection on each run.
- Input validation (only single alphabetic characters are allowed).
- Tracks and displays guessed letters.
- Shows remaining tries.
- Simple and interactive console-based UI.

## 🧠 How the Game Works

- The game randomly selects a word from a predefined list.
- The player must guess the word one letter at a time.
- If the letter is in the word, it is revealed in the correct position(s).
- If the letter is not in the word, the number of remaining tries decreases.
- The game ends when:
  - The player correctly guesses the entire word, or
  - The player runs out of tries (maximum of 6 incorrect guesses).

## 💻 Technologies Used

- Python 3
- Built-in libraries: `random`

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/hangman-game.git
cd hangman-game
2. Run the Game
Make sure Python 3 is installed on your system.

bash
Copy
Edit
python hangman.py
3. Play the Game
Follow the prompts in the terminal to guess letters and solve the hidden word.

📂 File Structure
bash
Copy
Edit
hangman-game/
├── hangman.py   # Main game script
└── README.md    # Project description
✍️ Author
Your Name – GitHub Profile

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

yaml
Copy
Edit

---

✅ **How to Use**:
1. Replace `yourusername` and `Your Name` with your actual GitHub username and name.
2. Save this content as `README.md` in the same directory as your `hangman.py` file.

Let me know if you'd like help uploading to GitHub or turning this into a GUI or web version!
