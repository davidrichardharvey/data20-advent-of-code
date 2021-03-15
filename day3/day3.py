with open("input.txt","r") as f:
    array = []
    for line in f: # read rest of lines
        array.append(line.replace('\n',''))


def tree_on_route(array):
    down = 0
    right = 0
    count = 0
    while down != len(array):
        right_mod = right % 31
        if array[down][right_mod] == '#':
            count += 1
        right += 3
        down += 1
    return count


a = tree_on_route(array)
print(a)