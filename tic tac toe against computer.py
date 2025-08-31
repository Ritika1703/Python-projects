import tkinter as tk
import random

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []
current_player = "X"   # Human always starts

def check_winner():
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b,c in wins:
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            return True
    return False

def computer_move():
    empty = [i for i in range(9) if buttons[i]["text"] == ""]
    if empty:
        choice = random.choice(empty)
        buttons[choice]["text"] = "O"
        if check_winner():
            status["text"] = "Computer Wins!"
        elif all(btn["text"] != "" for btn in buttons):
            status["text"] = "Draw!"
        else:
            status["text"] = "Your Turn (X)"

def clicked(i):
    if buttons[i]["text"] == "" and status["text"].startswith("Your"):
        buttons[i]["text"] = "X"
        if check_winner():
            status["text"] = "You Win!"
        elif all(btn["text"] != "" for btn in buttons):
            status["text"] = "Draw!"
        else:
            status["text"] = "Computer's Turn..."
            root.after(500, computer_move)  # delay for realism

def reset():
    for btn in buttons:
        btn["text"] = ""
    status["text"] = "Your Turn (X)"

# Make board
for i in range(9):
    btn = tk.Button(root, text="", width=6, height=3,
                    font=("Arial", 20), command=lambda i=i: clicked(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

status = tk.Label(root, text="Your Turn (X)", font=("Arial", 14))
status.grid(row=3, column=0, columnspan=3)

reset_btn = tk.Button(root, text="Reset", command=reset)
reset_btn.grid(row=4, column=0, columnspan=3)

root.mainloop()
