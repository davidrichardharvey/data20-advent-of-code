with open('day9input.txt', 'r') as file:
    numbers = file.readlines()

# with open('day9example.txt', 'r') as file:
#     numbers = file.readlines()


# PART 1


# preamble of 25 numbers
# after that each number added should be the sum of any two different numbers from the immediate previous 25 numbers
#   there can be more than 1 pair

# what is the first number that is not the sum of any 2 diff numbers from the previous 25?
#   after the first 25, so from 26 onwards

# example = preamble of 5!

temp_numbers_list = []

for num in numbers:
    temp_numbers_list.append(num)

# print(temp_numbers_list)

# put the numbers into a list


numbers_list = []

for number in temp_numbers_list:
    num = number.strip('\n')
    numbers_list.append(num)

# print(numbers_list)

# removed the \n characters


# want to use a counter for list comprehension/slicing

# need to change the limit to <= 24 for the actual input, or <= 4 for example input

# preamble_list = []
#
# # print(range((len(numbers_list))))
#
# for value in range((len(numbers_list))):
#     # print(value)
#     if int(value) <= 4:
#         preamble_list.append(numbers_list[value])
#         # print(preamble_list)
#
#     else:
#         target = numbers_list[value]
#         # the number one of the sums should match
#
#         length = len(preamble_list)
#         count = 1
#         index_counter = 0
#         addition_counter = 0
#         sums_list = []
#
#         for num in preamble_list:
#             while count != length:
#                 # print(count)
#                 while addition_counter != 5:
#                     # change this to 25 for input or 5 for example input
#                     # print(addition_counter)
#                     if int(preamble_list[index_counter]) == int(preamble_list[addition_counter]):
#                         pass
#                         # checks if the numbers are equal, and stops addition of identical numbers
#                     else:
#                         total = int(preamble_list[index_counter]) + int(preamble_list[addition_counter])
#                         # print(preamble_list[index_counter], preamble_list[addition_counter], total)
#                         if total not in sums_list:
#                             sums_list.append(total)
#                             # only adds new sums, makes the code neater
#                     addition_counter += 1
#                 addition_counter = 0
#                 index_counter += 1
#                 count += 1
#         # print(sums_list)
#
#         if int(target) not in sums_list:
#             print(target)
#             print(sums_list, f"\n")
#
#         preamble_list.append(numbers_list[value])
#         num_to_remove = preamble_list[0]
#         preamble_list.remove(num_to_remove)
#         # print(preamble_list, f"\n")
#         # adds the next number and removes the first number in the list, keeps the preamble rolling
#
#
# # yes!!! did it! answer = 1930745883


# PART 2

# now need to find a contiguous set of at least two numbers in my list that sum the invalid number

# in example:
#   invalid number = 127
#   adding 15 through 40 produces the invalid number (15 + 25 + 47 + 40 = 127)
#   to find the weakness add together the smallest and largest number in the contiguous range (15 -> 40)
#       e.g. 15 and 47, producing 42


target = 1930745883

# 127 in example
# 1930745883 in input

# starting from first number, add numbers to a sum until sum is higher or equal to the missing number
#   then, if higher, move to next (second) number and go again

# use the list and remove the first number each time, adding until the value is higher than the target
# add numbers added to rolling sum to a list as well

sums_dict = {}
correct_dict = {}
count = 0
correct_count = 0

# print(numbers_list)
# print(range(len(numbers_list)))

for num in range(len(numbers_list)):
    # print(num)
    rolling_sum = 0
    added_list = []
    for value in numbers_list:
        # print(value)
        if rolling_sum < target:
            rolling_sum = rolling_sum + int(value)
            added_list.append(value)
            sums_dict.update({(str(rolling_sum) + '.' + str(count)): added_list})
            # print(rolling_sum)
            # print(added_list)
        elif rolling_sum == target:
            correct_dict.update({correct_count: {rolling_sum: added_list}})
            # print(rolling_sum, added_list, count, 'TRUE')
            # print(sums_dict)
            # print(sums_dict.get(f"1930745883.{count}"))
            correct_count += 1

            break

    count += 1
    # print(added_list)
    # print(sums_dict)
    numbers_list.remove(numbers_list[0])

# print(sums_dict.get('1930745883.553'))
# #
# #
# maximum = max(sums_dict['1930745883.553'])
# minimum = min(sums_dict.get('1930745883.553'))
#
# print(maximum, minimum)
#
# max_min_sum = int(maximum) + int(minimum)
# print(max_min_sum)

# no idea why the 20068... number isnt correct!!!!

# make dictionary for only correct ones - {correct_count:{rolling:[]}}

# print(correct_dict)

dictionary = correct_dict.get(0)
# print(dictionary)
values_list = []
for value in dictionary.values():
    values_list.append(value)

print(values_list[0])

maximum = max(values_list[0])
minimum = min(values_list[0])

print(minimum, maximum)

total_2 = int(minimum) + int(maximum)
print(total_2)

# this should be working! It works with the example data, why not the input data???!!!

# 200682420 is wrong!
