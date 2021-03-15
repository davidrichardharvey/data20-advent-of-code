with open("input.txt") as fp:
    lines = [f.strip() for f in fp]


def check_passports(lines):
    valid_passports = []
    all_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    count = 0
    temp = {}
    for line in lines:

        if line == '':
            print(list(temp.keys()))
            if all(keys in list(temp.keys()) for keys in all_keys):
                count += 1
            temp = {}
            pass

        else:

            new_line = line.split(' ')
            for i in new_line:
                temp[i.split(':')[0]] = i.split(':')[1]

    return count


a = check_passports(lines)
print(a)