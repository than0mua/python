luong=int(input("nhap vao luong:"))
phucap=int(input("nhap vao phu cap:"))
thunhaptruocthue=luong+phucap
giamtru=9000
thunhapchiuthue=thunhaptruocthue-giamtru
if thunhapchiuthue<=5000:
    thuethunhap=thunhapchiuthue*0.05
elif 10000>=thunhapchiuthue>5000:
    thuethunhap=(thunhapchiuthue-5000)*0.1+5000*0.05
elif 15000>=thunhapchiuthue>10000:
    thuethunhap=(thunhapchiuthue-10000)*0.15+(thunhapchiuthue-5000)*0.1+5000*0.05
elif 20000>=thunhapchiuthue>15001:
    thuethunhap=(thunhapchiuthue-15000)*0.2+(thunhapchiuthue-10000)*0.15+(thunhapchiuthue-5000)*0.1+5000*0.05
elif thunhapchiuthue>=20000:
    thuethunhap=(thunhapchiuthue-20000*0.25)+(thunhapchiuthue-15000)*0.2+(thunhapchiuthue-10000)*0.15+(thunhapchiuthue-5000)*0.1+5000*0.05
thunhapthuclinh = thunhaptruocthue - thuethunhap
print("thue phai nop:"+str(thuethunhap))
print("thu nhap thuc te:"+str(thunhapthuclinh))
