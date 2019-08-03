alt=int(input())
ctrl=pow(2,alt)
zoo=[]
for i in range(ctrl):
    mlt=bin(i).replace("0b","")
    zoo.append(mlt.zfill(alt))
    zoo.sort(key=(lambada y:y.count('l')))
for i in zoo:
    print(i)
