import math
r=input("nhap vao canh ben thu nhat:")
s=input("nhap vao canh ben thu hai:")
q=input("nhap vao canh day thu nhat:")
p=input("nhap vao canh day thu hai:")
chuvi=r+s+q+p
dientich=(q+p)* math.sqrt(2*(r*r*s*s+r*r*(p-q)*(p-q))-(r*r*r*r+s*s*s*s+(p-q)*(p-q)*(p-q)*(p-q)))
print("chu vi hinh thang"+str(chuvi))
print("dien tich hinh thang:" +str(dientich))