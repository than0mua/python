tong=0
n=int(input("nhap vao so chu so muon nhap:"))
for i in range(n):
    a = int(input("nhap vao so nguyen thu:"+str(i)+":"))
    tong+=a
    print(a)
print(tong)
