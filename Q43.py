numbers = [10, 20, 30, 40, 50]

element = int(input("Enter element to find: "))

if element in numbers:
    print("Index:", numbers.index(element))
else:
    print("Element Not Found")