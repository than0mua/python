def cong():
    sothunhat = int(input("nhap vao so thu nhat:"))
    sothuhai = int(input("nhap vao so thu hai:"))
    print("tong:"+str(sothunhat+sothuhai))
def tru():
    sothunhat = int(input("nhap vao so thu nhat:"))
    sothuhai = int(input("nhap vao so thu hai:"))
    print("hieu:" + str(sothunhat - sothuhai))
def nhan():
    sothunhat = int(input("nhap vao so thu nhat:"))
    sothuhai = int(input("nhap vao so thu hai:"))
    print("tich:" + str(sothunhat * sothuhai))
def chia():
    sothunhat = int(input("nhap vao so thu nhat:"))
    sothuhai = int(input("nhap vao so thu hai:"))
    print("tich:" + str(sothunhat / sothuhai))
print("Menu:")
print("1. cong")
print("2. tru")
print("3. nhan")
print("4. chia")
print("5. thoat")
a=0
while a!=5:
    a = int(input("Ban chon chuc nang:"))
    if(a==1):
        cong()
    if(a==2):
        tru()
    if(a==3):
        nhan()
    if (a == 4):
        chia()

