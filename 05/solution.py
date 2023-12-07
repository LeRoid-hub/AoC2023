def stripper(index, line):
    helper = lines[index].strip().split(":")[1].strip().split("\n")
    result = []
    for i in range(len(helper)):
        result.append(helper[i].strip().split(" "))
    return result


file = open("sample.txt", "r")
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
print(conversions)
rates = [0 for r in range(len(seeds))]

for i in range(len(seeds)):
    old = int(seeds[i])
    for j in range(len(conversions)):
        print("conv ", j)
        for k in range(len(conversions[j])):
            print(old, " - ", range(int(conversions[j][k][1]),(int(conversions[j][k][1])+int(conversions[j][k][2])-1)), old in range(int(conversions[j][k][1]),(int(conversions[j][k][1])+int(conversions[j][k][2])-1)))
            if old in range(int(conversions[j][k][1]),(int(conversions[j][k][1])+int(conversions[j][k][2])-1)):
                diff = old -int(conversions[j][k][1]) 
                print(diff)
                old = int(conversions[j][k][0]) + diff

                rates[i] = old

print(rates)
