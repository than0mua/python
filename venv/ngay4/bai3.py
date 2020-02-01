def arearectangle(a,b):
    print (a*b)
def square(a):
    print (a*a)
def factorial(a):
    giaithua = 1
    while a != 0:
        giaithua *= a
        a -= 1
    print(giaithua)

a=int(input("nhap vao so thu 1:"))
b=int(input("nhap vao so thu 2:"))
arearectangle(a,b)
square(a)
factorial(a)
