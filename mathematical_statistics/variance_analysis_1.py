import math

import pandas as pd

df = pd.DataFrame(
    [[32.3, 34.0, 34.3, 35.0, 36.5],
     [33.3, 33.0, 36.3, 36.8, 34.5],
     [30.8, 34.3, 35.3, 32.3, 35.8],
     [29.3, 26.0, 29.8, 28.0, 29.8]])
print(df)

S_T = 0
for i in range(4):
    for j in range(5):
        S_T += math.pow(df.iloc[i, j] - df.mean().mean(), 2)
print(f"S_T: {S_T}")

S_A = 0
for i in range(4):
    for j in range(5):
        S_A += math.pow(df.iloc[i, :].mean() - df.mean().mean(), 2)
print(f"S_A: {S_A}")

S_E = 0
for i in range(4):
    for j in range(5):
        S_E += math.pow(df.iloc[i, j] - df.iloc[i, :].mean(), 2)
print(f"S_E: {S_E}")
