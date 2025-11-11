# --- BAI 1 ---
n = int(input("Nhập vào số nguyên n: "))
print("Số gấp đôi của n là", 2 * n)
# --- BAI 2 ---
import math
a = float(input("Nhập vào số thực a: "))
b = float(input("Nhập vào số thực b: "))
r = float(input("Nhập vào số thực r: "))
diện_tích_hình_chữ_nhật = a * b
diện_tích_hình_tròn = math.pi * r**2
diện_tích_còn_lại = diện_tích_hình_chữ_nhật - diện_tích_hình_tròn
print("Diện tích còn lại là", diện_tích_còn_lại)
# --- BAI 3 ---
c = input("Nhập vào ký tự c: ")
if c == 'C':
    print("c bằng C")
else:
    print("C bằng c")
# --- BAI 4 ---
c = input("Nhập vào ký tự c: ")
if c.isalpha():
    print("c là ký tự chữ cái")
else:
    print("c không phải ký tự chữ cái")
# --- BAI 5 ---
c = input("Nhập vào chu cai in hoa: ")
if len(c) == 1 and 'A' <= c <= 'Z':
    if c == 'A':
        print ("Khong co chu cai thuong truoc 'a'.")
    else:
        chu_cai_thuong_truoc = chr(ord(c) + 32 - 1)
        print("Chu cai thuong truoc", c.lower(), "la", chu_cai_thuong_truoc)
else:       
    print("Vui long nhap mot chu cai in hoa hop le.")
# --- BAI 6 ---
a = float(input("Nhập vào cạnh a: "))
b = float(input("Nhập vào cạnh b: "))
c = float(input("Nhập vào cạnh c: "))
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c ) / 2
    s = math.sqrt(p * (p-a) * (p - b) * (p-c))
    print("Ba cạnh trên có thể tạo thành một tam giác. Diện tích tam giác S = {s}")
else:
    print("Khong phai 3 canh cua tam giac.")
# --- BAI 7 ---
s = input ("Nhap vao chuoi ki tu thuong (do dai >= 20:")
if len(s) >= 20 
    print ("Chu cai thu 5 la ", s[4])
    print ("Chu cai thu 10 den chu cai thu 9 la: ", s[8])
else: 
    print ("Chuoi qua ngan, phai co do dai >= 20")
# --- BAI 8 ---


