# When we use "r", the entire text file is returned as a single string
# we use the readlines method to ensure that each new line is returned, rather than each individual character
with open("day1input.txt", "r") as f:
    content = f.readlines()

# create a new list to append to
new_list = []
# strip the new lines from content and turn the strings into integers
# be sure to return them as replace and int do not automatically return themselves or their new values
for i in content:
    i = i.replace('\n', '')
    i = int(i)
    new_list.append(i)
print(new_list)

# printing solution values
values = []
# search new_list for i and j
# subtracting i from 2020 will return j, if both i and j are the solutions you are looking for
for i in new_list:
    for j in new_list:
        # the correct solutions will appear as both i and j as you go through the list, returning 4 solutions
        # ensure the values are appended only if the list is currently empty
        # when the values are found again as their vice versa components, they will not be appended
        if 2020 - i == j and len(values) < 2:
            values.append(i)
            values.append(j)
print(values)

# multiply i and j from the previous for loop
answer = values[0] * values[1]

# print the answer
print(f"The solution is {answer}")


# Part 2
three_values = []
# correct solutions when 2020 - i - j is equal to k
for i in new_list:
    for j in new_list:
        for k in new_list:
            if 2020 - i - j == k and len(three_values) < 3:
                three_values.append(i)
                three_values.append(j)
                three_values.append(k)
print(three_values)

answer_two = three_values[0] * three_values[1] * three_values[2]
print(f"The solution is {answer_two}")
