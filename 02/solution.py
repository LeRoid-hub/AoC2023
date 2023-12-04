file = open("input.txt", "r")
lines = file.readlines()

count = 0

#Gamerules
max_red = 12
max_green = 13
max_blue = 14

for line in lines:
    error = False
    print(line)
    
    #Split the line into a list
    line = line.split(":")
    print(line)
    id = int(line[0].split(" ")[1])
    draw = line[1].split(";")
    for i in range(len(draw)):
        color = draw[i].strip().split(" ")
        for i in range(0, len(color),2):
            print(color[i+1])
            if "red" in color[i+1]:
                if int(color[i]) > max_red:
                    print("Error: Too many red cards")
                    error = True
            elif "green" in color[i+1]:
                if int(color[i]) > max_green:
                    print("Error: Too many green cards")
                    error = True
            elif "blue" in color[i+1]:
                if int(color[i]) > max_blue:
                    print("Error: Too many blue cards")
                    error = True
    if error == False:
        count += id
print(count)
count = 0
for line in lines:
    error = False
    red = 0
    green = 0
    blue = 0
    print(line)
    
    #Split the line into a list
    line = line.split(":")
    print(line)
    id = int(line[0].split(" ")[1])
    draw = line[1].split(";")
    for i in range(len(draw)):
        color = draw[i].strip().split(" ")
        for i in range(0, len(color),2):
            print(color[i+1])
            if "red" in color[i+1]:
                if int(color[i]) > red:
                    print("Error: Too many red cards")
                    red = int(color[i])
            elif "green" in color[i+1]:
                if int(color[i]) > green:
                    print("Error: Too many green cards")
                    green = int(color[i])
            elif "blue" in color[i+1]:
                if int(color[i]) > blue:
                    print("Error: Too many blue cards")
                    blue = int(color[i])
    if error == False:
        count += (red * green * blue)
print(count)

