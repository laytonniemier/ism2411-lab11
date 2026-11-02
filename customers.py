# ISM2411 Lab 11 — Customer Dictionary & Lookup
# Name: Layton Niemier
#
# Reflection
#
# 1. .get() vs. bracket notation:
#    I would use .get() when a key might legitimately be missing, like an
#    optional field (phone, email) in customer data pulled from a CRM, because
#    it returns a default instead of crashing the program. I would use bracket
#    notation when the key must be there, like a customer ID, because a
#    KeyError tells me right away that the data is broken. My rule of thumb:
#    if missing is normal, use .get(); if missing is a bug, use brackets.
#
# 2. Summary dictionary pattern:
#    Building totals by region with a loop is like a SUMIF formula or a
#    PivotTable in Excel that groups rows by region and adds up the amounts.
#    The Python version is more useful for large datasets because it can
#    handle millions of rows that would slow down or crash Excel, it doesn't
#    need anyone to click through menus, and it can be rerun on new data
#    automatically every day.


# ---------------------------------------------------------------
# Exercise 1 · One customer
# ---------------------------------------------------------------
print("=== Exercise 1: One customer ===")

customer = {
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# ---------------------------------------------------------------
# Exercise 2 · Update and add
# ---------------------------------------------------------------
print("\n=== Exercise 2: Update and add ===")

customer["phone"] = "813-555-0142"      # add a new field
print(customer)

customer["tier"] = "platinum"           # update an existing field
print(customer)

del customer["email"]                   # delete a field
print(customer)


# ---------------------------------------------------------------
# Exercise 3 · Safe lookup
# ---------------------------------------------------------------
print("\n=== Exercise 3: Safe lookup ===")

email = customer.get("email", "no email on file")
print("Using .get():", email)

try:
    print(customer["email"])
except KeyError as error:
    print("Using brackets: KeyError for", error)


# ---------------------------------------------------------------
# Exercise 4 · Iterate
# ---------------------------------------------------------------
print("\n=== Exercise 4: Iterate ===")

for key, value in customer.items():
    print(f"{key}: {value}")

print("--- without .items() ---")
for key in customer:
    print(key)

# Difference: looping over a dict by itself only gives you the keys.
# .items() gives you each (key, value) pair, so you can use both at once.
# Without .items() you would have to look up the value with customer[key].


# ---------------------------------------------------------------
# Exercise 5 · Lookup table
# ---------------------------------------------------------------
print("\n=== Exercise 5: Lookup table ===")

tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount: {discount_rate:.0%}")
print(f"Final price: ${final_price:.2f}")


# ---------------------------------------------------------------
# Exercise 6 · List of dicts
# ---------------------------------------------------------------
print("\n=== Exercise 6: List of dicts ===")

customers = [
    {"name": "Alice Johnson", "tier": "platinum", "ytd_spend": 1250.50},
    {"name": "Ben Carter", "tier": "silver", "ytd_spend": 430.00},
    {"name": "Carla Diaz", "tier": "bronze", "ytd_spend": 85.25},
]

purchase = 300
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount_amount = purchase * rate
    print(f"{c['name']} | tier: {c['tier']} | discount on ${purchase}: ${discount_amount:.2f}")


# ---------------------------------------------------------------
# Exercise 7 · Nested catalog
# ---------------------------------------------------------------
print("\n=== Exercise 7: Nested catalog ===")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} has only {info['stock']} left")


# ---------------------------------------------------------------
# Exercise 8 · Sales by region
# ---------------------------------------------------------------
print("\n=== Exercise 8: Sales by region ===")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for t in transactions:
    region = t["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + t["amount"]

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")
