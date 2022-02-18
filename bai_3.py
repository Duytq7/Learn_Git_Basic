txt = input("Nhập chuỗi ký tự: ")
d = dict()
for i in txt:
    d[i] = txt.count(i)
print(d)