attack_speed = int(input("How many attacks can the hero do per second?"  ))
unit_of_time = input("What unit of time are you using? Select from seconds, minutes, hours or days.")
damage_per_hit = int(input("How much damage does the hero do per hit??"  ))
crit_frequency = int(input("What percent of the time does the hero critically strike? Express this as a number between 0 and 100!"  ))

def function(speed, unit, dph, crit):
    converter = 1
    if(unit == "minute"):
        converter = 60
    if(unit == "hour"):
        converter = 3600
    if(unit == "hour"):
        converter = 86400
    total_hits = converter*speed

count = 0
case_origin = case_num

while(case_num > 0):
    if(case_num > case_origin):
        break
    case_num = case_num - case_recover + case_grow
    count += 1
    
if(case_num > case_origin):
    print("The case count will never reach zero - it will just keep growning.")
else:  
    print("It will take", count, "many days until all cases are closed.")
