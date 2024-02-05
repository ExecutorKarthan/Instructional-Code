case_num = int(input("How many cases are there to start?"  ))
case_grow = int(input("How many more cases will show up per day?"  ))
case_recover = int(input("How many cases will recover per day?"  ))

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
