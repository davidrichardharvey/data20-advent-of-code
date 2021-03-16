# import Regex
import re

# Open the file of inputs
with open('day4input.txt', 'r') as f:
    pp = f.read().split('\n\n')

# list of passport fields
p = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


# checking number of passports with all the required fields
def pp_validity(text):
    counter = 0
    for i in pp:
        if all(x in i for x in p):
            counter += 1
    return counter


with open("day4input.txt") as rf:
    pp2 = [f.strip() for f in rf]


total_dict = []
total_valid_dict = []

# turning the passports into a list of dictionaries
def makedict(txtlist):
    temp = [re.split("\n| ", i) for i in txtlist]
    for j in temp:
        temp2 = {}
        temp3 = [re.split(":", x) for x in j]
        for k in temp3:
            temp2.update({k[0]: k[1]})
        total_dict.append(temp2)


# only retaining the passports with all the required fields
def check_valid1(pplist):
    for i in pplist:
        if all(x in list(i.keys()) for x in p):
            total_valid_dict.append(i)


# checking how many passports have all the values for each field within the set constraints
def check_valid2(pplist):
    counter = 0
    ecol = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for i in pplist:
        temp = 0
        if 1920 <= int(i[p[0]]) <= 2002:
            temp += 1
        if 2010 <= int(i[p[1]]) <= 2020:
            temp += 1
        if 2020 <= int(i[p[2]]) <= 2030:
            temp += 1
        if re.findall(r"cm$", i[p[3]]):
            if 150 <= int(re.split("cm", i[p[3]])[0]) <= 193:
                temp += 1
        if re.findall(r"in$", i[p[3]]):
            if 59 <= int(re.split("in", i[p[3]])[0]) <= 76:
                temp += 1
        if re.findall(r"^#", i[p[4]]):
            if len(re.findall("[a-f0-9]", i[p[4]].split("#")[1])) == 6:
                temp += 1
        if i[p[5]] in ecol:
            temp += 1
        if i[p[6]].isdigit() and len(i[p[6]]) == 9:
            temp += 1
        if temp == 7:
            counter += 1
    return counter


print(check_valid2(total_valid_dict))


