
with open('day4input.txt', 'r') as file:
    passports = file.readlines()

# with open('day4example.txt', 'r') as file:
#     passports = file.readlines()

# print(passports)


# for string in read_file:
#     print(f"{string}\next str")

# issue of new lines being called new strings


# getting rid of new_lines
temp_passports = []
for string in passports:
    string = string.replace("\n", '')
    temp_passports.append(string)

# print(temp_passports)
# got rid of all \n


# now want to get all values into single strings, not over 2 or more strings...
#   separated by blank lines, which are now , '',

psplit = []
temp_string = []
p_temp = []
empty = []

for plist in passports:
    # print(plist)
    plist = str(plist)
    if plist != '':
        temp_string = plist.split()
        psplit.append(temp_string)
# print(psplit)

# print(p_temp)


length = len(psplit)
# print(length)

for i in range(len(psplit)):
    # print(i)
    # print(psplit[i])
    if i != length:
        index = psplit[i]
        # print(index)
        if index != empty:
            p_temp.extend(index)
        if index == empty:
            p_temp.extend('-')

# print(p_temp)

# got all values as a list of strings, diff passports separated by "'-'", should be able to split!

passports_list = [[]]
count = 0

for value in p_temp:
    if value != '-':
        passports_list[count].append(value)
    if value == '-':
        passports_list.append([])
        count += 1

# print(passports_list)
# YES!!!!! all values from each passport in a separate lists inside passports_list!!!!!!!


# values in the values lists need to be key value pairs
#   turn each list into a mini dictionary before adding to passports_dict

# putting these values into a dictionary:

passport_id = 1

temp_list = []
temp_dict = {}
passports_dict = {}

for passport in passports_list:
    # print(passport)
    temp_dict = {}
    for pair in passport:
        pair = str(pair)
        # print(pair)
        # temp_pair_list = []
        k, v = pair.split(":")
        temp_dict[k] = v
    # print(temp_dict)
    passports_dict.update({passport_id: temp_dict})
    passport_id += 1

# print(passports_dict)
# # nice and easy! :)

# print(passports_dict.keys())
# print(passports_dict.values())

# print(passports_dict.get(1, {}).get('ecl'))
# # so this print statement retrieves the value for 'ecl in passport 1
#
# print(passports_dict.get(1, {}).get('pid'))
# # same for this one, but for pid
#
# print(passports_dict.get(1, {}))
# # returns the values of passport 1, so must be able to now validate the passport


# need to code a function to check if the passport is valid


# def is_valid():
#     valid_list = ['eyr', 'ecl', 'pid', 'hcl', 'byr', 'iyr', 'hgt']
#     passport_count = 1
#     valid_count = 0
#     for values in passports_dict.values():
#         # print(values)
#         valid_keys = 0
#         for key in values.keys():
#             # print(key)
#             if key != 'cid' and key in valid_list:
#                 valid_keys += 1
#         # print(valid_keys)
#         if valid_keys == 7:
#             valid_count += 1
#         passport_count += 1
#     return valid_count
#
# # all good, returns the example of 2 valid passports
#
# print(is_valid())
#
# # PART 2:
#
#
# def is_present():
#     passport_count = 1
#     present_count = 0
#     for values in passports_dict.values():
#         # print(values)
#         all_present_count = 0
#         for code in values:
#             byr = passports_dict.get(passport_count, {}).get('byr')
#             iyr = passports_dict.get(passport_count, {}).get('iyr')
#             eyr = passports_dict.get(passport_count, {}).get('eyr')
#             hgt = passports_dict.get(passport_count, {}).get('hgt')
#             hcl = passports_dict.get(passport_count, {}).get('hcl')
#             ecl = passports_dict.get(passport_count, {}).get('ecl')
#             pid = passports_dict.get(passport_count, {}).get('pid')
#             # print(code)
#             if code == 'byr' and len(byr) == 4 and 1920 <= int(byr) <= 2002:
#                 # print(byr)
#                 all_present_count += 1
#             elif code == 'iyr' and len(iyr) == 4 and 2010 <= int(iyr) <= 2020:
#                 # print(iyr)
#                 all_present_count += 1
#             elif code == 'eyr' and len(eyr) == 4 and 2020 <= int(eyr) <= 2030:
#                 # print(eyr)
#                 all_present_count += 1
#             elif code == 'hgt':
#                 if len(hgt) == 4:
#                     if 59 <= int(hgt[0:2]) <= 76:
#                         # print(hgt)
#                         all_present_count += 1
#                 elif len(hgt) == 5:
#                     if 150 <= int(hgt[0:3]) <= 193:
#                         # print(hgt)
#                         all_present_count += 1
#             elif code == 'hcl':
#                 if hcl[0] == '#' and len(hcl) == 7:
#                     # print(hcl[1:7])
#                     hcl_count = 0
#                     for character in hcl:
#                         if character in '#abcdef0123456789':
#                             hcl_count += 1
#                     # print(hcl_count)
#                     if hcl_count == 7:
#                         # print(hcl)
#                         all_present_count += 1
#             elif code == 'ecl' and ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
#                 # print(ecl)
#                 all_present_count += 1
#             elif code == 'pid' and len(pid) == 9:
#                 num_count = 0
#                 for num in pid:
#                     if num in '0123456789':
#                         num_count += 1
#                 if num_count == 9:
#                     # print(pid)
#                     all_present_count += 1
#             else:
#                 pass
#
#         passport_count += 1
#         # print(all_present_count)
#         if all_present_count == 7:
#             present_count += 1
#     return present_count
#
#
# print(is_present())


