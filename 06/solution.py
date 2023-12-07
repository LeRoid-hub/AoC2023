def prod(list):
    result = 1
    for i in range(len(list)):
        result *= list[i]
    return result

def glue(list):
    result = ""
    for i in range(len(list)):
        result += str(list[i])
    return int(result)

file = open("input.txt", "r")
lines = file.read()
lines = lines.strip()
lines = lines.split("\n")

time = list(filter(None, lines[0].strip().split(":")[1].strip().split(" ")))
distance = list(filter(None, lines[1].strip().split(":")[1].strip().split(" ")))
result = []
for i in range(len(time)):
    t = int(time[i])
    d = int(distance[i])
    solutions = 0
    for j in range(t):
        l = j * (t-j)
        if l > d:
            solutions += 1
    result.append(solutions)
print("Part 1: ", prod(result))
time = glue(time)
distance = glue(distance)
print("time: ", time)
print("distance: ", distance)
solutions = 0

for j in range(time):
    print("percentage: ", j/time)
    l = j * (time-j)
    if l > distance:
        solutions += 1
print("Part 2: ", solutions)
