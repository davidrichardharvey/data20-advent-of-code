with open("day2input.txt", "r") as f:

    # separate characters and convert to a list
    f_list = []
    for i in f:
        i = i.replace("\n", "")
        i = i.replace(":", "")
        j = i.split(" ")
        f_list.append(j)

    # convert range into a list
    def characters(array):
        for range_characters in f_list:
            range_characters[0] = range_characters[0].split("-")
        return array

    # convert strings into integers
    def string_to_int(array2):
        for string in f_list:
            string[0][0] = int(string[0][0])
            string[0][1] = int(string[0][1])
        return array2

    # check valid passwords
    def valid_password(array3):
        valid = 0
        for password in array3:
            count = 0
            for letter in password[2]:
                if password[1] == letter:
                    count += 1
            if password[0][0] <= count <= password[0][1]:
                valid += 1
        return valid

print(f"Number of valid passwords: {valid_password(string_to_int(characters(f_list)))}")
