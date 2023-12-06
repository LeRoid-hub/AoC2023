file = open("sample.txt", "r")
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
for i in range(len(lines)):
    for j in range(len(lines[i])):
        numbers = 0
        star_score = 1
        if lines[i][j] == "*":
            if lines[i-1][j-1].isnumeric() and lines[i-1][j+1].isnumeric():
                if lines[i-1][j].isnumeric():
                    star_score *= int(lines[i][j-1:j+1])
                    numbers += 1
                else:
                    if lines[i-1][j-3].isnumeric():
                        star_score *= int(lines[i-1][j-3:j-1])
                    else:
                        star_score *= int(lines[i-1][j-2:j-1])
                    if lines[i-1][j+3].isnumeric():
                        star_score *= int(lines[i-1][j+1:j+3])
                    else:
                        star_score *= int(lines[i-1][j+1:j+2])
                    numbers += 2
            elif lines[i-1][j].isnumeric():
                if lines[i-1][j-1].isnumeric():
                    if lines[i][j-2].isnumeric():
                        star_score *= int(lines[i][j-2:j])
                    else:
                        star_score *= int(lines[i][j-1:j])
                else:
                    if lines[i][j-2].isnumeric():
                        star_score *= int(lines[i][j-2:j])
                numbers += 1
            elif lines[i-1][j-1].isnumeric():
                if lines[i-1][j-3].isnumeric():
                    star_score *= int(lines[i-1][j-3:j-1])
                else:
                    star_score *= int(lines[i-1][j-2:j-1])
                numbers += 1
            elif lines[i-1][j+1].isnumeric():
                if lines[i-1][j+3].isnumeric():
                    star_score *= int(lines[i-1][j+1:j+3])
                else:
                    star_score *= int(lines[i-1][j+1:j+2])
                numbers += 1
            if lines[i][j-1].isnumeric():
                if lines[i][j-3].isnumeric():
                    star_score *= int(lines[i][j-3:j-1])
                else:
                    star_score *= int(lines[i][j-2:j-1])
                numbers += 1
            if lines[i][j+1].isnumeric():
                if lines[i][j+3].isnumeric():
                    star_score *= int(lines[i][j+1:j+3])
                else:
                    star_score *= int(lines[i][j+1:j+2])
                numbers += 1
            if lines[i+1][j-1].isnumeric() and lines[i+1][j+1].isnumeric():
                if lines[i+1][j].isnumeric():
                    star_score *= int(lines[i][j-1:j+1])
                    numbers += 1
                else:
                    if lines[i+1][j-3].isnumeric():
                        star_score *= int(lines[i+1][j-3:j-1])
                    else:
                        star_score *= int(lines[i+1][j-2:j-1])
                    if lines[i+1][j+3].isnumeric():
                        star_score *= int(lines[i+1][j+1:j+3])
                    else:
                        star_score *= int(lines[i+1][j+1:j+2])
                    numbers += 2
                

        if numbers == 2:
            print(star_score)
            score += star_score
        numbers = 0
        star_score = 1



