import chess
import fetcher
import random

seed = random.randint(0,1000)

Fen = fetcher.puzzles_df.iloc[seed]["FEN"]
rating = fetcher.puzzles_df.iloc[seed]["Rating"]

board = chess.Board(Fen)

print(board)
print(f"The puzzle is rated {rating}")