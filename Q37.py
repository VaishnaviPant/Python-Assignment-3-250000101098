numbers = [10, 50, 30, 40, 20, 50]

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second Largest Element:", unique_numbers[-2])
else:
    print("Second largest element does not exist.")