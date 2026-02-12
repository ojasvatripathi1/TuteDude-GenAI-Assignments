## TASK 2: Categories (Sets)

# Solution 1 =>
categories = ["Electronics", "Gadgets", "Accessories", "Wearables", "Audio", "Photography"]
categories_set = set(categories)

# Solution 2 =>
categories_set.add("Gaming")
categories_set.add("Electronics")
print(categories_set)

# Solution 3 =>
category_check = "Gaming"
print(category_check in categories_set)

#Extra optional:
total_categories = len(categories_set)
print(total_categories)