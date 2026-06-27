import chess
import fetcher

seed = int(input("Give an integer: "))

Fen = fetcher.puzzles_df.iloc[seed]["FEN"]

board = chess.Board(Fen)

print(board)