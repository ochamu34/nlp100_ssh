import random
ram="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
dom=ram.split()

random.shuffle(dom)

for i in dom:
    if len(i)>=4:
        i=list(i[1:-1])
        random.shuffle(i)
        print(''.join(i),end=' ')
    else:
        print(i,end=' ')