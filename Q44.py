list1 = [10, 20, 30, 40]

# Using copy()
list2 = list1.copy()

# Using direct assignment
list3 = list1

list1.append(50)

print("Original List:", list1)
print("Copied List:", list2)
print("Assigned List:", list3)