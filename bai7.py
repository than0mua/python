a=int(input("nhap vao so dien:"))
if a<=100:
    print("tien dien truoc thue cua ban la:"+str(a*450))
    print("tien luong sau thue cua ban la:" + str(((a*450)/100)*110))
elif a>100 & a<=200:
    print("tien dien truoc thue cua ban la:" + str(a*450+(a-100) * 600))
    print("tien luong sau thue cua ban la:" + str(((a*450+(a-100) * 600) / 100) * 110))
elif a>200 & a<=300:
    print("tien dien truoc thue cua ban la:" + str(a*450+(a-100) * 600+(a-200) * 750))
    print("tien luong sau thue cua ban la:" + str(((a*450+(a-100) * 600+(a-200) * 750) / 100) * 110))
elif a>300 & a<=500:
    print("tien dien truoc thue cua ban la:" + str(a*450+(a-100) * 600+(a-200) * 750+(a-300) * 900))
    print("tien luong sau thue cua ban la:" + str(((a*450+(a-100) * 600+(a-200) * 750+(a-300) * 900) / 100) * 110))
elif a>500 & a<=1000:
    print("tien dien truoc thue cua ban la:" + str(a*450+(a-100) * 600+(a-200) * 750+(a-300) * 900+(a-500) * 1000))
    print("tien luong sau thue cua ban la:" + str(((a*450+(a-100) * 600+(a-200) * 750+(a-300) * 900+(a-500) * 1000) / 100) * 110))
elif a>1000:
    print("tien dien truoc thue cua ban la:" + str(a*450+(a-100) * 600+(a-200) * 750+(a-300) * 900+(a-500) * 1000+(a-1000) * 1200))
    print("tien luong sau thue cua ban la:" + str(((a*450+(a-100) * 600+(a-200) * 750+(a-300) * 900+(a-500) * 1000+(a-1000) * 1200) / 100) * 110))
