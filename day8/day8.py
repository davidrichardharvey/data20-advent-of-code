# with open('day8input.txt', 'r') as file:
#     game_code = file.readlines()

with open('day8example.txt', 'r') as file:
    game_code = file.readlines()


# PART 1


# infinite loop in the boot code
# need to run it in isolation
# each instruction == operation and argument

# acc = increase or decrease a single global value called the accumulator
#   starts at 0
#   operation immediately after acc is executed next
#   e.g. acc +7 would increase accumulator by 7

# jmp = jump to the next instruction relative to itself
#   e.g. jmp +2 would skip the next instruction
#   e.g. jmp +1 would do the instruction below it
#   e.g. jmp -20 would cause the instruction 20 lines above to be completed next

# nop = No Operation
#   so nothing happens and the next instruction is followed

# to solve:
#   before any instruction is run a second time, what is the value in the accumulator?


# print(game_code)
# just looking at the code

code_list = []

for value in game_code:
    code_list.append(value.strip('\n'))

# print(code_list)
# removed all \n's after values

# dictionary or list??
# dictionary in dictionary?
#   e.g. {increment_index : {action: number}}
# should allow me to skip through the dictionary by number when jumping (use a counter)
# if acc == second key, then can add the value to a counter
# if nop turns up, can use another counter to move to next line(same counter as jumping)

# to know if its going again, keep a record of the key increment numbers that have been run
#    then check before doing each action if the increment number has already been recorded!

# increment_counter = 1
# big_code_dict = {}
#
# for code in code_list:
#     instruction = code[0:3]
#     number = code[4:8]
#     # perfect for getting values out!!
#
#     # now add the incremental counter and append all to one big dictionary {:{}}
#     big_code_dict.update({increment_counter: {'operator': instruction, 'argument': number}})
#     increment_counter += 1

# print(big_code_dict)

# this worked, now have  a large dictionary ready to search/run through

# accumulator = 0
# place_counter = 1
# keys_list = []
#
# while place_counter not in keys_list:
#     keys_list.append(place_counter)
#     # print(big_code_dict[place_counter])
#     if big_code_dict[place_counter].get('operator') == 'acc':
#         accumulator = accumulator + int(big_code_dict[place_counter].get('argument'))
#         place_counter += 1
#         # adds the value to the accumulator
#     elif big_code_dict[place_counter].get('operator') == 'jmp':
#         place_counter = place_counter + int(big_code_dict[place_counter].get('argument'))
#         # should jump the numbers
#         print(place_counter)
#     elif big_code_dict[place_counter].get('operator') == 'nop':
#         place_counter += 1
#
# print(accumulator)
# print(keys_list)

# got it!!! 1087!


# PART 2

# believe one instruction is corrupt!
#   can only be a nop or jmp wrong (jmp should be nop and vice versa)
#   supposed to terminate immediately after last instruction in the file
# by changing exactly one jump or nop, you can repair the boot code and terminate it

# tips:
#   cannot be a +0 instruction
#   if a nop is a value other than 0, skips lines like jmp but does nothing
#   the example accumulator should stop at 6
#   the example jmp -4 code should be nop -4

# fix the code so that it terminates by changing a nop to jmp or vice versa


increment_counter = 1
big_code_dict = {}
jmp_counter = 1
acc_counter = 1
nop_counter = 1

for code in code_list:
    instruction = code[0:3]
    number = code[4:8]
    # perfect for getting values out!!

    # now add the incremental counter and append all to one big dictionary {:{}}
    if instruction == 'acc':
        big_code_dict.update({increment_counter: {acc_counter: {'operator': instruction, 'argument': number}}})
        increment_counter += 1
        acc_counter += 1

    elif instruction == 'jmp':
        big_code_dict.update({increment_counter: {jmp_counter: {'operator': instruction, 'argument': number}}})
        increment_counter += 1
        jmp_counter += 1

    elif instruction == 'nop':
        big_code_dict.update({increment_counter: {nop_counter: {'operator': instruction, 'argument': number}}})
        increment_counter += 1
        nop_counter += 1


print(big_code_dict)


accumulator = 0
place_counter = 1
keys_list = []

acc_count = 1
jmp_count = 1
nop_count = 1


while place_counter < 9 and place_counter not in keys_list:

    keys_list.append(place_counter)
    # print(big_code_dict[place_counter])
    # print(big_code_dict[place_counter].get(acc_count).get('operator'))
    # print(type(big_code_dict[place_counter].get(acc_count).get('operator')))

    if big_code_dict[place_counter].get(acc_count).get('operator') == 'acc':
        print('acc')
        accumulator = accumulator + int(big_code_dict[place_counter].get(acc_count).get('argument'))
        place_counter += 1
        # adds the value to the accumulator
        acc_count += 1
        print(place_counter)

    elif big_code_dict[place_counter].get(jmp_count).get('operator') == 'jmp':
       #  if jmp_count ==
        place_counter = place_counter + int(big_code_dict[place_counter].get(jmp_count).get('argument'))
        # should jump the numbers
        jmp_count += 1
        print(place_counter)

    elif big_code_dict[place_counter].get(nop_count).get('operator') == 'nop':
        place_counter += 1
        nop_count += 1
        print(place_counter)


print(f"\n{accumulator}")
print(keys_list)
print(max(big_code_dict.keys()))


# if 'operator' == jmp:
#      'operator' = 'nop'
# + while counter == 0, then tick it up and it will finish?

# would this help??????

