import aocd

input = aocd.get_data(day=1, year=2022).split('\n')

calorieslist = []
tmp = 0
for calories in input:
    if calories != "": tmp+=int(calories)
    else:
        calorieslist.append(tmp)
        tmp = 0

calorieslist = sorted(calorieslist, reverse=True)
print("Part One: ", calorieslist[0])
print("Part Two: ", sum(calorieslist[:3]))