from BirdBrain import Finch

def directions(bird):
    headings = []
    motor_count = []
    rotations = 0
    for index in range(0, 360):
        heading = bird.getCompass()
        rotations = bird.setMotors(1,0)
        motor_count += 1
    

def orientation(bird):
    heading = bird.getCompass()
    print("Initial heading: " + str(heading))
    while(heading > 250 and heading < 255):
        heading = bird.getCompass()
        bird.setMotors(1,0)
        heading = bird.getCompass()
        print(heading)
        bird.setMotors(0,0)
    print("Calibrated heading is:" + str(heading))
    return heading

def drive(bird, heading):
    current_distance = bird.getDistance()
    while(current_distance > 5):
        current_heading = bird.getCompass()
        print("The current heading is:" + str(current_heading))
        while(heading > (current_heading+5)):
            bird.setMotors(0, 1)
            current_heading = bird.getCompass()
        while(heading < (bird.getCompass()-5)):
            bird.setMotors(1, 0)
            current_heading = bird.getCompass()
        else:
            bird.setMove('F', 20, 100)
            current_distance = bird.getDistance()

bird = Finch()
bird.setBeak(0, 0, 0)
bird.setTail("all", 0, 0, 0)

oriented_heading = orientation(bird)

drive(bird, oriented_heading)