
with open('day3input.txt', 'r') as file:
    grid = file.readlines()

# with open('day3example.txt', 'r') as file:
#     grid = file.readlines()

# print(grid)


new_grid = []

for i in grid:
    i = i.replace("\n", '')
    new_grid.append(i)

# print(new_grid)
# removed the \n


# for col in new_grid:
#     print(col)
# giving a relevant output line by line


# str_len = len(new_grid[0])
# print(str_len)
# perfect! will allow for measuring when to loop back round


def set_length():
    count = 0
    for i in new_grid:
        # for j in i:
        #     print(j)
        count += 1
        # print(i)
    return count


print(set_length())


def move(across_move, down_move):
    across = 0
    down = 0
    col_count = 0
    str_len = len(new_grid[1])
    trees = 0
    while col_count <= set_length():
        for row in new_grid:
            # print(row)
            across += across_move
            down += down_move
            if across >= 31:
                diff = str_len - across
                across = 0 - diff
            # print(down)
            # print(across)
            position = new_grid[down][across]
            # print(position)
            if position == '#':
                trees += 1
                print(trees)
            # print(col_count)
            col_count += 1
    return trees


# print(move(3, 1))

# working, cant seem to get rid of the list index out of range error
# got the right answer = 218


# PART 2

# # across 1, down 1
# print(move(1, 1))
# # trees = 77

# # across 3 down 1
# print(move(3, 1))
# # trees = 218

# # across 5, down 1
# print(move(5, 1))
# trees = 65

# # across 7, down 1
# print(move(7, 1))
# # trees = 82

# # across 1, down 2
# print(move(1, 2))
# # trees = 43


# total trees
total = 77 * 218 * 65 * 82 * 43

print(total)

# correct, total product of trees on all slopes = 3847183340