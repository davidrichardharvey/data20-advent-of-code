from itertools import *
with open("2020_numbers.txt", "r") as f:
    content = f.readlines()

new_list = []
for i in content:
    # print(i)
    i = i.replace('\n', '')
    i = int(i)
    new_list.append(i)
# print(content)

exp_values = list(map(int, content))
list(combinations(content, 2))
all_pairs = list(combinations(exp_values, 2))
len(all_pairs)


def sums_to_2020(values):
    return sum(values) == 2020


result = list(filter(sums_to_2020, all_pairs))
print(result)

result_multiple = result[0][0] * result[0][1]
print(f"The result of these two values multiplied together is:  {result_multiple}")
