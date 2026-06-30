import chess
import fetcher
import random
from IPython.display import display
import tkinter as tk

seed = random.randint(0,1000)

#####The fetched data we meed#####
Fen = fetcher.puzzles_df.iloc[seed]["FEN"]
rating = fetcher.puzzles_df.iloc[seed]["Rating"]
right_moves = fetcher.puzzles_df.iloc[seed]["Moves"]
turn = (Fen.split(" "))[1]

#####FEN to usable data#####

position = Fen.split(" ")[0].split("/")
print(position)

# Each row into its own list. The result is list of lists, where the order starts from above from white's POW.
all_rows = []
number = 0
for j in position:
    current_row = list(position[number])
    current_row_ready = []
    
    for i in current_row:
        if i.isdigit() :
            current_row_ready += [" "] * int(i)  
        elif i == "P":
            current_row_ready.append("white_pawn")
        elif i == "p":
            current_row_ready.append("black_pawn")
        elif i == "N":
            current_row_ready.append("white_knight")
        elif i == "n":
            current_row_ready.append("black_knight")
        elif i == "B":
            current_row_ready.append("white_bishop")
        elif i == "b":
            current_row_ready.append("black_bishop")
        elif i == "R":
            current_row_ready.append("white_rook")
        elif i == "r":
            current_row_ready.append("black_rook")
        elif i == "Q":
            current_row_ready.append("white_queen")
        elif i == "q":
            current_row_ready.append("black_queen")
        elif i == "K":
            current_row_ready.append("white_king")
        elif i == "k":
            current_row_ready.append("black_king")
    number += 1
    all_rows.append(current_row_ready)



#####Taustakuva#####

#Name and logo for the window
root = tk.Tk()
root.title("Chess Puzzle Generator")
icon = tk.PhotoImage(file="src/chess_puzzle_solver_logo.png")
root.iconphoto(True, icon)

#Creating the background canvas
canvas = tk.Canvas(root, width=800, height=800, bg="white")
canvas.pack()

#Board on canvas
'''TODO'''

#root.mainloop()