def stripper(index, line):
    helper = lines[index].strip().split(":")[1].strip().split("\n")
    result = []
    for i in range(len(helper)):
        result.append(helper[i].strip().split(" "))
    return result


file = open("input.txt", "r")
lines = file.read()
lines = lines.strip()
lines = lines.split("\n\n")

seeds = lines[0].strip().split(":")[1].strip().split(" ")
seed_soil = stripper(1,lines)
soil_fertilizer = stripper(2,lines)
fertilizer_water = stripper(3,lines)
water_light = stripper(4,lines)
light_temperature = stripper(5,lines)
temperature_humidity = stripper(6,lines)
humidity_location = stripper(7,lines)

conversions = [seed_soil,soil_fertilizer,fertilizer_water,water_light,light_temperature,temperature_humidity,humidity_location]
rates = [0 for r in range(len(seeds))]
for i in range(len(seeds)):
    old = int(seeds[i])
    for j in range(len(conversions)):
        for k in range(len(conversions[j])):
            if old in range(int(conversions[j][k][1]),(int(conversions[j][k][1])+int(conversions[j][k][2]))):
                diff = old - int(conversions[j][k][1]) 
                old = int(conversions[j][k][0]) + diff
                rates[i] = old
                break

print("Part 1: ",min(rates))

rates = []
triedSeeds = []
for i in range(0,len(seeds),2):
    print("range ", range(int(seeds[i]),int(seeds[i+1]))) 
    for l in range (int(seeds[i]),int(seeds[i]) + int(seeds[i+1])):
        old = l
        if old in triedSeeds:
            break
        else:
            triedSeeds.append(old)
            for j in range(len(conversions)):
                for k in range(len(conversions[j])):
                    if old in range(int(conversions[j][k][1]),(int(conversions[j][k][1])+int(conversions[j][k][2]))):
                        diff = old - int(conversions[j][k][1]) 
                        old = int(conversions[j][k][0]) + diff
                        rates.append(old)
                        break

print(triedSeeds)
print("Part 2: ",min(rates))
