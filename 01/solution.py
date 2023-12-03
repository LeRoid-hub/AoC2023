f = open("sample.txt", "r")
lines = f.readlines()

numbers = ["one","two","three","four","five","six","seven","eight","nine"]
numbers_int = [1,2,3,4,5,6,7,8,9]

value = 0
for line in lines:
    print(line)
    first_number = None
    last_number = None
    replace = []
    replace_pos = []
    replace_with = []
    for number in numbers:
        if number in line:
            replace.append(number) 
            replace_with.append(str(numbers_int[numbers.index(number)]))
            replace_pos.append(line.index(number))

    if len(replace) > 0:
        last = 0
        for i in range(len(replace_pos)):
        current = 0
            for j in range(len(replace_pos)):
                if replace_pos[i] > last and replace_pos[i] < current:
                    current = replace_pos[i]
                #swap shit


        help = line
        help = help.replace(replace[0],replace_with[0])
        if replace[-1] in line:
            help = help.replace(replace[-1],replace_with[-1])
        line = line.replace(line,help)

    print(line)
    print(lines)
    for char in line:
        #print(char)
        if char.isdigit():
            if first_number is None:
                first_number = int(char)
            last_number = int(char)
    #print(str(first_number) + str(last_number))
    value += int(str(first_number) + str(last_number))
    #print(value)
