def halts(function):
    return True

def g():
    if halts(g):
        while True:
            print("Looping forever.")
    print("Halted")
    
halts(g())