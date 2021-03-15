with open('day1input.txt', 'r') as f:

    # convert file to list
    f_list = list(f)

    # convert str values into int
    for i in range(len(f_list)):
        f_list[i] = int(f_list[i])

    def sum_two(num, sum_values):
        # search for first element in the list
        for i in range(len(num)):
            # search for second element in the list
            for j in range(i + 1, len(num)):
                # search for the third element in the list
                for k in range(j + 1, len(num)):
                    # if both elements add to 2020, multiply them
                    if num[i] + num[j] + num[k] == sum_values:
                        multi = num[i] * num[j] * num[k]
                        print(f"The sum of {str(num[i])} + {str(num[j])} + {str(num[k])} = {str(sum_values)}")
                        print(f"The multiplication of {num[i]} * {num[j]} * {num[k]} = {multi}")

sum_two(f_list, 2020)



