# tictactoe_ab.py
import math
from typing import List, Optional, Tuple

# ------- Board helpers -------
def print_board(board: List[str]) -> None:
    print()
    for r in range(3):
        row = board[r*3:(r+1)*3]
        print(" " + " | ".join(row))
        if r < 2:
            print("---+---+---")
    print()

def available_moves(board: List[str]) -> List[int]:
    return [i for i, v in enumerate(board) if v == ' ']

def check_winner(board: List[str]) -> Optional[str]:
    wins = [
        (0,1,2),(3,4,5),(6,7,8),  # rows
        (0,3,6),(1,4,7),(2,5,8),  # cols
        (0,4,8),(2,4,6)           # diagonals
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return None

def game_over(board: List[str]) -> Tuple[bool, Optional[str]]:
    winner = check_winner(board)
    if winner:
        return True, winner
    if ' ' not in board:
        return True, None  # draw
    return False, None

# Simple move ordering: center first, then corners, then edges — helps pruning
MOVE_PRIORITY = {4: 3, 0:2, 2:2, 6:2, 8:2, 1:1, 3:1, 5:1, 7:1}

# ------- Alpha-Beta Minimax -------
# We use depth to prefer faster wins (score magnitude reduced by depth).
# AI is 'O' (maximizer), Human is 'X' (minimizer).
def alphabeta(board: List[str],
              depth: int,
              alpha: float,
              beta: float,
              is_maximizing: bool) -> int:
    over, winner = game_over(board)
    if over:
        if winner == 'O':
            return 10 - depth   # prefer faster wins
        elif winner == 'X':
            return -10 + depth  # prefer slower losses
        else:
            return 0            # draw

    moves = available_moves(board)
    # Order moves by heuristic priority (better ordering -> more pruning)
    moves.sort(key=lambda m: MOVE_PRIORITY.get(m, 0), reverse=True)

    if is_maximizing:
        value = -math.inf
        for mv in moves:
            board[mv] = 'O'
            score = alphabeta(board, depth+1, alpha, beta, False)
            board[mv] = ' '
            if score > value:
                value = score
            if value >= beta:
                # Beta cutoff: maximizing player found a move >= beta,
                # minimizing ancestor will avoid this branch.
                return value
            alpha = max(alpha, value)
        return value
    else:
        value = math.inf
        for mv in moves:
            board[mv] = 'X'
            score = alphabeta(board, depth+1, alpha, beta, True)
            board[mv] = ' '
            if score < value:
                value = score
            if value <= alpha:
                # Alpha cutoff: minimizing player found move <= alpha,
                # maximizing ancestor will avoid this branch.
                return value
            beta = min(beta, value)
        return value

def best_move(board: List[str]) -> Optional[int]:
    best_val = -math.inf
    choice = None
    moves = available_moves(board)
    moves.sort(key=lambda m: MOVE_PRIORITY.get(m,0), reverse=True)
    for mv in moves:
        board[mv] = 'O'
        val = alphabeta(board, depth=0, alpha=-math.inf, beta=math.inf, is_maximizing=False)
        board[mv] = ' '
        if val > best_val:
            best_val = val
            choice = mv
    return choice

# ------- Game loop (console) -------
def human_move(board: List[str]) -> int:
    moves = available_moves(board)
    while True:
        try:
            user = int(input(f"Enter your move (0-8). Available: {moves}\n> "))
            if user in moves:
                return user
            print("Invalid move. Pick an available index.")
        except ValueError:
            print("Enter a number 0-8.")

def main():
    board = [' '] * 9
    print("Tic-Tac-Toe with Alpha-Beta pruning. You = X, Computer = O")
    print("Positions: 0 1 2\n           3 4 5\n           6 7 8")
    print_board(board)

    current = 'X'  # human starts; change to 'O' if you want AI to start
    while True:
        if current == 'X':
            mv = human_move(board)
            board[mv] = 'X'
        else:
            print("Computer thinking...")
            mv = best_move(board)
            if mv is None:
                mv = available_moves(board)[0]  # fallback
            board[mv] = 'O'
            print(f"Computer played {mv}")

        print_board(board)
        over, winner = game_over(board)
        if over:
            if winner == 'X':
                print("You win!")
            elif winner == 'O':
                print("Computer wins.")
            else:
                print("Draw.")
            break

        current = 'O' if current == 'X' else 'X'

if __name__ == "__main__":
    main()
