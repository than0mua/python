a=int(input("nhap vao so gio lam viec:"))
b=int(input("nhap vao so luong/gio:"))
tienluong=a*b
if a>40:
    print("tien luong truoc thue cua ban la:"+str(tienluong+tienluong/2))
    print("tien luong sau thue cua ban la:" + str(((tienluong + tienluong / 2) / 100) * 90))
else:
    print("tien luong truoc thue cua ban la:"+str(tienluong))
    print("tien luong sau thue cua ban la:" + str((tienluong/100)*90))
