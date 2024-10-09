repeat = True
while (repeat):
    try:
        charge_1 = int(input("Write some stuff to be here"))
        repeat = False
    except: 
        print("try again please!")
charge_2 = int(input("Write some stuff to be here"))
distance = int(input("Write some stuff to be here"))
force = ((charge_1 * charge_2) / distance**2)
print("Calculated force: " + str(force))