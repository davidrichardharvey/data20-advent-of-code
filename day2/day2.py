# Notes are for my benefit
def verify_password(line):
    # separates list entry into required policy and password via ':'
    required, password = [item.strip() for item in line.split(':')]
    # bounds are found in the initial string, bar the last two index values
    bounds = required[:-2]
    # The letter is found in the last index before the colon
    letter = required[-1]
    # separates the lowest and highest value in the requirement policy via '-'
    low, high = [int(item) for item in bounds.split('-')]

    # Eliminates passwords that don't meet the length criteria
    letter_count = password.count(letter)
    if low <= letter_count <= high:
        return True
    else:
        return False


def count_password(password_list):
    good_passwords = 0
    for line in password_list:
        if verify_password(line):
            good_passwords += 1
    print(f"Number of acceptable passwords:  {good_passwords}")
    return good_passwords


password_list = []
with open("day2input.txt", "r") as f:
    for line in f:
        password_list.append(line.strip())
    count_password(password_list)


