# with open('day11input.txt', 'r') as file:
#     grid = file.readlines()

with open('day11example.txt', 'r') as file:
    grid = file.readlines()


# PART 1

# seating people on a ferry:
#   L = empty seat
#   # = occupied seat
#   . = floor
# seating rules:
#   all based on a number of adjacent occupied seats to the given set
#       (one of the 8 positions: up, down, left, right, or diagonal)
#   if a seat is empty,
#       and no occupied seats adjacent to it,
#           the seat becomes occupied
#   if a seat is occupied,
#       and four or more seats adjacent are also occupied,
#           the seat becomes empty
#   otherwise, seat's state doesnt change,
#       and floor never changes,
#           and seats don't move

# find how many times it takes of changes before people stop moving around/remains the same


print(grid)


new_grid = []

for i in grid:
    i = i.strip("\n")
    new_grid.append(i)

print(new_grid)
# removed the \n's


# need a way to connect to the strings before and after
#   and get the value in those strings (above and below), and +/-1 form those values (diagonals)

line_count = 0
print(len(new_grid))


while line_count != len(new_grid):
    for line in new_grid:
        # print(line)
        # gets me to each row of seats

        for seat in range(len(line)):
            print(seat)
            # this gets me to the specific seats
            left_seat = seat - 1
            print(left_seat)
            right_seat = seat - 1
            print(right_seat)

    line_count += 1

