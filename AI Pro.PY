import tkinter as tk

board = [[' ' for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
player = 'X'
ai = 'O'

def check_winner(b):
    for row in b:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if b[0][col] == b[1][col] == b[2][col] != ' ':
            return b[0][col]
    if b[0][0] == b[1][1] == b[2][2] != ' ':
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != ' ':
        return b[0][2]
    return None

def is_full(b):
    return all(cell != ' ' for row in b for cell in row)


def minimax(b, is_maximizing):
    winner = check_winner(b)
    if winner == ai:
        return 1
    elif winner == player:
        return -1
    elif is_full(b):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if b[i][j] == ' ':
                    b[i][j] = ai
                    score = minimax(b, False)
                    b[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if b[i][j] == ' ':
                    b[i][j] = player
                    score = minimax(b, True)
                    b[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = ai
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        i, j = move
        board[i][j] = ai
        buttons[i][j].config(text=ai, state="disabled")
        if check_winner(board) or is_full(board):
            end_game()


def player_move(i, j):
    if board[i][j] == ' ':
        board[i][j] = player
        buttons[i][j].config(text=player, state="disabled")
        if check_winner(board) or is_full(board):
            end_game()
        else:
            ai_move()


def end_game():
    winner = check_winner(board)
    msg = "It's a draw!" if not winner else f"{winner} wins!"
    result_label.config(text=msg)
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state="disabled")

# FRONT
root = tk.Tk()
root.title("Tic Tac Toe - Minimax AI")

result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.grid(row=3, column=0, columnspan=3)

for i in range(3):
    for j in range(3):
        button = tk.Button(root, text=' ', font=('normal', 40), width=5, height=2,
                           command=lambda i=i, j=j: player_move(i, j))
        button.grid(row=i, column=j)
        buttons[i][j] = button

root.mainloop()
