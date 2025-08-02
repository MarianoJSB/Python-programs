import csv
import pandas as pd

file = pd.read_csv("notes.csv")

total_average = file["Average"].describe().loc["mean"]

print(file)
print(f"General average: {total_average}")