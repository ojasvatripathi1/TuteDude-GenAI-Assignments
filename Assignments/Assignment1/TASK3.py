## TASK 3: Product Pricing (Dictionaries)
# Solution 1 =>
price_dict ={"Laptop": 51000, "Smartphone": 30000, "Tablet": 15000, "Headphones": 2500, "Smartwatch": 3000, "Camera": 60000}

# Solution 2 =>
price_dict["Speaker"] = 4000
price_dict["Laptop"] = 58000

product_to_remove = "Headphones"

if product_to_remove in price_dict:
    del price_dict[product_to_remove]
    print(f"{product_to_remove} removed successfully.")
else:
    print(f"{product_to_remove} not found in the  dictionary.")

# Solution 3 =>
total_price = sum(price_dict.values())
total_products = len(price_dict)
average_price = total_price/total_products

print(f"Average price of products: {average_price}")

# Extra optional:
max_price_product = max(price_dict, key=price_dict.get)
min_price_product = min(price_dict, key=price_dict.get)

print(f"Most expensive product: {max_price_product } - {price_dict[max_price_product]}")
print(f"Least expensive product: {min_price_product} - {price_dict[min_price_product]}")
