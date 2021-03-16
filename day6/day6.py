with open("day6input.txt", 'r') as f:
    temp = f.read().split('\n\n')
    # quest is a list of strings after concatenating every answer from each group
    quest = [''.join(i.split("\n")) for i in temp]
    # quest2 is a 2D list of answers for each person in each group
    quest2 = [i.split("\n") for i in temp]
    # answers is a list of sets of answers for each group, i.e. no duplicates
    answers = [set(answer) for answer in quest]
    total = sum(len(i) for i in answers)
    everytotal = 0

print(quest2)
print(quest)
print(answers)

# for each group, check if every letter in the set appears in the total concatenated string a number of times equal
# to the length of a each list in the 2D list, i.e. the number of people who answered
for i in range(0, len(quest)):
    for j in answers[i]:
        if quest[i].count(j) == len(quest2[i]):
            everytotal += 1


print(everytotal)
