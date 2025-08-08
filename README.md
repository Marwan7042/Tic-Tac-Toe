🧠 Tic Tac Toe AI
Video Demo: Coming soon (optional, insert YouTube link if available)

Description
This project is an AI-powered implementation of the classic game Tic Tac Toe, developed in Python. The focus isn't just on making the game playable — it's about making the AI unbeatable.


Here’s what that means for you:

❌ You cannot win.
🤝 If you play optimally, you'll force a tie.
✅ If you slip up even once, you lose.


How It Works
Initial State:
The board starts as a 3x3 grid of empty spaces. X always plays first.

Player Logic:
The program alternates between X and O, determining the current player based on the number of remaining moves.

Valid Actions:
The AI generates a list of all valid positions on the board.

Minimax Algorithm:

Recursively simulates every possible future move.

Maximizes the score if it’s the AI’s turn, and minimizes it if it’s the opponent’s.

Prunes decisions that lead to worse outcomes.

Always selects the best move.

Game Over:
The game ends when a player wins or all cells are filled (draw). The result is printed clearly.

My Role
This project was developed as part of CS50’s Introduction to Artificial Intelligence with Python, specifically for the “Tic Tac Toe” unit.

I implemented the full logic, including:

Turn handling

Game state management

Win/draw detection

Optimal move selection via Minimax

Helper functions for simulation and scoring

All code is written in pure Python with no external libraries.

Results
The AI never loses. Here’s what happens based on how you play:

Your Strategy	Result
Random/Imperfect	❌ You lose
Perfect Play	🤝 Tie
Try to Trick AI	❌ Still lose

How to play.

first, open up your terminal window.

then, run 'python3 -r requirements.txt', and finally run 'python3 runner.py'

that will open the GUI, then try to win.
