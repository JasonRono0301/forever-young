from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:
for i in range(2):
    robotArm.grab()
    for a in range(9):
        robotArm.moveRight()
    robotArm.drop()
    for b in range(5,0,-1):
        robotArm.moveLeft()
    robotArm.grab()
    for c in range(3):
        robotArm.moveRight()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
