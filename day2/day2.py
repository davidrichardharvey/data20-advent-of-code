# Opens up file, each entry for password split into 3 strings.
with open("day2input.txt","r") as f:
    array = []
    for line in f: # read rest of lines
        array.append((line.replace('\n','')).split())


def check_valid_password(array):
    valid_count = 0
    for password in array:
        lower_lim = int(password[0].split('-')[0])
        upper_lim = int(password[0].split('-')[1])
        letter_needed = password[1][0]
        amount_sub_in_pass = password[2].count(letter_needed)
        if (amount_sub_in_pass >= lower_lim) and (amount_sub_in_pass <= upper_lim):
            valid_count += 1

    return valid_count


def new_check_valid_password(array):
    valid_count = 0
    for password in array:
        allowed_space = int(password[0].split('-')[0]) - 1
        not_allowed_space = int(password[0].split('-')[1]) - 1
        letter_needed = password[1][0]
        if password[2][allowed_space] == letter_needed and password[2][not_allowed_space] != letter_needed:
            valid_count += 1
            continue

        elif password[2][not_allowed_space] == letter_needed and password[2][allowed_space] != letter_needed :
            valid_count += 1


    return valid_count

print(new_check_valid_password(array))
