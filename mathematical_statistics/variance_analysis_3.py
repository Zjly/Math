import math

import pandas as pd

df1 = pd.DataFrame([[15, 15, 17], [19, 19, 16], [16, 18, 21]])
df2 = pd.DataFrame([[17, 17, 17], [15, 15, 15], [19, 22, 22]])
df3 = pd.DataFrame([[15, 17, 16], [18, 17, 16], [18, 18, 18]])
df4 = pd.DataFrame([[18, 20, 22], [15, 16, 17], [17, 17, 17]])

df_list = [df1, df2, df3, df4]

df = pd.DataFrame(columns=[0, 1, 2])
for i in range(len(df_list)):
    t = pd.DataFrame(df_list[i].mean(axis=1))
    df[i] = t
df = df.T

c = 3

S_A = 0
for i in range(df.shape[0]):
    S_A += math.pow(df.iloc[i, :].mean() - df.mean().mean(), 2)
S_A = S_A * df.shape[1] * c
print(f"S_A: {S_A}")
_S_A = S_A / 3
print(f"_S_A: {_S_A}")

S_B = 0
for j in range(df.shape[1]):
    S_B += math.pow(df.iloc[:, j].mean() - df.mean().mean(), 2)
S_B = S_B * df.shape[0] * c
print(f"S_B: {S_B}")
_S_B = S_B / 2
print(f"_S_B: {_S_B}")

S_I = 0
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        S_I += math.pow(df.iloc[i, j] - df.iloc[i, :].mean() - df.iloc[:, j].mean() + df.mean().mean(), 2)
S_I = S_I * c
print(f"S_I: {S_I}")
_S_I = S_I / 6
print(f"_S_I: {_S_I}")

S_E = 0
for i in range(len(df_list)):
    for j in range(df_list[0].shape[0]):
        for k in range(df_list[0].shape[1]):
            S_E += math.pow(df_list[i].iloc[j, k] - df.iloc[i, j], 2)
print(f"S_E: {S_E}")
_S_E = S_E / 24
print(f"_S_E: {_S_E}")

S_T = 0
for i in range(len(df_list)):
    for j in range(df_list[0].shape[0]):
        for k in range(df_list[0].shape[1]):
            S_T += math.pow(df_list[i].iloc[j, k] - df.mean().mean(), 2)
print(f"S_T: {S_T}")

print(f"F_A: {_S_A / _S_E}")
print(f"F_B: {_S_B / _S_E}")
print(f"F_I: {_S_I / _S_E}")
