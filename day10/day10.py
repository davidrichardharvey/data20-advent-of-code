with open('day10input.txt', 'r') as file:
    jolts_input = file.readlines()

# with open('day10example2.txt', 'r') as file:
#     jolts_input = file.readlines()

# with open('day10example.txt', 'r') as file:
#     jolts_input = file.readlines()


# PART 1

# each of your joltage adapters is rated for a specific voltage:
#   any adapter can take an input of 1, 2, or 3 jolts lower than it's rating and still produce its rated output
#   device also has built-in joltage adapter rated for 3 jolts higher than highest rated adapter in bag
#       e.g. if adapters = 3, 9, 6, device adapter == 12

#   seat outlet = 0 jolts

#   if you use every adapter in your bag at once,
#       what is the distribution of jolt differences between charging outlet, adapters, and device?

# e.g. adapters: 16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4
#   so device joltage = 19 +3, = 22 jolts
#   because adapters can only connect to one of 1, 2, or 3 jolts lower:
#       connection order = 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, device
#   so joltage diff = 7 cases of 1 jolt and 5 cases of 3 jolts

# must do adapters in numerical order if more than one can fit
#   i.e. from 4, could use 5, 6 or 7, but should go 4, 5, 6, 7, as you cant connect to a higher joltage

print(jolts_input)


jolts_list = []

for jolt in jolts_input:
    temp_jolt = jolt.strip('\n')
    jolts_list.append(int(temp_jolt))

print(jolts_list)
# removed the \n's and now have a list of numbers


device = max(jolts_list) + 3
print(device)
jolts_list.append(device)
# this gets the highest value form the list and adds 3


temp = sorted(jolts_list)
jolts_list = temp

print(jolts_list)
# now all numbers are in order


previous_number = 0

count3 = 0
count2 = 0
count1 = 0

for adapter in jolts_list:
    if int(adapter) - int(previous_number) == 3:
        count3 += 1
        previous_number = adapter
    elif int(adapter) - int(previous_number) == 2:
        count2 += 1
        previous_number = adapter
    elif int(adapter) - int(previous_number) == 1:
        count1 += 1
        previous_number = adapter
    else:
        print("Error!!!")

print(f"1: {count1}, 2:{count2}, 3: {count3}")
# counts all the differences between each number in the list

answer = int(count1) * int(count3)
print(f"answer = {answer}\n")
# calculates the answer, which is 2030


# PART 2

# need to figure out all the diff ways the adapters can be arranged
#   every arrangement needs to connect to the device's outlet
#   previous connection rules still apply
#   example 1 has 8 ways to connect:
#       (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
#       (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
#       (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
#       (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
#       (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
#       (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
#       (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
#       (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)

#   the second example has many arrangements (19208!)

# what is the total number of distinct ways you could arrange the adapters to connect to you device


print(jolts_list)

# need to check each number for all possible connections (from diff 1 to 3), and branch out from there
# record each unique set of connections as i go
# like opening a safe by going up one number every time

# not sure how to code this?
# while counter != length of list
# if diff = 1, elif diff = 2, elif diff = 3?
# then go again with next number?
# add each diff to a new list in a list of lists, then do something from there?

solution = {0: 1}
for adapter in jolts_list:
    solution[adapter] = 0
    if adapter - 1 in solution:
        solution[adapter] += solution[adapter - 1]
    if adapter - 2 in solution:
        solution[adapter] += solution[adapter - 2]
    if adapter - 3 in solution:
        solution[adapter] += solution[adapter - 3]

print(solution[max(jolts_list)])
