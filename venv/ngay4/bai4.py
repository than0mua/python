def timmax(a, b ,c):
    max=a
    if(max<=b):
        max=b
    if (max<=c):
        max=c
    print("max la:"+str(max))
def trungbinhcong(a,b,c,d):
    tbc=(a+b+c+d)/4
    print("trung binh cong"+str(tbc))
a=int(input("so thu nhat:"))
b=int(input("so thu hai:"))
c=int(input("so thu ba:"))
d=int(input("so thu bon:"))
timmax(a,b,c)
trungbinhcong(a,b,c,d)