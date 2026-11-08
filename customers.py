# Reflection 1:
# .get() is useful when a key might not exist because it can return a default value. Bracket notation is better when I know the key should exist. I would use .get() for optional data and brackets for required data.

# Reflection 2:
# This reminds me of using a PivotTable or SUMIF in Excel to group and total data. Python can be more useful for large datasets because it can handle lots of data automatically.

# Exercise 1 - One customer
customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 1250
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2 - Update and add
customer["phone"] = "555-1234"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

# Exercise 3 - Safe lookup
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email not found")

# Exercise 4 - Iterate
for key, value in customer.items():
    print(f"{key}: {value}")
# Without .items(), the loop only gives the dictionary keys.
for key in customer:
    print(key)

# Exercise 5 - Lookup table
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}
tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)
purchase_price = 200
final_price = purchase_price * (1 - discount_rate)
print("Tier:", tier)
print("Discount:", discount_rate * 100, "%")
print("Final price:", final_price)

# Exercise 6 - List of dicts
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]
for person in customers:
    rate = tier_discounts.get(person["tier"], 0)
    discount_amount = 300 * rate
    print(
        f'{person["name"]}: {person["tier"]}, '
        f'discount amount: ${discount_amount:.2f}'
    )

# Exercise 7 - Nested catalog
catalog = {
    "Widget A": {
        "price": 9.99,
        "stock": 150
    },
    "Gadget C": {
        "price": 49.99,
        "stock": 8
    }
}
for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"{product}: LOW STOCK")

# Exercise 8 - Sales by region
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]
summary = {}
for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    summary[region] = summary.get(region, 0) + amount
for region in sorted(summary):
    print(f"{region}: {summary[region]}")