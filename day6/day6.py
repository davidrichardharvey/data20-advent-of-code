def sum_of_question_counts():
    with open('input.txt', 'r') as f:
        array = f.read().split('\n\n')

    # removing new line character.
    cleaned_data = []
    for string in array:
        cleaned_data.append(string.replace('\n', ''))

    total_sum = 0 # variable that will hold total of all sums added together

    # loop for every string in the data, i.e every groups answer in the plane.
    for element in cleaned_data:
        qus_ans = []
        for char in element:
            if char not in qus_ans:
                qus_ans.append(char)
        temp_sum = len(qus_ans)
        total_sum += temp_sum

    return total_sum


def new_soqc():
    with open('input.txt', 'r') as f:
        array = f.read().split('\n\n')

    # removing new line character.
    cleaned_data = []
    for string in array:
        cleaned_data.append(string.split('\n'))

    total_sum = 0

    for element in cleaned_data:
        if len(element) == 1:
            total_sum += len(element[0])
        else:
            group_ans = set(element[0]).intersection(*element[1:])
            total_sum += len(group_ans)


    return total_sum


a = sum_of_question_counts()
print(a)
b = new_soqc()
print(b)