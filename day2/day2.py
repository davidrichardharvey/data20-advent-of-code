# import Regex
import re

# Open the file of inputs
with open('day2input.txt', 'r') as f:
    # turn the text file into a 2D list separated by occurrence range, character and password
    pw = [re.split(' |: ', i.rstrip('\n')) for i in f.readlines()]


# count number of passwords in the list where a character appears within the specified range
def pw_validity(passwords):
    counter = 0
    for i in passwords:
        low = int(i[0].split('-')[0])
        high = int(i[0].split('-')[-1])
        if low <= i[2].count(i[1]) <= high:
            counter += 1
    return counter


# count number of passwords in the list where character appears in exactly one of the specified indexes
def pw_validity_new(passwords):
    counter = 0
    for i in passwords:
        index1 = int(i[0].split('-')[0]) - 1
        index2 = int(i[0].split('-')[-1]) - 1
        if [i[2][index1], i[2][index2]].count(i[1]) == 1:
            counter += 1
    return counter


print(pw_validity_new(pw))
