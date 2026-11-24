my_tuple = (10, 20, 30, 40)

print("Original Tuple:", my_tuple)

# Tuples cannot be modified directly.
# my_tuple[0] = 100  # This causes TypeError.

# Creating a new tuple using concatenation
new_tuple = (100,) + my_tuple[1:]

print("Modified Tuple:", new_tuple)