a1t=int(input())
b1t=pow(2,a1t)
z1t=[]
for i in range(bt1):  
    m1t=bin(i).replace("0b","")
    z1t.append(m1t.zfill(a1t))
    z1t.sort(key=(lambda x:x.count('1')))
for i in z1t:
    print(i)
