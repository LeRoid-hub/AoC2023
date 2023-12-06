file = open("input.txt", "r")
lines = file.read()
lines = lines.strip()
lines = lines.split("\n")
score = 0
for i in range(len(lines)):
    start = None
    end = None
    for j in range(len(lines[i])):
        if lines[i][j].isnumeric():
            if start == None:
                start = j
                end = j
            else:
                end = j
        if not lines[i][j].isnumeric() or j == len(lines[i])-1:
            if start != None:
                serial = False
                for z in range(start-1,end+2):
                    if z <0 or z >= len(lines[i]):
                        continue
                    if not lines[i][z].isnumeric() and not lines[i][z] == ".":
                        serial = True
                    if i > 0 and not lines[i-1][z].isnumeric() and not lines[i-1][z] == ".":
                        serial = True
                    if i < len(lines)-1 and not lines[i+1][z].isnumeric() and not lines[i+1][z] == ".":
                        serial = True
                if serial:
                    score += int(lines[i][start:end+1])
                serial = False
                start = None
                end = None
print(score)
score = 0
numbers = [[[0 for k in range(1)] for j in range(len(lines))] for i in range(len(lines[0]))]
print(numbers)
for i in range(len(lines)):
    start = None
    end = None
    for j in range(len(lines[i])):
        if lines[i][j].isnumeric():
            if start == None:
                start = j
                end = j
            else:
                end = j
        if not lines[i][j].isnumeric() or j == len(lines[i])-1:
            if start != None:
                serial = False
                for z in range(start-1,end+2):
                    if z <0 or z >= len(lines[i]):
                        continue
                    if lines[i][z] == "*":
                        numbers[i][z].append(int(lines[i][start:end+1])) 
                    if i > 0 and lines[i-1][z] == "*":
                        numbers[i-1][z].append(int(lines[i][start:end+1]))
                    if i < len(lines)-1 and lines[i+1][z] == "*":
                        numbers[i+1][z].append(int(lines[i][start:end+1]))
                serial = False
                start = None
                end = None
print(numbers)
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if len(numbers[i][j]) == 3:
            score += numbers[i][j][1] * numbers[i][j][2]
print(score)

