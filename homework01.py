n = int(input("Nhập vào số nguyên n:"))
print("Số gấp đôi của n là", 2 * n)
# --- IGNORE ---
import math
a = float(input("Nhập vào số thực a: "))
b = float(input("Nhập vào số thực b: "))
r = float(input("Nhập vào số thực r: "))
diện_tích_hình_chữ_nhật = a * b
diện_tích_hình_tròn = math.pi * r**2
diện_tích_còn_lại = diện_tích_hình_chữ_nhật - diện_tích_hình_tròn
print("Diện tích còn lại là", diện_tích_còn_lại)