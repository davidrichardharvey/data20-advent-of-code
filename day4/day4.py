with open("input.txt") as fp:
    lines = [f.strip() for f in fp]


def check_passports(lines):
    all_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    count = 0
    temp = {}
    passports = []
    for line in lines:
        if line == '':
            if all(keys in list(temp.keys()) for keys in all_keys):
                passports.append(temp)
            temp = {}

        else:
            new_line = line.split(' ')
            for i in new_line:
                temp[i.split(':')[0]] = i.split(':')[1]

    # Was missing check on last passport due to the if/else statement layout
    if all(keys in list(temp.keys()) for keys in all_keys):
        passports.append(temp)

    return len(passports), passports


def extra_validation(passports):
    all_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_passports = []
    for passport in passports:
        count = 0
        if 1920 <= int(passport['byr']) <= 2002:
            count += 1

        if 2010 <= int(passport['iyr']) <= 2020:
            count += 1

        if 2020 <= int(passport['eyr']) <= 2030:
            count += 1

        # could make if statement in for loop more pythonic.
        if passport['hgt'].count('cm') == 1:
            number = ''
            for char in passport['hgt']:
                if char.isdigit():
                    number += char

            if 150 <= int(number) <= 193:
                count += 1

        # could make if statement in for loop more pythonic
        elif passport['hgt'].count('in') == 1:
            number = ''
            for char in passport['hgt']:
                if char.isdigit():
                    number += char

            if 59 <= int(number) <= 76:
                count += 1

        # could use a while loop instead of for loop for neater code.
        if passport['hcl'][0] == '#' and len(passport['hcl']) == 7:
            allowed_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
            temp_count = 0
            for string in passport['hcl'][1:7]:
                if string in allowed_chars:
                    temp_count += 1

            if temp_count == 6:
                count += 1

        eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if passport['ecl'] in eye_colours:
            count += 1

        # could simplify using while loop
        if len(passport['pid']) == 9:
            temp_count = 0
            for val in passport['pid']:
                if val in "0123456789":
                    temp_count += 1
            if temp_count == 9:
                count += 1

        if count == 7:
            valid_passports.append(passport)

    return len(valid_passports)


# part 1 answer
a = check_passports(lines)
print(a[0])


# part 2 answer
b = extra_validation(a[1])
print(b)



