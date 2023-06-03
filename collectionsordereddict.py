from collections import OrderedDict

# Create an OrderedDict to store the items and their net prices
items = OrderedDict()

# Read the number of items
n = int(input())

# Process each item
for _ in range(n):
    # Read the item's name and price
    item_name, price = input().rsplit(' ', 1)
    price = int(price)

    # Calculate the net price by adding the price to the existing value or initializing it to 0
    items[item_name] = items.get(item_name, 0) + price

# Print the item_name and net_price in order of their first occurrence
for item_name, net_price in items.items():
    print(item_name, net_price)
