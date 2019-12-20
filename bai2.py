import math
chieudai=int(input("nhap vao chieu dai:"))
chieurong=int(input("nhap vao chieu rong:"))
chuvi=2*(chieudai+chieurong)
dientich=chieudai*chieurong
print("chu vi hinh chu nhat:"+str(chuvi))
print("dien tich hinh chu nhat:"+str(dientich))
canha=int(input("nhap vao canh a:"))
canhb=int(input("nhap vao canh b:"))
canhc=int(input("nhap vao canh c:"))
chuvitamgiac=canha+canhb+canhc
p=chuvitamgiac/2
dientichtamgia=math.sqrt(p*(p-canha)*(p-canhb)*(p-canhc))
print("chu vi:"+str(chuvitamgiac))
print("dien tich:"+str(dientichtamgia))
bankinh=int(input("nhap vao ban kinh:"))
chuvihinhtron=bankinh*2*math.pi
dientichhinhtron=bankinh*bankinh*math.pi
print("chu vi hinh tron:"+str(chuvihinhtron))
print("dien tich hinh tron :"+str(dientichhinhtron))