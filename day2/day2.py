with open("day2input.txt", "r") as f:
    content = f.readlines()

temp = []
valid = 0

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

