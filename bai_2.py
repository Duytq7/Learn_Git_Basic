txt = input("Nhập chuỗi ký tự: ")
def viethoa(str1):
    str_hoa = ""
    for i in str1:
        if i.isupper():
            str_hoa += i
    output = "Ký tự viết hoa: " + str_hoa + " - " + str(len(str_hoa))
    return output

def vietthuong(str1):
    str_thuong = ""
    for i in str1:
        if i.islower():
            str_thuong += i
    output = "Ký tự viết thường: " + str_thuong + " - " + str(len(str_thuong))
    return output

print(viethoa(txt))
print(vietthuong(txt))