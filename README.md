# Tic-Tac-Toe with AI

This is a simple command-line Tic-Tac-Toe game where a human player competes against an AI player. The AI uses the Negamax algorithm for decision-making, powered by the `easyAI` library in Python.

## Features
- Human vs. AI gameplay
- AI powered by the Negamax algorithm
- Simple 3x3 grid interface
- Win, lose, or draw detection

## How to Play
- Players take turns choosing a cell (1-9) on the grid to place their symbol.
- The first player to align 3 symbols horizontally, vertically, or diagonally wins.
- If all cells are filled and no one wins, the game ends in a draw.

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/tictactoe-ai.git
    ```
2. Install the `easyAI` library:
    ```bash
    pip install easyAI
    ```
3. Run the game:
    ```bash
    python tictactoe.py
    ```

## Controls
- Human player inputs a number (1-9) to select a move.
- AI automatically makes its move after the human player's turn.

## AI Algorithm
The AI uses the **Negamax algorithm** to calculate the best possible move, ensuring competitive gameplay.
