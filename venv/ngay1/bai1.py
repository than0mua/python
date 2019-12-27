sothunhat=int(input("nhap vao so thu nhat:"))
sothuhai=int(input("nhap vao so thu hai:"))
pheptinh=input("nhap vao phep tinh muon thuc hien: + - * /:")
if pheptinh=="+":
    ketqua=sothunhat+sothuhai
elif pheptinh=="-":
    ketqua=sothunhat-sothuhai
elif pheptinh=="*":
    ketqua=sothunhat*sothuhai
elif pheptinh=="/":
    ketqua=sothunhat/sothuhai
else:
    print("phep tinh khong chinh xac")
print("ket qua tinh toan:" +str(ketqua))