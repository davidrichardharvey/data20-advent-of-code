import numpy as np

# Open the file of inputs
with open('day1input.txt', 'r') as f:
    # turn the text file into a sorted list
    nums = sorted([int(i.rstrip('\n')) for i in f.readlines()])

answers = []


# function for getting 2 numbers that sum to specific target
def sum_components(target):
    for i in nums:
        if target - i in nums:
            answers.extend([i, target - i])
            break
        if i >= target / 2:
            break
    return answers


# function for getting 3 numbers that sum to specific target using sum_components
def three_sum_components(target):
    temp = [i for i in nums if i < target//3]
    for j in temp:
        rem = target - j
        if len(sum_components(rem)) > 0:
            answers.append(j)
            break


three_sum_components(2020)
print(answers)
print(np.prod(answers))
