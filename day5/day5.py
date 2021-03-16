with open("input.txt","r") as f:
    array = []
    for line in f: # read rest of lines
        array.append(line.replace('\n',''))


def highest_boarding_pass(array):
    max_id = 0
    all_seat_ids = []
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

    # part 2 of question, saves all seat id's, sorts the list find when they is a missing number in
    # sequence as we know this is where our seat will be.
        all_seat_ids.append(temp)
    all_seat_ids.sort()
    for i in range(1, len(all_seat_ids)):
        if all_seat_ids[i] - all_seat_ids[i-1] == 2:
            free_seat = all_seat_ids[i] - 1

    return max_id, free_seat


a = highest_boarding_pass(array)
print(a[0])
print(a[1])
