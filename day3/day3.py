with open("input.txt","r") as f:
    array = []
    for line in f: # read rest of lines
        array.append(line.replace('\n',''))


def tree_on_route(array, right_num, down_num):
    down = 0
    right = 0
    count = 0
    while down < len(array):
        right_mod = right % 31
        down_mod = down % 323
        if array[down_mod][right_mod] == '#':
            count += 1
        right += right_num
        down += down_num
    return count


a = tree_on_route(array, 1, 1)
b = tree_on_route(array, 3, 1)
c = tree_on_route(array, 5, 1)
d = tree_on_route(array, 7, 1)
e = tree_on_route(array, 1, 2)
print(a*b*c*d*e)