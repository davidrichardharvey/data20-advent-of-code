with open("day2input.txt", "r") as f:
    content = f.readlines()

temp = []
valid = 0
new_valid = 0

# strip and replace unnecessary characters
for entry in content:
    entry = entry.replace('\n', '')
    entry = entry.replace(':', '')
    x = entry.split(" ")
    temp.append(x)

# split numbers into own list
for pass_range in temp:
    pass_range[0] = pass_range[0].split("-")

# turn number strings into integers
for pass_type in temp:
    pass_type[0][0] = int(pass_type[0][0])
    pass_type[0][1] = int(pass_type[0][1])

print(temp)

# Iterate letter through password to find valid passwords
for password in temp:
    count = 0
    for pass_letter in password[2]:
        if password[1] == pass_letter:
            count += 1
    if password[0][0] <= count <= password[0][1]:
        valid += 1

print(f"\nThere are {valid} valid passwords in the list")


# Part 2
print("\n\n")

# Generating new Python indexes
for i in temp:
    i[0][0] = i[0][0] - 1
    i[0][1] = i[0][1] - 1
print(temp)

# Comparing indexes using XOR operator
for i in temp:
    lower = i[0][0]
    upper = i[0][1]
    if bool(i[2][lower] == i[1]) != bool(i[2][upper] == i[1]):
        new_valid += 1
print(f"Actually, there are {new_valid} valid passwords in the list")

