with open('day1input.txt', 'r') as f:

    f_list = list(f)

    #   convert str values into int
    for i in range(len(f_list)):
        f_list[i] = int(f_list[i])

    def sum_two(num, pair_sum):
        # search first element in the list
        for i in range(len(num)-1):
            # search other element in the list
            for j in range(i + 1, len(num)):
                # if both elements add to 2020, multiply them
                if num[i] + num[j] == pair_sum:
                    print(str(num[i]) + " + " + str(num[j]) + " = " + str(pair_sum))
                    multi = num[i] * num[j]
                    print(str(num[i]) + " * " + str(num[j]) + " = " + str(multi))

sum_two(f_list, 2020)

