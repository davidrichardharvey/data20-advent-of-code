with open("day6input.txt", 'r') as f:
    temp = f.read().split('\n\n')
    quest = [''.join(i.split("\n")) for i in temp]
    quest2 = [i.split("\n") for i in temp]
    answers = [set(answer) for answer in quest]
    total = sum(len(i) for i in answers)
    everytotal = 0

print(quest2)
print(quest)
print(answers)

for i in range(0, len(quest)):
    for j in answers[i]:
        if quest[i].count(j) == len(quest2[i]):
            everytotal += 1


print(everytotal)