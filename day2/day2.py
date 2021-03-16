# Notes are for my benefit:

#P
def verify_password_part_one(line):
    # separates list entry into required policy and password via ':'
    required, password = [item.strip() for item in line.split(':')]
    # bounds are found in the initial string, bar the last two index values
    bounds = required[:-2]
    # The letter is found in the last index before the colon
    letter = required[-1]
    # separates the lowest and highest value in the requirement policy via '-'
    low, high = [int(item) for item in bounds.split('-')]

    letter_count = password.count(letter)
    if low <= letter_count <= high:
        return True
    else:
        return False


def count_password_part_one(password_list):
    good_passwords = 0
    for line in password_list:
        if verify_password_part_one(line):
            good_passwords += 1
    print(f"Number of acceptable passwords for part one:  {good_passwords}")
    return good_passwords


def verify_password_part_two(line):
    required, password = [item.strip() for item in line.split(':')]
    bounds = required[:-2]
    letter = required[-1]
    index1, index2 = [int(item) for item in bounds.split('-')]
    new_index1 = (int(index1) - 1)
    new_index2 = (int(index2) - 1)
    letter_index1 = password[new_index1]
    letter_index2 = password[new_index2]

    if letter_index1 == letter and letter_index2 != letter:
        return True
    elif letter_index1 != letter and letter_index2 == letter:
        return True
    else:
        return False


def count_password_part_two(password_list):
    valid_passwords = 0
    for line in password_list:
        if verify_password_part_two(line):
            valid_passwords += 1
    print(f"Number of acceptable passwords for part two:  {valid_passwords}")
    return valid_passwords


password_list = []
with open("day2input.txt", "r") as f:
    for line in f:
        password_list.append(line.strip())
    count_password_part_one(password_list)
    count_password_part_two(password_list)
