a=int(input("nhap vao so dien:"))
if a<=100:
    print("tien dien truoc thue cua ban la:"+str(a*450))
    print("tien luong sau thue cua ban la:" + str(((a*450)/100)*110))
elif a>100 & a<=200:
    print("tien dien truoc thue cua ban la:" + str(a * 600))
    print("tien luong sau thue cua ban la:" + str(((a * 600) / 100) * 110))
elif a>200 & a<=300:
    print("tien dien truoc thue cua ban la:" + str(a * 750))
    print("tien luong sau thue cua ban la:" + str(((a * 750) / 100) * 110))
elif a>300 & a<=500:
    print("tien dien truoc thue cua ban la:" + str(a * 900))
    print("tien luong sau thue cua ban la:" + str(((a * 900) / 100) * 110))
elif a>500 & a<=1000:
    print("tien dien truoc thue cua ban la:" + str(a * 1000))
    print("tien luong sau thue cua ban la:" + str(((a * 1000) / 100) * 110))
elif a>1000:
    print("tien dien truoc thue cua ban la:" + str(a * 1200))
    print("tien luong sau thue cua ban la:" + str(((a * 1200) / 100) * 110))
