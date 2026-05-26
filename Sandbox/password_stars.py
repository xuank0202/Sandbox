MIN_LENGTH = 6

password = input("Enter password: ")

while len(password) < MIN_LENGTH:
    print("Password must be at least", MIN_LENGTH, "characters")
    password = input("Enter password: ")

print("*" * len(password))