a="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
b=a.split()

c={1,5,6,7,8,9,15,16,19}

for i,swk in enumerate(b,start=1):
    if i in c:
       print(i,swk[0])
    else:
        print(i,swk[:2]) 


#アルゴリズムの先生のP113
#[]と{}の違いはリストと辞書