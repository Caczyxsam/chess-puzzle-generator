import chess
import fetcher
import random
import chess.svg
from IPython.display import display

seed = random.randint(0,1000)

Fen = fetcher.puzzles_df.iloc[seed]["FEN"]
rating = fetcher.puzzles_df.iloc[seed]["Rating"]

board = chess.Board(Fen)

#print(f"The puzzle is rated {rating}")

board_svg = chess.svg.board(board, size=400)

with open("chessboard.svg", "w") as f:
    f.write(board_svg)

right_moves = fetcher.puzzles_df.iloc[seed]["Moves"]

#print(right_moves)

#Taustakuva


import tkinter as tk

root = tk.Tk()
root.title("Chess Puzzle Generator")
icon = tk.PhotoImage(file="src\chess_puzzle_solver_logo.png")
root.iconphoto(True, icon)

canvas = tk.Canvas(root, width=800, height=800, bg="white")
canvas.pack()
root.mainloop()