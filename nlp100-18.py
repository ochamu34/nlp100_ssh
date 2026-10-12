import subprocess

with open('popular-names.txt', "r") as f:
    s=f.readlines()
    b=s.split()
    for i in b:
        n=i[0]
        print(i.count(n))


