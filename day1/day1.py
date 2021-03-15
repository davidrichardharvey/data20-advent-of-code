# PART 1

# opening the file
with open('day1input.txt', 'r') as file:
    nums = file.readlines()

# print(nums)


# fixing the format of the list

new_nums = []

for i in nums:
    i = i.replace("\n", '')
    i = int(i)
    new_nums.append(i)

# print(new_nums)


# function to check numbers


# def add_nums(target):
#     for a in new_nums:
#         print(a)
#         for b in new_nums:
#             print(b)
#             if a + b == target:
#                 return target
#         print(a_list)
#         print(b_list)
#
#
# add_nums(2020)

# simplest code I can think of that might do this
# should be working, I think?


# def add_nums2(target2):
#     for a in new_nums:
#         if a + new_nums[-1] == target2:
#             print(target2)

# adding each number to the reverse of the sequence? - logically wont work/didn't


# nums_list = []

# def add_nums3(target3):
#     for a in new_nums:
#         # print(a)  # it is iterating through new_nums
#         for b in new_nums:
#             # print(b)  # iterating through a over and over
#             if a + b == target3:
#                 # return target3  # it returned target3! now need to get a and b
#                 nums_list.append(a)
#                 nums_list.append(b)
#                 return nums_list
#
#
# print(add_nums3(2020))
# works perfectly, and is very close to the original idea I had :)


# final code without comments:

def add_nums3(target):
    nums_list = []
    for a in new_nums:
        for b in new_nums:
            if a + b == target:
                nums_list.append(a)
                nums_list.append(b)
                return nums_list


print(add_nums3(2020))

# answering the question (product):
print(1224 * 796)

# got it right :)


# PART 2

# now need the three numbers that sum to 2020
def add_more_nums(target):
    nums_list = []
    for a in new_nums:
        for b in new_nums:
            for c in new_nums:
                if a + b + c == target:
                    nums_list.append(a)
                    nums_list.append(b)
                    nums_list.append(c)
                    return nums_list


print(add_more_nums(2020))

# answering the question (product):
print(332 * 858 * 830)

# right again :)
