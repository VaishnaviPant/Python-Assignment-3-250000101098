string = input("Enter a string: ")
ch = input("Enter a character: ")

if string.startswith(ch) and string.endswith(ch):
    print("String starts and ends with the given character.")
else:
    print("String does not start and end with the given character.")