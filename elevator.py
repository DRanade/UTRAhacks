import RPi.GPIO as GPIO
import time as t

def move(distance):
# pin assignments
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(36, GPIO.OUT)




    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(36, GPIO.LOW)


    # insert code for conversion for distance to max value here
    time2 = 0.0
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    t.sleep(0.03)
    neg_dist = False
    if distance < 0.0:
        neg_dist = True
        distance = -distance
        
    while (time2<distance):
        time2 = time2 + 1
        t.sleep(0.001)
        if neg_dist == True:
            time = 8 - (time2%8)
        else:
            time = time2%8
        if time%8==0:
            GPIO.output(16, GPIO.HIGH)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(36, GPIO.LOW)
        elif time%8==1:
            GPIO.output(16, GPIO.HIGH)
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(36, GPIO.LOW)
        elif time%8==2:
            GPIO.output(16, GPIO.LOW)
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(36, GPIO.LOW)
        elif time%8==3:
            GPIO.output(16, GPIO.LOW)
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(22, GPIO.HIGH)
            GPIO.output(36, GPIO.LOW)
            
        elif time%8==4:
            GPIO.output(16, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(22, GPIO.HIGH)
            GPIO.output(36, GPIO.LOW)
            
        elif time%8==5:
            GPIO.output(16, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(22, GPIO.HIGH)
            GPIO.output(36, GPIO.HIGH)
        elif time%8==6:
            GPIO.output(16, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(36, GPIO.HIGH)
        elif time%8==7:
            GPIO.output(16, GPIO.HIGH)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(36, GPIO.HIGH)
            print(time2)


def moveup():
    move(1000)
    return True
    
def movedown():
    move(-1000)
    return True
    
def moveto(currentfloor, floor):
    if floor == 1:
        if currentfloor == 1:
            return True
        if currentfloor == 2:
            movedown()
            return True
        if currentfloor == 3:
            movedown()
            movedown()
            return True
    
    if floor == 2:
        if currentfloor == 1:
            moveup()
            return True
        if currentfloor == 2:
            return True
        if currentfloor == 3:
            movedown()
            return True
    
    if floor == 3:
        if currentfloor == 1:
            moveup()
            moveup()
            return True
        if currentfloor == 2:
            moveup()
            return True
        if currentfloor == 3:
            return True
    
# Elevator Algorithm

# pin assignments
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(33, GPIO.IN)
GPIO.setup(35, GPIO.IN)
GPIO.setup(37, GPIO.IN)

queue = [] # Queue represents a list of lists. The first element in the sublist is the floor
# at which a person is waiting.
# The second element is the floor they want to go to.
in_elevator = [] 

if GPIO.input(11) == GPIO.HIGH:
    queue = queue + [3,2]
if GPIO.input(13) == GPIO.HIGH:
    queue = queue + [3,1]
if GPIO.input(15) == GPIO.HIGH:
    queue = queue + [2,3]
if GPIO.input(33) == GPIO.HIGH:
    queue = queue + [2,1]
if GPIO.input(35) == GPIO.HIGH:
    queue = queue + [1,3]
if GPIO.input(37) == GPIO.HIGH:
    queue = queue + [1,2]

floor = 1 # Start at floor 1.
up = True # Begin by going up.

while queue!=[]: # When there is a person waiting.
    
    if up == True: # If the elevator is going up.
        
        if floor == 1:
            nextfloor = []
            for i in range (0, len(queue)): # Iterate through waiting people
                if queue[i][0] == floor: # I there is anyone waiting in the same floor.
                    in_elevator = in_elevator + queue[i] # Pick up the person
                    queue = queue[0:i] + queue[i:] # Remove Them from the elevator
                if queue[i][1] > floor:
                    nextfloor = nextfloor + [queue[i][0]]
                    
            for i in range (0, len(in_elevator)):
                if in_elevator[i][1] == floor:
                    in_elevator = in_elevator[0:i] + in_elevator[i:]
                if in_elevator[i][1] == floor + 1:
                    nextfloor = nextfloor+[floor + 1]
                if in_elevator[i][1] == nextfloor+[floor + 2]:
                    nextfloor = nextfloor + [floor + 2]
            
            
            
            nextfloor = min(nextfloor)
            moveto(floor, nextfloor)
            floor = nextfloor
            
        if floor == 2:
            nextfloor = []
            for i in range (0, len(queue)): # Iterate through waiting people
                if queue[i][0] == floor: # I there is anyone waiting in the same floor.
                    in_elevator = in_elevator + queue[i] # Pick up the person
                    queue = queue[0:i] + queue[i:] # Remove Them from the elevator
                if queue[i][1] > floor:
                    nextfloor = nextfloor + [queue[i][0]]
                    
            for i in range (0, len(in_elevator)):
                if in_elevator[i][1] == floor:
                    in_elevator = in_elevator[0:i] + in_elevator[i:]
                if in_elevator[i][1] == floor + 1:
                    nextfloor = nextfloor+[floor + 1]
                if in_elevator[i][1] == nextfloor+[floor + 2]:
                    nextfloor = nextfloor + [floor + 2]
            
            nextfloor = min(nextfloor)
            moveto(floor, nextfloor)
            floor = nextfloor
                    
        if floor == 3:
            up = False
            
move(-8000)    
                
            
            
    



    

    