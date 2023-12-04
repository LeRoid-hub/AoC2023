f = open("input.txt", "r")
lines = f.readlines()

m = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        }

value = 0
for line in lines:
    if line == "\n":
        continue

    print(line)
    first_number = None
    last_number = None
    word = ""
    for char in line:

        temp = None
        if char.isdigit():
            temp = char
        else:
            word += char
            for w, z in m.items():
                if word.endswith(w):
                    temp = z

        if temp is not None:
            if first_number is None:
                first_number = int(temp)
            last_number = int(temp)
    value += int(str(first_number) + str(last_number))
    print(value)
