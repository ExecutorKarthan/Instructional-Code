import random

controlMaps = ["Ilios", "Lijiang", "Oasis", "Nepal", "Antarctic Peninsula"]
escortMaps = ["Circuit Royal", "Dorado", "Havana", "Route 66", "Watchpoint", "Junkertown", "Shambali Monastery", "Rialto"]
hybridMaps = ["Eichenwalde", "King's Row", "Midtown", "Paraiso", "Hollywood", "Numbani", "Blizzard World"]
pushMaps = ["Colloseo", "New Queen Street", "Esperanca"]
mapList = [controlMaps, escortMaps, hybridMaps, pushMaps]
previousValues = {0:False, 1:False, 2:False, 3:False}

roundList = []
for round in range(0, 9):
    current_round = []
    previousValues = {0:False, 1:False, 2:False, 3:False}
    round_cont = True
    while(round_cont):
        if(previousValues.get(0) == True and previousValues.get(1) == True and previousValues.get(2) == True and previousValues.get(3) == True):
            round_cont = False
            break
        else:
            round_cont = True
        randMapIndex = random.randint(0, 3)
        test = previousValues.get(randMapIndex) == True
        while(round_cont == True and previousValues.get(randMapIndex) == True):
            randMapIndex = random.randint(0, 3)
        for value in range(0, 10):
            random.shuffle(controlMaps)
            random.shuffle(escortMaps)
            random.shuffle(hybridMaps)
            random.shuffle(pushMaps)
        current_round.append(mapList[randMapIndex][0])    
        previousValues.update({randMapIndex: True})
    roundList.append(current_round)
for round in roundList:
    print(round)        