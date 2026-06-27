import pandas as pd

puzzles_csv = ("data\puzzledata.csv")
puzzles_df = pd.read_csv(puzzles_csv, skipinitialspace=True)

rating = puzzles_df[]

print(puzzles_df.iloc[0]["FEN"])