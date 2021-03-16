with open("input.txt","r") as f:
    array = []
    for line in f: # read rest of lines
        array.append(line.replace('\n',''))


def highest_boarding_pass(array):
    max_id = 0

    # for each boarding pass in array the following code is executed.
    for bpass in array:

        # Checks first 7 letters of boarding pass, splits row_list accordingly.
        row_list = list(range(128))
        i = 0
        while i < 7:
            if bpass[i] == 'F':
                row_list = row_list[:len(row_list)//2]
            else:
                row_list = row_list[len(row_list)//2:]
            i += 1

        # Checks last 3 letters of boarding pass, splits col_list accordingly.
        j = 7
        col_list = list(range(8))
        while j < 10:
            if bpass[j] == 'L':
                col_list = col_list[:len(col_list) // 2]
            else:
                col_list = col_list[len(col_list) // 2:]
            j += 1

        # Makes a temp variable the current boarding pass id via stated equation in question.
        # If statement makes temp variable the current max boarding pass variable if temp
        # greater than.
        temp = (row_list[0] * 8) + col_list[0]
        if temp > max_id:
            max_id = temp

    return max_id


a = highest_boarding_pass(array)
print(a)
