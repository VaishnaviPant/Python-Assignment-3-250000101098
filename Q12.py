string = input("Enter a string: ")
ch = input("Enter a character: ")

first = string.find(ch)
last = string.rfind(ch)

print("First occurrence:", first)
print("Last occurrence:", last)