def valid_and_present():
    # combining both functions

    valid_list = ['eyr', 'ecl', 'pid', 'hcl', 'byr', 'iyr', 'hgt']
    v_p_count = 0
    passport_count = 1

    for values in passports_dict.values():
        # print(values)
        valid_keys = 0
        for key in values.keys():
            # print(key)
            if key != 'cid' and key in valid_list:
                valid_keys += 1
        # print(valid_keys)
        if valid_keys == 7:
            all_present_count = 0
            for code in values:
                print(values)
                # print(code)
                # print(type(code))
                byr = str(passports_dict.get(passport_count, {}).get('byr'))
                iyr = passports_dict.get(passport_count, {}).get('iyr')
                eyr = passports_dict.get(passport_count, {}).get('eyr')
                hgt = passports_dict.get(passport_count, {}).get('hgt')
                hcl = passports_dict.get(passport_count, {}).get('hcl')
                ecl = passports_dict.get(passport_count, {}).get('ecl')
                pid = passports_dict.get(passport_count, {}).get('pid')
                print(byr)
                print(type(byr))
                if code == 'byr' and len(byr) == 4 and byr is not None and 1920 <= int(byr) <= 2002:
                    # print(byr)
                    all_present_count += 1
                elif code == 'iyr' and len(iyr) == 4 and 2010 <= int(iyr) <= 2020:
                    # print(iyr)
                    all_present_count += 1
                elif code == 'eyr' and len(eyr) == 4 and 2020 <= int(eyr) <= 2030:
                    # print(eyr)
                    all_present_count += 1
                elif code == 'hgt':
                    if len(hgt) == 4:
                        if 59 <= int(hgt[0:2]) <= 76:
                            # print(hgt)
                            all_present_count += 1
                    elif len(hgt) == 5:
                        if 150 <= int(hgt[0:3]) <= 193:
                            # print(hgt)
                            all_present_count += 1
                elif code == 'hcl':
                    if hcl[0] == '#' and len(hcl) == 7:
                        # print(hcl[1:7])
                        hcl_count = 0
                        for character in hcl:
                            if character in '#abcdef0123456789':
                                hcl_count += 1
                        # print(hcl_count)
                        if hcl_count == 7:
                            # print(hcl)
                            all_present_count += 1
                elif code == 'ecl' and ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    # print(ecl)
                    all_present_count += 1
                elif code == 'pid' and len(pid) == 9:
                    num_count = 0
                    for num in pid:
                        if num in '0123456789':
                            num_count += 1
                    if num_count == 9:
                        # print(pid)
                        all_present_count += 1
                else:
                    pass
            passport_count += 1
            if all_present_count == 7:
                v_p_count += 1
    return v_p_count


print(valid_and_present())


# need to fix the fact that the codes can appear as 'none' so that part 2 will work
