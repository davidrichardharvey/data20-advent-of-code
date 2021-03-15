with open("input.txt") as fp:
    lines = [f.strip() for f in fp]


def check_passports(lines):
    all_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    count = 0
    temp = {}
    for line in lines:
        if line == '':
            if all(keys in list(temp.keys()) for keys in all_keys):
                count += 1
            temp = {}

        else:
            new_line = line.split(' ')
            print(new_line)
            for i in new_line:
                temp[i.split(':')[0]] = i.split(':')[1]

    # Was missing check on last passport due to the if/else statement layout
    if all(keys in list(temp.keys()) for keys in all_keys):
        count += 1

    return count


a = check_passports(lines)
print(a)
