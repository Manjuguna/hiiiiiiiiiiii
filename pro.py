all=int(input())
ctrl=pow(2,all)
zol=[]
for i in range(ctrl):
    mll=bin(i).replace("0b","")
    zol.append(mll.zfill(all))
    zol.sort(key=(lambda y:y.count('l')))
for i in zol:
    print(i)
