import subprocess
with open('popular-names.txt', "r") as f:
    s=f.readlines()
    for i in range(10):
        a=str.maketrans("\t"," ")
        print(s[i].translate(a))

