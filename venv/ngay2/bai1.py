i=1
tong=0
tongbinhphuong=0
giaithua=1;
for i in range(100):
    tong=tong+i
print(tong)
for i in range(100):
    tongbinhphuong=tongbinhphuong+i*i
print(tongbinhphuong)
print(tong/100)
a=int(input("nhap vao mot so:"))
for i in range(1,a+1):
    giaithua=giaithua*i
print (giaithua)