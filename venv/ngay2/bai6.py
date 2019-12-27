a = int(input("nhap vao so nguyen thu:"))
giaithua=1
while a!=0:
    giaithua*=a
    a-=1
print(giaithua)
b=300
while b<=500:
    if(b%7==0):
        if (b == 400):
            break
        if (b == 350):
            continue
        print(b)
    b += 1