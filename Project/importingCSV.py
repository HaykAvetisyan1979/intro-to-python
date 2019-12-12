# coding=utf-8
from tkinter import filedialog

import numpy as np
import pandas as pd


dt = pd.read_csv('database.csv')

balance = np.array(dt, dtype=float)  # to work with lines

df = pd.DataFrame(dt, dtype=float)   # to work with columns

print(dt['Branch'][0])
print(dt['balance'][2])
print(balance[3])
print("average of the 3-rd line values=", np.mean(balance[3]))
print(balance[3][1])

print("average of column balance=",  float(np.mean(df['balance'])))
print(df)

df1 = pd.read_excel(r'C:\Users\G3\Desktop\intro-to-python\Project\database.xlsx')

# df1 = pd.read_excel(filedialog.askopenfilename())
print(df1)
