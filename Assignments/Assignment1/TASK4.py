## TASK 4: Combined Operations
# Solution 1 =>
products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch","Camera"]

price_dict ={"Laptop": 51000, "Smartphone": 30000, "Tablet": 15000, "Headphones": 2500, "Smartwatch": 3000, "Camera": 60000}

catalog = [] 
for i in range(len(products)):
    product_name = products[i]
    price = price_dict.get(product_name,0)
    category = categories[i]
    catalog.append((product_name,price,category))

print(catalog)

# Solution 2 =>
category_to_products = {}
for product_name, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append((product_name))
    
max_category = max(category_to_products, key=lambda c: len(category_to_products[c]))
max_products = category_to_products[max_category]

print("\nCategory with maximum products:", max_category)
print("Products in this category:", max_products)