# Horrible solution, opened file so each number is a list in a list, needs cleaning up.
with open("day1input.txt","r") as f:
    array = []
    for line in f: # read rest of lines
        array.append([int(x.replace('\n','')) for x in line.split()])

def part1():
    # Because of how i opened the file, had to index each number in the array
    for i in array:
        for j in array:
            if int(i[0]) != int(j[0]):
                if i[0] + j[0] == 2020:
                    answer = (i[0] * j[0])
    return answer


def part2():
    # Because of how i opened the file, had to index each number in the array
    for i in array[0:100]:
        for j in array[100:150]:
            for k in array[150:200]:
                    if i[0] + j[0] + k[0] == 2020:
                        answer = (i[0] * j[0] * k[0])
                        break

                    else:
                        continue

    return answer