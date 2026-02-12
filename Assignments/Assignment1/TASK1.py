## TASK 1: Product Collections (Lists & Tuples)

# Solution 1 => 
products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch","Camera"]

# Solution 2 => 
sample_product = ("Smartphone", 15000, "Gadget")

# Solution 3 => 
print(products[1], products[5])

# Solution 4 => 
products.append("Speaker")
products.append("Printer")

print(products)

# Extra optional:
sample_product_list = list(sample_product)
sample_product_list[1] = 21000
sample_product_list = tuple(sample_product_list)

print(sample_product_list)