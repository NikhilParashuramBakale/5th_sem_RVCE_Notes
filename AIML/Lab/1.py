# # tic_tac_toe_minimax.py
# import math

# # Board is a list of 9 cells: 'X', 'O', or ' ' (space for empty)
# def print_board(board):
#     print()
#     for row in range(3):
#         r = board[row*3:(row+1)*3]
#         print(" " + " | ".join(r))
#         if row < 2:
#             print("---+---+---")
#     print()

# def available_moves(board):
#     return [i for i, v in enumerate(board) if v == ' ']

# def is_full(board):
#     return ' ' not in board

# def check_winner(board):
#     # returns 'X' or 'O' if there's a winner, or None otherwise
#     wins = [
#         (0,1,2), (3,4,5), (6,7,8),  # rows
#         (0,3,6), (1,4,7), (2,5,8),  # cols
#         (0,4,8), (2,4,6)            # diagonals
#     ]
#     for a,b,c in wins:
#         if board[a] == board[b] == board[c] and board[a] != ' ':
#             return board[a]
#     return None

# def game_over(board):
#     winner = check_winner(board)
#     if winner:
#         return True, winner
#     if is_full(board):
#         return True, None  # draw
#     return False, None

# # MINIMAX
# # We'll make AI = 'O' (maximizer) and Human = 'X' (minimizer).
# def minimax(board, is_maximizing):
#     over, winner = game_over(board)
#     if over:
#         if winner == 'O':
#             return 1  # AI win
#         elif winner == 'X':
#             return -1 # Human win
#         else:
#             return 0  # draw

#     if is_maximizing:
#         best_score = -math.inf
#         for move in available_moves(board):
#             board[move] = 'O'
#             score = minimax(board, False)
#             board[move] = ' '
#             if score > best_score:
#                 best_score = score
#         return best_score
#     else:
#         best_score = math.inf
#         for move in available_moves(board):
#             board[move] = 'X'
#             score = minimax(board, True)
#             board[move] = ' '
#             if score < best_score:
#                 best_score = score
#         return best_score

# def best_move(board):
#     best_score = -math.inf
#     move_choice = None
#     for move in available_moves(board):
#         board[move] = 'O'
#         score = minimax(board, False)
#         board[move] = ' '
#         if score > best_score:
#             best_score = score
#             move_choice = move
#     return move_choice

# def human_move(board):
#     moves = available_moves(board)
#     while True:
#         try:
#             user = int(input(f"Enter your move (0-8). Available: {moves}\n> "))
#             if user in moves:
#                 return user
#             else:
#                 print("Invalid move. Choose an empty cell index from the list.")
#         except ValueError:
#             print("Please input a number from 0 to 8.")

# def main():
#     board = [' '] * 9
#     print("Tic-Tac-Toe: You are X, computer is O.")
#     print("Board positions are numbered 0..8 like this:")
#     print(" 0 | 1 | 2\n---+---+---\n 3 | 4 | 5\n---+---+---\n 6 | 7 | 8")
#     print_board(board)

#     # Let human start. You can swap who starts or implement choice.
#     current_player = 'X'

#     while True:
#         if current_player == 'X':
#             mv = human_move(board)
#             board[mv] = 'X'
#         else:
#             print("Computer is thinking...")
#             mv = best_move(board)
#             # best_move should never be None unless game over; guard anyway
#             if mv is None:
#                 mv = available_moves(board)[0]
#             board[mv] = 'O'
#             print(f"Computer played at position {mv}.")

#         print_board(board)
#         over, winner = game_over(board)
#         if over:
#             if winner == 'X':
#                 print("You win! 🎉")
#             elif winner == 'O':
#                 print("Computer wins. Better luck next time.")
#             else:
#                 print("It's a draw.")
#             break

#         current_player = 'O' if current_player == 'X' else 'X'

# if __name__ == "__main__":
#     main()
# def print_board(board): 
#     for row in board: 
#         print(" ".join(row)) 
 
# def is_winner(board, player): 
#     # Check rows, columns, and diagonals 
#     for i in range(3): 
#         if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):  
#              return True 
#     if all(board[i][i] == player for i in range(3)) or  all(board[i][2 - i] == player for i in range(3)): 
#         return True 
#     return False 
 
