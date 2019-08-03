all=int(input())
ctrl=pow(2,alt)
zol=[]
for i in range(ctrl):
    mll=bin(i).replace("0b","")
    zol.append(mll.zfill(all))
    zol.sort(key=(lambada y:y.count('l')))
for i in zol:
    print(i)
