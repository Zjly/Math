import math

import pandas as pd

df = pd.DataFrame(
    [[325, 292, 316],
     [317, 310, 318],
     [310, 320, 318],
     [330, 370, 365]])
print(df)

S_A = 0
for i in range(df.shape[0]):
    S_A += math.pow(df.iloc[i, :].mean() - df.mean().mean(), 2)
S_A = S_A * df.shape[1]
print(f"S_A: {S_A}")

S_B = 0
for j in range(df.shape[1]):
    S_B += math.pow(df.iloc[:, j].mean() - df.mean().mean(), 2)
S_B = S_B * df.shape[0]
print(f"S_B: {S_B}")

S_T = 0
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        S_T += math.pow(df.iloc[i, j] - df.mean().mean(), 2)
print(f"S_T: {S_T}")

S_E = S_T - S_A - S_B
print(f"S_E: {S_E}")

_S_A = S_A / (df.shape[0] - 1)
print(f"_S_A: {_S_A}")

_S_B = S_B / (df.shape[1] - 1)
print(f"_S_B: {_S_B}")

_S_E = S_E / ((df.shape[0] - 1) * (df.shape[1] - 1))
print(f"_S_E: {_S_E}")

F_A = _S_A / _S_E
print(f"F_A: {F_A}")

F_B = _S_B / _S_E
print(f"F_B: {F_B}")
