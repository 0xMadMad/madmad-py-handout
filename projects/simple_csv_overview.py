import pandas as pd

df = pd.read_csv("data.csv")

print("mean: ", df.mean(numeric_only=True))
print("min: ", df.min(numeric_only=True))
print("max: ", df.max(numeric_only=True))
#MadMad_8