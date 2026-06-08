filename = input("Enter a filename: ")

in_file = open(filename, "r")

for line in in_file:
    print(line)

in_file.close()