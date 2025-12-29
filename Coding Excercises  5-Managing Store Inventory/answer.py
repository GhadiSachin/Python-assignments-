branch_a_products={"bread", "milk", "butter", "jam"}
branch_b_products={"bread", "cheese", "butter", "ketchup"}
print(branch_a_products)
print(branch_b_products)

all_items_union=branch_a_products | branch_b_products
print(all_items_union)

all_items_intersection=branch_a_products & branch_b_products
print(all_items_intersection)

all_items_notin=branch_a_products -branch_b_products

print(all_items_notin)

print('ketchup' in  branch_a_products)
# Define a frozenset called essential items with the specified values

essential_items = frozenset(["milk", "bread", "ketchup"])

# Print the frozenset
print(essential_items)