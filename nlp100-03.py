hakumai=[]
onigiri="Now I eed a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
nori=onigiri.split()
hakumai.append(nori)

okaka=[len(i) for i in nori]
#↑調べて出てきたけどマジわからんかった
#もう一回調べなおそう

konbu=sorted(okaka,reverse=True)
print(konbu)
print(okaka)
