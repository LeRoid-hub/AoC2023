file = open("input.txt", "r")
lines = file.read()
lines = lines.strip()
lines = lines.split("\n")

score = 0
for line in lines:
    play = line.strip().split(":")
    card = play[0].strip().split(" ")[1]
    play = play[1].strip().split("|")
    
    winning = play[0].strip().split(" ")
    game = play[1].strip().split(" ")
    lscore = 0
    while "" in winning:
        winning.remove("")
    while "" in game:
        game.remove("")
    for w in winning:
        if w in game:
            if lscore > 0:
                lscore =lscore + lscore
            else:
                lscore = 1
    if lscore >0:
        score += lscore
    lscore = 1
print(score)

scratchcards = [1 for r in range(len(lines))]
score = 0
for index,line in enumerate(lines,start=0):
    play = line.strip().split(":")
    card = play[0].strip().split(" ")[1]
    play = play[1].strip().split("|")
    
    winning = play[0].strip().split(" ")
    game = play[1].strip().split(" ")
    lscore = 0
    while "" in winning:
        winning.remove("")
    while "" in game:
        game.remove("")
    for w in winning:
        if w in game:
            lscore += 1
    for i in range((lscore)):
        scratchcards[index + i +1] = scratchcards[index + i + 1] + scratchcards[index]
for sc in scratchcards:
    score += sc
print(score)
