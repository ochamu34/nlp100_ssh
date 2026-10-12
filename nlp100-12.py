import subprocess
N=input()
with open('popular-names.txt', "r") as f:
    s=f.readlines()
    for i in range(int(N)):
       print(s[-i])

#確認
res=subprocess.run(['tail', '-n',N,'popular-names.txt'], text=True)
print(res)