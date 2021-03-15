# Repeat the map horizontally enough times to reach the bottom (moving right 3 and down 1 so needs 3 * number of lines)

# with open('day3input.txt', 'r+') as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         lines[i] = lines[i].rstrip('\n') * 32 + "\n"
#     f.seek(0)
#
#     for line in lines:
#         f.write(line)


# Turn dots and hashes into 0s and 1s respectively

# with open('day3input.txt', 'r+') as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         lines[i] = ''.join(str(x) for x in [1 if j == '#' else 0 for j in lines[i]])
#
#     f.seek(0)
#
# with open('day3tinput.txt', 'w') as w:
#     for line in lines:
#         w.write(line + "\n")


# read lines of the new file of 0s and 1s to create a matrix
with open('day3tinput.txt', 'r') as r:
    temp = [i.rstrip("\n") for i in r.readlines()]
    matrix = [[int(j) for j in k] for k in temp]


# start moving right 3 and down 1 in the matrix. Right 3 means going through the index of each row, down 1 means
# moving to the next row, i.e. next list element of the matrix
def treehopping(mat):
    coords = [0, 0]
    counter = 0
    while coords[1] < len(mat) - 1:
        coords[0] += 3
        coords[1] += 1
        if mat[coords[1]][coords[0]]:
            counter += 1

        if coords[1] == len(mat):
            break
    return counter

print(treehopping(matrix))
