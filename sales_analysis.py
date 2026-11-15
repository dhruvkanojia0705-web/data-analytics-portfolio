
import pandas as pd
import matplotlib.pyplot as plt

# Read sales dataset
df = pd.read_csv("sales.csv")

# Calculate business KPIs
total_sales = df["Sales"].sum()
total_quantity = df["Quantity"].sum()
average_sales = df["Sales"].sum()

print ("SALES PERFORMANCE REPORT")
print ("------------------------")
print ("Total Revenue: Rs.", total_sales)
print ("Total Quantity:", total_quantity)
print ("Average Sales: Rs.", average_sales)

# Sales by product
print ("\nSales by Product:")
print (df[["Product", "Sales"]])

# Create chart
plt.figure(figsize=(9, 5))
plt.bar(df["Product"], df["Sales"])
plt.title("Sales Performance by Product")
plt.xlabel("Products")
plt.ylabel("Sales (INR)")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("sales_dashboard.png")
plt.close()

print("\nDashboard created successfully! ")
