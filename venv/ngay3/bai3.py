lis=[]
for i in range(0,10):
    lis.append(i)
for i in lis:
    print(i)
tong=0
for i in lis:
    tong+=i
print (tong)
print(len(lis))
print(max(lis))
print(min(lis))
del(lis[2])
print(lis)
del(lis)
print(lis)