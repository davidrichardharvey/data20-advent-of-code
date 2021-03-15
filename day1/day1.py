with open('day1input.txt', 'r') as f:

    nums = sorted([int(i.rstrip('\n')) for i in f.readlines()])


def sum_components(target):
    for i in nums:
        if target - i in nums:
            print(i, target - i)
            print(i * (target - i))
            break
        if i >= target / 2:
            break


sum_components(2020)
