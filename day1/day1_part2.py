from itertools import *
with open("day1input.txt", "r") as f:
    content = f.readlines()

new_list = []
for i in content:
    # print(i)
    i = i.replace('\n', '')
    i = int(i)
    new_list.append(i)
# print(content)

exp_values = list(map(int, content))
# Change 2 to 3
list(combinations(content, 3))
# Change 2 to 3
all_pairs = list(combinations(exp_values, 3))
len(all_pairs)


def sums_to_2020(values):
    return sum(values) == 2020


result = list(filter(sums_to_2020, all_pairs))
print(result)

# Add a third value to be multiplied:
result_multiple = result[0][0] * result[0][1] * result[0][2]
print(f"The result of these two values multiplied together is:  {result_multiple}")
