def hinhvuong():
    canh = int(input("nhap vao canh cua hinh vuong:"))
    print("dien tich hinh vuong la:"+str(canh*canh))
def hinhchunhat():
    chieudai = int(input("nhap vao chieu dai hinh chu nhat:"))
    chieurong = int(input("nhap vao chieu rong hinh chu nhat:"))
    print("dien tich hinh chu nhat la:" + str(chieurong * chieudai))
def hinhtamgiac():
    chieucao = int(input("nhap vao chieu cao cua tam giac:"))
    canhday = int(input("nhap vao canh day cua tam giac:"))
    print("dien tich hinh chu nhat la:" + str(chieucao * canhday*0.5))
print("Menu:")
print("1.Tính diện tích hình vuông")
print("2. Tính diện tích hình chữ nhật")
print("3. Tính diện tích hình tam giác")
print("4. Thoát")
a=0
while a!=4:
    a = int(input("Ban chon chuc nang:"))
    if(a==1):
        hinhvuong()
    if(a==2):
        hinhchunhat()
    if(a==3):
        hinhtamgiac()

