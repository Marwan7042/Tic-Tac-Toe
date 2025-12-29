# Tic Tac Toe AI

An unbeatable implementation of Tic Tac Toe developed in Python, featuring an AI opponent powered by the Minimax algorithm.

## Overview

This project demonstrates optimal game-playing AI through a classic Tic Tac Toe implementation. The AI is designed to never lose—at best, a perfectly-played human opponent will achieve a draw.

## Features

- **Unbeatable AI**: Uses the Minimax algorithm to evaluate all possible game states and select optimal moves
- **Turn Management**: Automatically alternates between human (X) and AI (O) players
- **Game State Validation**: Checks for valid moves, win conditions, and draw states
- **GUI Interface**: Interactive graphical interface for gameplay
- **Pure Python**: No external dependencies beyond the GUI framework

## How the AI Works

The AI uses the **Minimax algorithm** to determine optimal moves:

1. **Game Tree Exploration**: Recursively simulates all possible future moves from the current board state
2. **Score Evaluation**: Assigns scores to terminal states (win, loss, draw)
3. **Minimax Logic**: Maximizes the AI's score while minimizing the opponent's
4. **Move Selection**: Returns the move that produces the best outcome

This exhaustive approach ensures the AI always makes the optimal play.

## Technical Implementation

- **Turn Handling**: Determines current player based on remaining moves
- **Move Validation**: Generates list of available positions
- **State Management**: Tracks board configuration and game progress
- **Win Detection**: Evaluates all winning combinations
- **Helper Functions**: Utilities for board simulation and score calculation

## Installation & Usage

### Requirements

- Python 3.x

### Setup

```bash
pip install -r requirements.txt
```

### Running the Game

```bash
python3 runner.py
```

This launches the GUI interface where you can play against the AI. You control X (first move), and the AI plays as O.

## Expected Outcomes

- **Perfect Play**: Results in a draw
- **Suboptimal Play**: Results in a loss for the human player

## Project Context

Developed as part of CS50's Introduction to Artificial Intelligence with Python, specifically for the "Tic Tac Toe" unit. All code is written in pure Python.
first, open up your terminal window.

then, run 'pip install -r requirements.txt', and finally run 'python3 runner.py'

that will open the GUI, then try to win.


