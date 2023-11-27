import aocd

input = aocd.get_data(day=2, year=2022).split("\n")

def checkshape(hand):
    if hand=="A" or hand=="X": point=1
    elif hand=="B" or hand=="Y": point=2
    elif hand=="C" or hand=="Z": point=3
    else: print("error")
    return point

def matchresult(p1, p2):
    if (p1==1 and p2==2)or(p1==2 and p2==3)or(p1==3 and p2==1): result=6
    elif (p1==1 and p2==3)or(p1==2 and p2==1)or(p1==3 and p2==2): result=0
    else: result=3
    return result

def followresult(p1, matchresult):
    if matchresult==1:
        result=0
        if p1==1: p2=3
        elif p1==2: p2=1
        else: p2=2  
    elif matchresult==3:
        result=6
        if p1==1: p2=2
        elif p1==2: p2=3
        else: p2=1
    else: result, p2 = 3, p1
    return p2+result
    
total1, total2 = 0, 0
for pair in input:
    opponent = checkshape(pair[0])
    me = checkshape(pair[-1])
    total1 += me
    total1 += matchresult(opponent, me)
    total2 += followresult(opponent, me)
print(total1, total2)