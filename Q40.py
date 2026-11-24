list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = list(set(list1) & set(list2))

print("Common Elements:", sorted(common))