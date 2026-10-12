import subprocess
with open('popular-names.txt', "r") as f:
    s=f.readlines()
    for i in range(10):
        aa=s[i]
        for h in range(1):
            print(aa.split()[0])
#確認まだ