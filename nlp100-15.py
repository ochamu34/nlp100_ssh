import subprocess
with open('popular-names.txt', "r") as f:
    s=f.readlines()
    
    




#確認
res=subprocess.run(['split','-1',10,'popular-names.txt'], text=True)
print(res)