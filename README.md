# Tic Tac Toe with AI

A command-line **Tic Tac Toe** game in Python where you play against a computer opponent. The hard mode uses the **Minimax algorithm**, which makes the AI **unbeatable**: the best a human can do is draw.

## Features
- Play as X against the computer (O)
- **Easy mode**: computer plays random moves
- **Unbeatable mode**: computer looks at every possible future move using Minimax
- Input validation, scoreboard and replay option

## How the AI works
Minimax tries every possible sequence of moves until the game ends and scores each result:
- AI wins: positive score, human wins: negative score, draw: 0
- The AI chooses the move that leads to the best guaranteed outcome
- A depth penalty makes the AI prefer faster wins

## Tools
Python 3 (no extra libraries needed)

## How to run
```bash
python tic_tac_toe.py
```
Enter a number from 1 to 9 to place your X:
```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

## What I learned
Game logic, recursion, the Minimax algorithm, and how a simple AI makes decisions.

## Ideas to improve
Add Alpha-Beta pruning, a graphical interface (Pygame / Tkinter), or let the player choose to go second.
