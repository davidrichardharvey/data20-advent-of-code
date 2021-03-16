with open("day3input.txt", "r") as f:
    content = f.read()

content = content.split("\n")

for i in range(len(content)):
    content[i] = content[i] * 200

# content[0] provides first line
# content[0][4] provides first line, fifth item
# across 3 - across indexes
# down 1 - down the rows
# content[x][y] - y increases by 3, starting at 0, moving across by 3
# use range for x

y = 0
tree_count = 0

for i in range(len(content)):
    if content[i][y] == '#':
        tree_count += 1
    y += 3
print(tree_count)


# Right 1, Down 1
y = 0
tree_count2 = 0

for i in range(len(content)):
    if content[i][y] == '#':
        tree_count2 += 1
    y += 1
print(tree_count2)

# Right 5, Down 1
y = 0
tree_count3 = 0

for i in range(len(content)):
    if content[i][y] == '#':
        tree_count3 += 1
    y += 5
print(tree_count3)

# Right 7, Down 1
y = 0
tree_count4 = 0

for i in range(len(content)):
    if content[i][y] == '#':
        tree_count4 += 1
    y += 7
print(tree_count4)

# Right 1, Down 2
# Use i % 2 != 0 (could use i == 0) to skip every other row
y = 0
tree_count5 = 0

for i in range(len(content)):
    if i % 2 != 0:
        pass
    else:
        if content[i][y] == '#':
            tree_count5 += 1
        y += 1
print(tree_count5)

multiplied_trees = tree_count * tree_count2 * tree_count3 * tree_count4 * tree_count5
print(f"The answer is {multiplied_trees}")
