# PART 1

# opening the file

with open('day2input.txt', 'r') as file:
    values = file.readlines()

# print(values)
# needs some cleaning up

new_values = []

for i in values:
    i = i.replace("\n", '')
    new_values.append(i)

# print(new_values)
# better, \n is gone


# must get values into smaller lists of lists

new_lists = []

for i in new_values:
    new_lists.append([i])

# print(new_lists)

# new_lists0 = new_lists[0]
# print(new_lists0[0])
# the value is still the entire list, not separate values


# need to find a way to separate the values - use the spaces!!!
#       split the string on white space (.split), so do that for each string
# values_split = str(new_values)
# values_split = values_split.split()
#
# print(values_split)
# back to the beginning, without the \n

# putting into a list of lists

v_split = []

for i in new_lists:
    # print(i)
    i = str(i)
    temp_i = i.replace("'", '')
    # print(temp_i)
    for j in temp_i:
        temp_j = str(temp_i.replace("[", '', ))
        temp_j = str(temp_j.replace("]", '', ))
    # print(temp_j)
    temp_j = temp_j.split()
    v_split.append(temp_j)
    # print(temp_j)
# print(v_split)
# got it as lists within a list now, just had to remove the [] from the str
#       it was being counted as a part of the values [ '[....' '...]'], not ['...']


# removing the :

for x in v_split:
    # print(x)
    x1 = x[1].strip(':')
    # print(x1)
    x[1] = x1

# print(v_split)
# fixed, no colon now


# separating the numbers into 2 strings

for x in v_split:
    # print(x)
    x[0] = x[0].split('-')

# print(v_split)


# getting the values and completing the task

correct_count = 0

for x in v_split:
    password = x[2]
    letter = x[1]
    num1 = int(x[0][0])
    num2 = int(x[0][1])
    # print(f" password: {password}")
    # print(f" letter: {letter}")
    # print(f" min: {num1}")
    # print(f" max: {num2}")

    l_count = 0

    for i in password:
        if i == letter:
            l_count += 1
        # print(f" password: {password}")
        # print(f" letter: {letter}")
        # print(f" min: {num1}")
        # print(f" max: {num2}")
        # print(f" letter count: {l_count}")
    if num1 <= l_count <= num2:
        correct_count += 1
print(f" count of correct passwords: {correct_count}")

# got it, 591 correct passwords! :)


# PART 2

# no index zero for the task answer!

correct_letters_count = 0

for x in v_split:
    password = x[2]
    letter = x[1]
    num1 = int(x[0][0])
    num2 = int(x[0][1])

    num1 = num1 - 1
    num2 = num2 - 1
    # setting the index to start at 1, not 0!- so input - 1

    # print(password)
    # print(letter)
    # print(num1)
    # print(num2)

    if (password[num1] == letter or password[num2] == letter) and (password[num1] != password[num2]):
        # print(password[num1])
        # print(password[num2])
        correct_letters_count += 1


print(f" count of correct password letters: {correct_letters_count}")
