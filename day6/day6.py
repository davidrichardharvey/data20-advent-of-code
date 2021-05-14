
# with open('day6input.txt', 'r') as file:
#     answers = file.readlines()

with open('day6example.txt', 'r') as file:
    answers = file.readlines()


# 26 questions marked a to z

# input letters = questions answered 'yes'

# group is separated by new line
# sum of group = count of letters in group (not times, just if the letter is there)

answers_list = []

for answer in answers:
    if answer != '\n':
        answers_list.append(answer)
    if answer == '\n':
        answers_list.append('-')


temp_list = []
temp_str = ''

for answer in answers_list:
    temp = answer.strip('\n')
    temp_list.append(temp)
    temp_str = temp_str + f"{temp}"

# print(answers_list)
# print(temp_list)
# print(temp_str)

answers_list = temp_str.split('-')
# print(answers_list)

# answers_list now contains the answers perfectly ready for analysis

answer_count_list = []

for answer in answers_list:
    # print(answer)
    letter_list = []
    for letter in answer:
        if letter not in letter_list:
            letter_list.append(letter)
    answer_count_list.append(letter_list)


# print(answer_count_list)

# now I only have unique letters, not repeated instances

sum = 0

for answer in answer_count_list:
    count = len(answer)
    # print(count)
    sum = sum + count

print(sum)

# answer == 6530


# PART 2

# not anyone answered yes,  but all answered yes!

answers_list2 = []

for answer in answers:
    if answer != '\n':
        answers_list2.append(answer)
    if answer == '\n':
        answers_list2.append('-')


temp_list2 = []
temp_str2 = ''

for answer in answers_list2:
    temp = answer.strip('\n')
    if answer != '-':
        temp_list2.append(temp + '.')
        temp_str2 = temp_str2 + str(temp + '.')
    if answer == '-':
        temp_list2.append(temp)
        temp_str2 = temp_str2 + str(temp)

print(answers_list2)
print(temp_list2)
print(temp_str2)

# now i have a string with all people separated by '.' and groups by '-'





