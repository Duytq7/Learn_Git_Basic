txt = input("Nhập dãy số: ")
l = list()
for i in txt.split(","):
    l.append(int(i))
sochan = list()
for i in l:
    if i % 2 == 0:
        sochan.append(i)
def sum(_list):
    tong = 0
    for i in _list:
        tong += i
    return tong
def trungbinhcong(_list):
    return sum(_list)/len(_list)
print("Các số chẵn trong dãy: ",sochan)
print("Tổng các số chẵn: ",sum(sochan))
print("Trung bình cộng các số chẵn: ",trungbinhcong(sochan))