import pandas as pd

puzzles_csv = (r"C:\Users\samue\Downloads\lichess_db_puzzle.csv")
puzzles_df = pd.read_csv(puzzles_csv)

print(puzzles_df.head(10))