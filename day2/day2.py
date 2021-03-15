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



print(check_valid_password(array))