# def is_full(board): 
#     return all(board[i][j] != ' ' for i in range(3) for j in range(3)) 
 
# def is_game_over(board): 
#     return is_winner(board, 'X') or is_winner(board, 'O') or is_full(board) 
 
# def minimax(board, depth, maximizing_player): 
#     if is_winner(board, 'X'): 
#         return -1 
#     elif is_winner(board, 'O'): 
#         return 1 
#     elif is_full(board): 
#         return 0 
 
#     if maximizing_player: 
#         max_eval = float('-inf') 
#         for i in range(3): 
#             for j in range(3): 
#                 if board[i][j] == ' ': 
#                     board[i][j] = 'O' 
#                     eval = minimax(board, depth + 1, False) 
#                     board[i][j] = ' ' 
#                     max_eval = max(max_eval, eval) 
#         return max_eval 
#     else: 
#         min_eval = float('inf') 
#         for i in range(3): 
#             for j in range(3): 
#                 if board[i][j] == ' ': 
#                     board[i][j] = 'X' 
#                     eval = minimax(board, depth + 1, True) 
#                     board[i][j] = ' ' 
#                     min_eval = min(min_eval, eval) 
#         return min_eval 
 
# def get_best_move(board): 
#     best_move = None 
#     best_eval = float('-inf') 
#     for i in range(3): 
#         for j in range(3): 
#             if board[i][j] == ' ': 
#                 board[i][j] = 'O' 
#                 eval = minimax(board, 0, False) 
#                 board[i][j] = ' ' 
#                 if eval > best_eval: 
#                     best_eval = eval 
#                     best_move = (i, j) 
#     return best_move 
 
# def play_game(): 
#     board = [[' ' for _ in range(3)] for _ in range(3)] 
#     current_player = 'X' 
 
#     while not is_game_over(board): 
#         print_board(board) 
 
#         if current_player == 'X': 
#             row, col = map(int, input("Enter your move (row and column separated by space): ").split()) 
#             if board[row][col] == ' ': 
#                 board[row][col] = 'X' 
#                 current_player = 'O' 
#             else: 
#                 print("Invalid move. Try again.") 
#         else: 
#             print("AI is thinking...") 
#             move = get_best_move(board) 
#             board[move[0]][move[1]] = 'O' 
#             current_player = 'X' 
 
#     print_board(board) 
 
#     if is_winner(board, 'X'): 
#         print("You win!") 
#     elif is_winner(board, 'O'): 
#         print("AI wins!") 
#     else: 
#         print("It's a draw!") 
 
# if __name__ == "__main__": 
#     play_game() 
import math

# ---------- BOARD DISPLAY ----------
def print_board(board):
    print("\nCurrent Board:")
    for i in range(3):
        print(" " + " | ".join(board[i]))
        if i < 2:
            print("---+---+---")
    print()

# ---------- GAME STATE CHECKS ----------
def is_winner(board, player):
    # Rows and Columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True

    # Diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def game_over(board):
    return is_winner(board, 'X') or is_winner(board, 'O') or is_full(board)

# ---------- MINIMAX WITH ALPHA-BETA ----------
def minimax(board, depth, alpha, beta, is_maximizing):
    if is_winner(board, 'O'):
        return 10 - depth
    if is_winner(board, 'X'):
        return -10 + depth
    if is_full(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    value = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = ' '
                    best = max(best, value)
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        return best  # Prune
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    value = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = ' '
                    best = min(best, value)
                    beta = min(beta, best)
                    if beta <= alpha:
                        return best  # Prune
        return best

# ---------- AI MOVE ----------
def best_move(board):
    best_val = -math.inf
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

# ---------- GAME LOOP ----------
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("TIC TAC TOE (You = X | AI = O)")
    print("Enter row and column (0–2)\n")

    while not game_over(board):
        print_board(board)

        # Human move
        row, col = map(int, input("Your move (row col): ").split())
        if board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        board[row][col] = 'X'

        if game_over(board):
            break

        # AI move
        print("AI is thinking...")
        r, c = best_move(board)
        board[r][c] = 'O'

    print_board(board)
    if is_winner(board, 'X'):
        print("🎉 You win!")
    elif is_winner(board, 'O'):
        print("🤖 AI wins!")
    else:
        print("🤝 It's a draw!")

if __name__ == "__main__":
    play_game()
