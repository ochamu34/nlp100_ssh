def cipher():
    isl=str(input())
    for i in isl:
        if i.islower():
            print(ord(i))
        else:
            print(i)

cipher()
    