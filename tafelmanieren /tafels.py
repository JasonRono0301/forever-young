
#De eerste opdracht van de tafel lab.
tafelInput = int(input('Type een getal in:'))

if tafelInput > 0:
    for i in range (1,11):
        print(i * tafelInput)
else:
    print('Ongeldige invoer')

print('\n')

#De tweede opdracht van de tafel lab.
for a in range (30,0,-1):
    print(a)

#De derde opdracht van de tafel lab.
for x in range (1,13):
    if x <= 13:
        print(int(x) ,'am')
    else:
        print(int(x),'pm')

#De vierde opdracht van de tafel lab.
for b in range(20,51):
    print(b)
