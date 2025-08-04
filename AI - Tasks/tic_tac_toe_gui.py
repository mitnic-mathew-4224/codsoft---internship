import tkinter as tk
from tkinter import messagebox
import copy

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe AI")
root.resizable(False, False)

# Game variables
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
player = "X"
ai = "O"

# Check if there are moves left
def is_moves_left(b):
    for row in b:
        if "" in row:
            return True
    return False

# Evaluate score
def evaluate(b):
    # Rows, Columns, Diagonals
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != "":
            return 10 if b[i][0] == ai else -10
        if b[0][i] == b[1][i] == b[2][i] != "":
            return 10 if b[0][i] == ai else -10

    if b[0][0] == b[1][1] == b[2][2] != "":
        return 10 if b[0][0] == ai else -10
    if b[0][2] == b[1][1] == b[2][0] != "":
        return 10 if b[0][2] == ai else -10

    return 0

# Minimax Algorithm
def minimax(b, depth, is_max):
    score = evaluate(b)

    if score == 10 or score == -10:
        return score

    if not is_moves_left(b):
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if b[i][j] == "":
                    b[i][j] = ai
                    best = max(best, minimax(b, depth + 1, False))
                    b[i][j] = ""
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if b[i][j] == "":
                    b[i][j] = player
                    best = min(best, minimax(b, depth + 1, True))
                    b[i][j] = ""
        return best

# Find best move for AI
def find_best_move(b):
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if b[i][j] == "":
                b[i][j] = ai
                move_val = minimax(b, 0, False)
                b[i][j] = ""
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Check win/draw and show message
def check_game_over():
    score = evaluate(board)
    if score == 10:
        messagebox.showinfo("Game Over", "AI Wins :(")
        reset_board()
        return True
    elif score == -10:
        messagebox.showinfo("Game Over", "You Win :)")
        reset_board()
        return True
    elif not is_moves_left(board):
        messagebox.showinfo("Game Over", "Draw ~_~ ")
        reset_board()
        return True
    return False

# When a button is clicked
def on_click(i, j):
    if board[i][j] == "":
        board[i][j] = player
        buttons[i][j].config(text=player, state="disabled")
        if not check_game_over():
            ai_move()

# AI makes a move
def ai_move():
    i, j = find_best_move(copy.deepcopy(board))
    if i != -1 and j != -1:
        board[i][j] = ai
        buttons[i][j].config(text=ai, state="disabled")
        check_game_over()

# Reset the board
def reset_board():
    global board
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")

# Create buttons for grid
for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text="", font=('Helvetica', 20), width=5, height=2,
                        command=lambda i=i, j=j: on_click(i, j))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

root.mainloop()

