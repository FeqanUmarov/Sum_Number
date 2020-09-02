def melumat_al():
    while True:
        try:
            value = int(input("Hər hansı bir reqem ve ya ədəd daxil edin:"))
            hesabla(value)
        except ValueError:
            print("Siz ancaq reqem ve ya eded daxil ede bilersiz!")


def hesabla(value):
    m=0
    for s in range(value):
        m+=s

    print(m)
melumat_al()