# W2A4
a1 = float(input("Nhap vao so diem a1: "))
b1 = float(input("Nhap vao so diem b1: "))
c1 = float(input("Nhap vao so diem c1: "))
a2 = float(input("Nhap vao so diem a2: "))
b2 = float(input("Nhap vao so diem b2: "))
a3 = float(input("Nhap vao so diem a3: "))
TB = ((a1 + b1 + c1) + (a2 + b2) * 2 + a3 * 3) / 10
print("Diem trung binh cua hoc sinh la:", TB)
print (round(TB,1))
# W2A6
chu_thuong = input("Nhap vao mot ki tu chu cai thuong: ")
print("Ma Unicode cua ky tu '{}' la: {}".format(chu_thuong, ord(chu_thuong)))
chu_hoa = chr(ord(chu_thuong))
print("Ky tu chu cai in hoa tuong ung la: {}".format(chu_hoa))
# W2A18
print("""### ## ### ###""")
print(""" #  # # #   # """)
print(""" #  # # #   # """)
print(""" #  # # #   # """)
print(""" #  ##  #   #""")
# VD #
a = int(input ("Nhap vao so nguyen duong a:"))
b = int(input ("Nhap vao so nguyen duong b:"))
c = int(input ("Nhap vao so nguyen duong c:"))
if a + b > c and a + c > b and b + c > a:
    print ("3 canh tren co the tao thanh 1 tam giac")   
elif a == b and b == c:
    print ("3 canh tren co the tao thanh 1 tam giac deu")
elif a == b or b == c or a == c:
    print ("3 canh tren co the tao thanh 1 tam giac can")
elif (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
    print ("3 canh tren co the tao thanh 1 tam giac vuong")
else:
    print ("3 canh tren khong the tao thanh 1 tam giac")