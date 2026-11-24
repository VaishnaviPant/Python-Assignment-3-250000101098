numbers = [10, 20, 30, 40, 50]

position = int(input("Enter position (0 to 5): "))
element = int(input("Enter element to insert: "))

if 0 <= position <= len(numbers):
    numbers.insert(position, element)
    print("Updated List:", numbers)
else:
    print("Invalid Position")