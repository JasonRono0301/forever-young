from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:
for i in range(1,0):
    robotArm.grab()
    for a in range(1,10):
        robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
