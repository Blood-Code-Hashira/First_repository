import pandas as pd
import matplotlib.pyplot as plt

data = {
        'Product' :["Laptop", "T.V.", "Mobile", "Earbuds"],
        'Month 1': [75000, 80000, 65000, 31100],
        'Month 2': [85000, 54000, 99000, 53220],
        'Month 3': [66000, 78000, 43000, 70000],
        'Ratings': [5, 2, 7, 5]
        }

df = pd.DataFrame(data)
u = df[df["Product"] == "Laptop"]
print("\nLaptop's info :\n", u)

df.insert(4, "Month 4", [92993, 93923, 99993, 89999])
df.loc[0, "Month 1"] = 89000
df['Total'] = df[['Month 1', 'Month 2', 'Month 3', 'Month 4']].sum(axis=1)


highest_selling_product = df.loc[df['Total'].idxmax()]
print(f"\nProduct that had made the highest profit:\n{highest_selling_product}")

highest_rating_product = df.loc[df['Ratings'].idxmax()]
print("\nHighest rating product:\n", highest_rating_product)

product_of_month1 = df.loc[df['Month 1'].idxmax()]
print(f"\nProduct that made highest profit in month 1 is:\n{product_of_month1}")

product_of_month2 = df.loc[df['Month 2'].idxmax()]
print(f"\nProduct that made highest profit in month 2 is:\n{product_of_month2}")

product_of_month3 = df.loc[df['Month 3'].idxmax()]
print(f"\nProduct that made highest profit in month 3 is:\n{product_of_month3}")
print("\nData Frame Before Sorting :\n", df)

d = df.sort_values(by = "Total", ascending = False)
print("\nData Frame After Sorting :\n", d)

print("\nBar-Graph:\n")
plt.bar(df['Product'], df['Total'], color='orange', edgecolor='black', linewidth=2)
plt.title("Sales-Bar graph")
plt.xlabel("Products Name")
plt.ylabel("Total")
plt.show()
