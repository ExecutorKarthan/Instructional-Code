import random
import io

controlMaps = ["Ilios", "Lijiang", "Oasis", "Nepal", "Antarctic Peninsula"]
escortMaps = ["Circuit Royal", "Dorado", "Havana", "Route 66", "Watchpoint", "Junkertown", "Shambali Monastery", "Rialto"]
hybridMaps = ["Eichenwalde", "King's Row", "Midtown", "Paraiso", "Hollywood", "Numbani", "Blizzard World"]
pushMaps = ["Colloseo", "New Queen Street", "Esperanca"]
mapList = [controlMaps, escortMaps, hybridMaps, pushMaps]
previousValues = {0:False, 1:False, 2:False, 3:False}

roundList = []
for round in range(0, 8):
    current_round = []
    round_cont = True
    while(round_cont):
        for index in range(0, 4):
            if(previousValues.get(index) == True):
                round_cont = False
                break
            else:
                round_cont = True
        randMapIndex = random.randint(0, 3)
        while(previousValues.get(randMapIndex)):
            randMapIndex = random.randint(0, 3)
        for value in range(0, 10):
            random.shuffle(controlMaps)
            random.shuffle(escortMaps)
            random.shuffle(hybridMaps)
            random.shuffle(pushMaps)
        current_round.append(mapList[randMapIndex][0])    
        previousValues.update({randMapIndex: True})
        
print("pause")