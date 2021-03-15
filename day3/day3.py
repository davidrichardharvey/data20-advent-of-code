with open("day3input.txt", "r") as f:
    content = f.read()

content = content.split("\n")

for i in range(len(content)):
    content[i] = content[i] * 50

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

# PART 2 HINTS
# Every single test has an instance of "1"
# Whatever direction you need to go "1" in, make that i, as it cycles through your range in the for loop
# Make y the other number
