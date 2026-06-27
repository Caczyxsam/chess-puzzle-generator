import chess
import fetcher
import random
import chess.svg
from IPython.display import display
import tkinter as tk

seed = random.randint(0,1000)

#####The fetched data we meed#####
Fen = fetcher.puzzles_df.iloc[seed]["FEN"]
rating = fetcher.puzzles_df.iloc[seed]["Rating"]
right_moves = fetcher.puzzles_df.iloc[seed]["Moves"]

#####Taustakuva#####

#The board
board = chess.Board(Fen)
board_svg = chess.svg.board(board, size=400)

with open("chessboard.svg", "w") as f:
    f.write(board_svg)

#Name and logo for the window
root = tk.Tk()
root.title("Chess Puzzle Generator")
icon = tk.PhotoImage(file="src\chess_puzzle_solver_logo.png")
root.iconphoto(True, icon)

#Creating the background canvas
canvas = tk.Canvas(root, width=800, height=800, bg="white")
canvas.pack()

#Board on canvas
'''TODO'''

root.mainloop()