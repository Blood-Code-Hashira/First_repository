#import numpy as np
import pandas as pd

data = {
        "Name": ["Adamya", "Akshay", "Ganesha", "Shlok"],
        "Age": [10, 20, 30, 40],
        "City": ["Lucknow", "M.P.", "Andhra Pradesh", "U.P."]
        }

df = pd.DataFrame(data)
print("\nUsing Head :\n",df.head(2))
print("\nUsing Tail :\n",df.tail(2))
print("\nPrinting the dataset :\n",df)

#df.to_csv("Sample.csv", index=False)
#df.to_excel("Sample.xlsx", index = False)
#df.to_json("Sample.json", index=False)
print("\nUsing Info method :\n", df.info()) # Entries refers to row in the output.

d2 = {
      "Name": ["Ram", "Shyam", "Ghanshyam","Aarush", "Jagdish", "Raj", "Max"],
      "Age": [10, 20, 30, 40, 50, 60, 70],
      "Salary": [10000, 20000, 30000, 40000, 50000, 60000, 70000],
      "Performance Score": [85, 90, 78, 92, 88, 95, 80]
      }

df_2 = pd.DataFrame(d2)

print("\nCreating another dataset :\n",df_2)
print("\nDescirbe Method :\n",df_2.describe())

print(f"\nUsing Shape :\n{df_2.shape}")
print(f"\nUsing Columns :\n{df_2.columns}")

print("\nFiltering The Dataset:\n",df_2[(df_2["Performance Score"] < 92) & (df_2["Salary"] > 30000) & (df_2["Age"] > 30)])

print("\nFiltering The Dataset:\n",df_2[(df_2["Performance Score"] < 92) & (df_2["Salary"] > 30000) | (df_2["Age"] > 30)])

x = df_2["Name"]
print("\nAccessing a single column\n", x)

y = df_2[["Salary", "Performance Score"]]
print("\nAccessing multiple columns at once :\n", y)

z1 = df_2[["Salary", "Age"]]
print("\nSelecting multiple columns:\n")
print(z1)
