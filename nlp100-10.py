import subprocess

with open('popular-names.txt', "r") as f:
    s=f.readlines()
    count=len(s)
    print(count)

#確認
res=subprocess.run(['wc', '-l','popular-names.txt'], text=True)
print(res)