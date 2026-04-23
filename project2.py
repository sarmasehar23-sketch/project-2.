import pandas as pd
class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    def use_item(self, amount):
        self.quantity -= amount
df = pd.read_csv("morning_stock.csv")
df = df.rename(columns={"Qty_kg": "Current_Quantity"})
df["Current_Quantity"] = df["Current_Quantity"].astype(float)
coffee_row = df[df["Ingredient"] == "Coffee Beans"]
name = coffee_row.iloc[0]["Ingredient"]
quantity = float(coffee_row.iloc[0]["Current_Quantity"])
coffee = Ingredient(name, quantity)
coffee.use_item(2.5)
df.loc[df["Ingredient"] == "Coffee Beans", "Current_Quantity"] = coffee.quantity
df.to_csv("evening_stock.csv", index=False)
print("Evening stock saved successfully!")