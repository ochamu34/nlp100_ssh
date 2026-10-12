def n_gram(t,n):
   return  [t[i:i+n] for i in range(len(t)-n+1)]

t="I am an NLPer"
s=t.split()
tri_gram=n_gram(t,1)
bi_gram=n_gram(s,2)

print(tri_gram)
print(bi_gram)

#n-gramって調べたら一番上に答えが出てきちゃう！！
#来年気を付けて!!!

#n=1のときrange(13) になるから、i（インデックス） 0から12 までを順にやってる。
#iが0のときtarget[0:1]（0から1）で"I"
#iが1のときtarget[1:2]（1から0）で" "
#iが2のときtarget[2:3]（2から3）で"a"