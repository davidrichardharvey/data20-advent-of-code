import re

# read file and make dictionary of bag colour and its contents
with open("day7input.txt", 'r') as f:
    rules = f.read().split('\n')
    temp = [i.split(" bags contain ") for i in rules]
    ruledict = {}

    for j in temp:
        ruledict.update({j[0]: j[1].split(" bags, ")})
print(rules)
print(temp)
print(ruledict)


# search algorithm to find bags that contain a bag of the parameter colour
def search(tree: dict, colour):
    temp = []
    for i in list(tree.keys()):
        for k in tree[i]:
            if re.findall(colour, k):
                temp.append(i)
                tree.pop(i)
    return temp, len(temp)


# function for a recursive search of the dictionary to find the number of bags that can contain the specified colour
def bigsearch(tree: dict, colour):
    counter = 0
    temp = [colour]
    while temp:
        for x in temp:
            temp2 = search(tree, x)
            temp.extend(temp2[0])
            counter += temp2[1]
            temp.remove(x)
        if not temp:
            break
    return counter

print(bigsearch(ruledict, "shiny gold"))
