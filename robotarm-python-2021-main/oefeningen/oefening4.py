from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for a in range(3):
    for i in range(2):
        robotArm.grab()
        robotArm.moveRight()
    robotArm.drop()
    for b in range(2):
        robotArm.moveLeft()
robotArm.moveRight()
robotArm.moveRight()
for c in range(3):
    for d in range(1):
        robotArm.grab()
        robotArm.moveLeft()
    robotArm.drop()
    for e in range(1):
        robotArm.moveRight()

    

    





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()