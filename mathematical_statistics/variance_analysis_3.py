import math

import pandas as pd

df1 = pd.DataFrame([[15, 15, 17], [19, 19, 16], [16, 18, 21]])
df2 = pd.DataFrame([[17, 17, 17], [15, 15, 15], [19, 22, 22]])
df3 = pd.DataFrame([[15, 17, 16], [18, 17, 16], [18, 18, 18]])
df4 = pd.DataFrame([[18, 20, 22], [15, 16, 17], [17, 17, 17]])

df = [df1, df2, df3, df4]

mean = 0
for i in range(len(df)):
    mean += df[i].mean().mean()
mean = mean / len(df)

S_A = 0
for i in range(len(df)):
    S_A += math.pow(df[i].mean().mean() - mean, 2)
S_A *= df[0].shape[0] * df[0].shape[1]
print(S_A)

S_B = 0
for j in range(df[0].shape[0]):
    mean_j = 0
    for i in range(len(df)):
        mean_j += df[i].iloc[j, :].mean()
    S_B += math.pow(mean_j / (len(df)) - mean, 2)
S_B *= len(df) * df[0].shape[1]
print(S_B)

S_I = 0
for i in range(len(df)):
    for j in range(df[0].shape[0]):
        S_I += df[i].iloc[j, :]