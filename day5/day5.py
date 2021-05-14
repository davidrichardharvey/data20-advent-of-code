import math


with open('day5input.txt', 'r') as file:
    codes = file.readlines()

# with open('day5example.txt', 'r') as file:
#     codes = file.readlines()

# print(codes)


codes_list = []

for code in codes:
    if code != codes[-1]:
        temp_code = code.strip(code[-1])
        codes_list.append(temp_code)
    else:
        codes_list.append(code)

# print(codes_list)

# all codes in new list without \n at the end

# now onto the task:

codes_seats = []

for code in codes_list:
    row_upper = 127
    row_lower = 0
    row = 0
    for char in code[0:7]:
        if char == 'F':
            row_upper = row_lower + ((row_upper - row_lower)/2)
            row_lower = row_lower
            # print(row_lower, row_upper)
        else:
            row_lower = row_lower + ((row_upper - row_lower)/2)
            row_upper = row_upper
            # print(row_lower, row_upper)

        if code[6] == 'F':
            row = int(math.ceil(row_lower))
        else:
            row = int(math.floor(row_upper))
    # print(code)
    # print(code[0:7])
    # print(row)

    # getting the correct row now :)

    column_upper = 7
    column_lower = 0
    column = 0

    for char in code[7:10]:
        if char == 'L':
            column_upper = column_lower + ((column_upper - column_lower)/2)
            column_lower = column_lower
            # print(column_lower, column_upper)
        else:
            column_lower = column_lower + ((column_upper - column_lower)/2)
            column_upper = column_upper
            # print(column_lower, column_upper)

        if code[9] == 'R':
            column = int(math.ceil(column_lower))
        else:
            column = int(math.floor(column_upper))

    codes_seats.append((row, column))

    # print(code[7:10])
    # print(column)

    # all good for the final 3 digits too :)

# print(codes_seats)

seat_ids = []

for seat in codes_seats:
    # seat_id = 0
    seat_id = (seat[0] * 8) + seat[1]
    seat_ids.append(seat_id)

# print(seat_ids)

# perfect!!!

# answer:
print(max(seat_ids))


# PART 2

max_seat_id = (127 * 8) + 7
print(max_seat_id)

missing_list = []

for seat in range(0, max_seat_id):
    if seat not in seat_ids:
        missing_list.append(seat)

print(missing_list)


for seat in range(len(missing_list)):
    seat_diff = missing_list[seat+1]-missing_list[seat]
    # print(seat_diff)
    if seat_diff != 1:
        print(missing_list[seat])

# answer = 640 :)
