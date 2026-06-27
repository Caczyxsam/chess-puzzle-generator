import pandas as pd

puzzles_csv = ("data\puzzledata.csv")
puzzles_df = pd.read_csv(puzzles_csv)

print(puzzles_df.head(20))