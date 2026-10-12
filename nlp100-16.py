import subprocess
import random

with open('popular-names.txt', "r") as f:
    s=f.readlines()
    random.shuffle(s)
    print(s[:10])
    
#確認
res=subprocess.run(['shuf', '-n','10','popular-names.txt'], text=True)
print(res)