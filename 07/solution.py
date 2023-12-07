file = open("sample.txt", "r")
lines = file.read()
lines = lines.strip()
lines = lines.split("\n")

result = 0
sort_order = {
    "A": 0,
    "K": 1,
    "Q": 2,
    "J": 3,
    "T": 4,
    "9": 5,
    "8": 6,
    "7": 7,
    "6": 8,
    "5": 9,
    "4": 10,
    "3": 11,
    "2": 12
}
sorted = [[] for i in range(7)]
for i in range(len(lines)):
    cards = lines[i].strip().split(" ")[0]
    score = lines[i].strip().split(" ")[1]
    print("cards: ", cards)

    counted = []
    for j in range(len(cards)):
        if [cards[j],cards.count(cards[j])] in counted:
            continue 
        else:
            counted.append([cards[j],cards.count(cards[j])])
    counted.sort(key=lambda x: x[1], reverse=True)
    print("counted: ", counted)
    print(len(counted)) 
    if len(counted) == 1:
        sorted[0].append([cards,score])
    elif len(counted) == 2:
        if counted[0][1] == 4:
            sorted[1].append([cards,score])
        else:
            sorted[2].append([cards,score])
    elif len(counted) == 3:
        if counted[0][1] == 3:
            sorted[3].append([cards,score])
        else:
            sorted[4].append([cards,score])
    elif len(counted) == 4:
        sorted[5].append([cards,score])
    else:
        sorted[6].append([cards,score])
print(sorted)
for i in range(len(sorted)):
    print(sorted[i])
    if not sorted[i] == [None]:
        sorted[i].sort(key=lambda val: sort_order[val[0][0]], reverse=True)
        print(sorted[i])
sorted.reverse()
index = 1
for sort in sorted:
    for i in range(len(sort)):
        if len(sort[i]) > 0:
            result += int(sort[i][1]) * index
            index += 1
print(sorted)
print("Part 1: ", result)
