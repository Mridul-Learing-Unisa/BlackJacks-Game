# 🎲 Blackjack Dice Game

**Author**: Mridul Chopra  
**Email**: chomy077@mymail.unisa.edu.au  

---

## 📝 Project Overview

The **Blackjack Dice Game** is an interactive, command-line-based Python application that recreates the classic Blackjack game using dice instead of cards. Players can compete to get as close to 21 as possible without exceeding it. The game supports player statistics, chip management, and a variety of interactive features.

---

## ⚙️ Features

- **Player Management**: 
  - Add new players to the game.
  - Remove existing players.
  - View player statistics (games played, won, lost, drawn, chips, and total score).
  - Search for a specific player by name.
  - Display the player with the highest chip balance.
  - Sort and display all players by chip balance.
  
- **Chip Transactions**:
  - Players can buy chips and manage their balances.
  
- **Game Mechanics**:
  - Dice-based gameplay with blackjack-inspired rules.
  - Track individual game outcomes (won, lost, or drawn).
  - Update player statistics after each game session.

---

## 📂 Project Structure

- `Main.py` - The entry point of the application. Handles the game loop and user interactions.
- `blackjack.py` - Contains all the logic for the Blackjack Dice game.
- `players.txt` - Stores player data (statistics, chips, scores) persistently between game sessions.

---

## 🛠️ Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/blackjack-dice-game.git
    cd blackjack-dice-game
    ```

2. **Ensure `players.txt` exists**:
   The script will attempt to read from `players.txt` for player data. If the file doesn’t exist, the script will create it on the first run.

3. **Run the game**:
    ```bash
    python Main.py
    ```

---

## 🚀 How to Play

1. **Start the game**: Run the `Main.py` script. You'll be presented with a list of available commands.
2. **Available Commands**:
    - `list`: View all registered players and their statistics.
    - `buy`: Buy chips for a specific player.
    - `search`: Search for a player by name.
    - `high`: Display the player with the highest chip balance.
    - `add`: Add a new player to the game.
    - `remove`: Remove an existing player.
    - `play`: Play a round of Blackjack Dice for a player.
    - `chips`: List players sorted by chip balance.
    - `quit`: Exit the game.

3. **Gameplay Example**:
    ```bash
    Please enter choice
    [list, buy, search, high, add, remove, play, chips, quit]: play
    Enter Players Name: John
    Rolling the dice for John...
    Johns total score is: 19
    You won! 🎉
    ```
4. **Winning**: Players win by getting a total score as close to 21 as possible without exceeding it. Dice are rolled to simulate card draws.

---

## 🏅 Example Outputs

### Listing Players:
```bash
===========================================================
-                    Player Summary                       -
===========================================================
-                                P  W  L  D  Chips Score  -
-----------------------------------------------------------
- John Doe                    10  3  4  3   150   20      -
-----------------------------------------------------------
```

## 🔧 Future Improvements

- Add **leaderboards** for player rankings based on win/loss ratios.
- Introduce more **game variations** and betting mechanics.
- Implement a **save/load feature** for game sessions.
- Improve **user interface** for a more engaging experience.

---


### Key Elements:
- **Clear Structure**: Breaks down sections for easy navigation.
- **Visual Flair**: Uses emojis for readability and engagement.
- **Comprehensive Details**: Includes everything from installation to gameplay and future improvements.
- **User-Centered**: Easy-to-follow instructions, sample commands, and outputs make it user-friendly.
