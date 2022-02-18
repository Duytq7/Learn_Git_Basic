f = open("test1.txt","r")
l = f.read().split()
f.close()

def inchuoi(_list):
    maxlength = ""
    for i in _list:
        if len(i) > len(maxlength):
            maxlength = i
    output = "Chuỗi dài nhất: " + maxlength
    return output

def ghepdong(str1):
    try:
        f = open("test1.txt", "w")
        output = ""
        for i in str1:
            output += i + " "
        f.write(output)
        f.close()
    except:
        print("Error!")
    finally:
        print("Ghi file thành công!")

print(inchuoi(l))
ghepdong(l)