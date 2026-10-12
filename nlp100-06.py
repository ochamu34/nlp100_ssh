para="paraparaparadise"
graph="paragraph"

def n_gram(t,n):
   return  {t[i:i+n] for i in range(len(t)-n+1)}

bipara=n_gram(para,2)
bigraph=n_gram(graph,2)

wshugo  = bipara | bigraph
skshugo = bipara & bigraph
sashugo = bipara - bigraph

if "se" in (wshugo or skshugo or sashugo):
   print("あるよ！")
else:
   print("ないよ！")