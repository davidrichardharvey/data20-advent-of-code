route_list = []
xl_route_list = []
with open("day3input.txt", "r") as f:
    for line in f:
        route_list.append(line)
        res = list(''.join(route_list))
    print(res)


def pathway_to_exit(line):
    j = 0
    dot_count = 0
    tree_count = 0
    for i in range(0, len(res)):
        if res[i] == '.':
                dot_count += 1
                i += 33
        else:
            tree_count += 1
            i += 33

    print(dot_count)
    print(tree_count)

# Unfinished, complete in own time.
