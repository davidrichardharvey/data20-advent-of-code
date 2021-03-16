with open("day3input.txt", "r") as f:

    # read file
    file = f.read()
    lines = file.split("\n")
    print(lines)

    # x number of spaces to the right, y number of spaces down
    def count_trees(x=0, y=1):
        tree_count = 0
        # start from 0, go through length of each line to check # and one down using y
        for i in range(0, len(lines), y):
            # remove white spaces
            line = lines[i].strip()
            # if position x in line = # add to count
            if line[x] == "#":
                tree_count += 1
            # add 3 spaces to the right each line
            x += 3
            # solution to string out of range(not 100% clear)
            x = x % len(line)
        return tree_count

print(count_trees())
