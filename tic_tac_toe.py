"""Tic Tac Toe with an AI opponent
You play as X. The computer plays as O.
  - Easy mode: the computer picks random moves.
  - Unbeatable mode: the computer uses the MINIMAX algorithm, so the best
    you can ever do is draw.
"""
import random

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]
HUMAN, AI = "X", "O"


def print_board(board):
    """Show the board. Empty cells display their number (1-9)."""
    cells = [board[i] if board[i] != " " else str(i + 1) for i in range(9)]
    print()
    print(f" {cells[0]} | {cells[1]} | {cells[2]}")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]}")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]}")
    print()


def get_winner(board):
    """Return 'X' or 'O' if someone has won, otherwise None."""
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def free_cells(board):
    return [i for i in range(9) if board[i] == " "]


def minimax(board, ai_turn, depth):
    """Score a position from the AI's point of view.
    +10 (minus depth) = AI wins, -10 (plus depth) = human wins, 0 = draw.
    Depth is used so the AI prefers quicker wins and slower losses."""
    winner = get_winner(board)
    if winner == AI:
        return 10 - depth
    if winner == HUMAN:
        return depth - 10
    if not free_cells(board):
        return 0

    if ai_turn:                              # AI tries to MAXIMISE the score
        best = -100
        for move in free_cells(board):
            board[move] = AI
            best = max(best, minimax(board, False, depth + 1))
            board[move] = " "
        return best
    else:                                    # Human tries to MINIMISE the score
        best = 100
        for move in free_cells(board):
            board[move] = HUMAN
            best = min(best, minimax(board, True, depth + 1))
            board[move] = " "
        return best


def best_ai_move(board):
    """Try every free cell and pick the one with the highest minimax score."""
    best_score, best_move = -100, None
    for move in free_cells(board):
        board[move] = AI
        score = minimax(board, False, 1)
        board[move] = " "
        if score > best_score:
            best_score, best_move = score, move
    return best_move


def random_ai_move(board):
    return random.choice(free_cells(board))


def get_human_move(board):
    while True:
        choice = input("Your move (1-9): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= 9 and board[int(choice) - 1] == " ":
            return int(choice) - 1
        print("Invalid move. Choose an empty cell from 1 to 9.")


def play_round(unbeatable):
    board = [" "] * 9
    human_turn = True
    print_board(board)

    while True:
        if human_turn:
            board[get_human_move(board)] = HUMAN
        else:
            move = best_ai_move(board) if unbeatable else random_ai_move(board)
            board[move] = AI
            print(f"Computer plays {move + 1}")
        print_board(board)

        winner = get_winner(board)
        if winner:
            return winner
        if not free_cells(board):
            return "draw"
        human_turn = not human_turn


def main():
    print("=== TIC TAC TOE: You (X) vs Computer (O) ===")
    mode = input("Choose mode: 1 = Easy, 2 = Unbeatable AI: ").strip()
    unbeatable = mode != "1"
    score = {"you": 0, "computer": 0, "draw": 0}

    while True:
        result = play_round(unbeatable)
        if result == HUMAN:
            print("You win! 🎉")
            score["you"] += 1
        elif result == AI:
            print("Computer wins!")
            score["computer"] += 1
        else:
            print("It's a draw.")
            score["draw"] += 1
        print(f"Score -> You: {score['you']} | Computer: {score['computer']} | Draws: {score['draw']}")

        if input("Play again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
