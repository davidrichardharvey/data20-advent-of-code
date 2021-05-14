# with open('day7input.txt', 'r') as file:
#     bags = file.readlines()

with open('day7example.txt', 'r') as file:
    bags = file.readlines()

# need something that gets bag colour and bags contained in it as an object
# then need to run a code that counts down through bags and counts all shiny gold bags

line_bags = []

for line in bags:
    # print(line + "next")
    line = line.strip('.')
    line = line.split()
    line_bags.append(line)
# gets each line out separately

# print(line_bags)

bag_details = {}

for line in line_bags:
    # print(line)
    initial_colour = line[0] + ' ' + line[1]
    # gets the first bag colour

    if line[4] == 'no':
        num = 0
        bag_details.update({initial_colour: num})
    # if initial bag contains no more bags, notes it as 0

    count = 3
    bags_count = 1

    temp_dict = {}
    # stores the colour and number

    for word in line:
        if word in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            # print(word)
            number = int(word)
            desc = line[(count+2)]
            bag_col = line[(count+3)]
            colour = str(desc) + ' ' + str(bag_col)
            # gets the description and colour of the secondary bags (one on each run through, for each number)

            # print(colour, number)

            count += 4

            if initial_colour in bag_details.keys():
                temp_obj = bag_details.get(initial_colour)
                temp_obj.append({colour: number})
                bag_details.update({initial_colour: temp_obj})

                # appending the next bag to the values list
                # the replacing the dictionary in bag_details with the new one
            else:
                temp_dict.update({initial_colour: [{colour: number}]})
                # updates the temporary dictionary with the description and colour pair of a new bag

            bag_details.update(temp_dict)
            # adds the temp dict into the permanent dictionary

print(bag_details)

#
# for line in bag_details.keys():
#     print(line, "key")
# for line in bag_details.values():
#     print(line, "value")
#
# # just checking things have worked


list_of_bag_colours = []

for bag in bag_details.keys():
    # print(bag, bag_details.get(bag))
    # prints the bag and bags in the bag (the values)
    if bag_details.get(bag) == 0:
        list_of_bag_colours.append(bag)
    else:
        for bag_dict in bag_details.get(bag):
            # print(bag_dict)

            for a in bag_dict.keys():
                bag_colour = a
            # print(bag_colour)
            for b in bag_dict.values():
                count_of_bags = b
            # print(count_of_bags)

            temp_bag_list = []

            while count_of_bags != 0:
                count_of_bags -= 1
                if bag_colour in bag_details.keys():
                    if bag_details.get(bag_colour) == 0:
                        list_of_bag_colours.append(bag_colour)
                    else:
                        for bag_dict in bag_details.get(bag):
                            # print(bag_dict)

                            for a in bag_dict.keys():
                                bag_colour = a
                            # print(bag_colour)
                            for b in bag_dict.values():
                                count_of_bags = b
                            # print(count_of_bags)
                    temp_bag_list.append(bag_details.get(bag_colour))

            list_of_bag_colours.append(temp_bag_list)
            # this got the next row of bags in, so need to repeat this unless value = 0

shiny_count = 0

for bag in list_of_bag_colours:
    if bag == 'shiny gold':
        shiny_count += 1

print(shiny_count)

# runs for too long!!!



# think i need to make a function for checking through all the bags

# run through the dictionaries (use the key to get the appropriate values and quantities)
# put the values in a list
#   then do the first step again for each value (check the dictionary and get values into a list)
# keep all bags it goes through in a final list
# count all times "gold shiny" appears in the list
