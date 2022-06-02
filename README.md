# Rock-Paper-Scissors

## Description
This GitHub project hosts an expanded version of the classic game Rock-Paper-Scissors. It allows users to play the traditional Rock-Paper-Scissors game and adds the feature to support custom game options beyond the original trio. The game also implements a simple scoring system where the player's score is stored and accessed from a file. This interactive Python application engages players with a console-based interface where they can input their choices, view their current ratings, and dynamically alter the game's options.

## Features

- **User Identification**: Players can enter their name at the beginning, and the game will greet them accordingly.
- **Scoring System**: The game reads and updates the player's score from a file, allowing for persistent score tracking across different game sessions.
- **Custom Gameplay Options**: Players can define their own set of symbols for the game, making it more versatile and interesting than the traditional version.
- **Interactive Commands**: During the game, players can dynamically request their current score or exit the game using simple commands.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/rock-paper-scissors.git
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## How to Play

1. **Start the Game**: Run the script, and when prompted, enter your name to start playing.
2. **Set Custom Options** *(Optional)*: Before the actual game starts, you can enter a custom set of symbols separated by commas. If you prefer the classic version, just press Enter to continue with the default options (rock, paper, scissors).
3. **Playing**: Enter your choice of symbol at each prompt. The game will compare your choice against the computer's random choice and update the score based on the outcome.
4. **Commands**:
   - Type `!exit` to end the game.
   - Type `!rating` to view your current score.
5. **Scoring**: Winning a round awards you 100 points, a draw gives 50 points, and losing yields no points.

## File Structure

- `main.py`: The main game script that you run to start playing.
- `rating.txt`: A text file where player scores are stored and retrieved from.

## License

This project is licensed under the [MIT License](LICENSE.txt).
