import json
import re
df = [json.loads(line)
        for line in open("jawiki-country.json", 'r', encoding='utf-8')]

for i in range(len(df)):
     if df[i]['title']=='イギリス':
        UK=df[i]['text']

pattern1=r'\[\[Category:(.*?)(?:\|.*?)?\]\]'
Category_name = re.findall(pattern1, UK)
print(Category_name)

#\[\[Category:は開始
#(.*?)は(任意の1文字、0回以上の、直前の文字が0回または1、)＝とりあえず文字
#このままだと'イギリス|*'もでてしまう
#(?:...)をつかって中身を\|と.*?(それ以降)にして、あってもなくてもいいように？をつけて
#\]\]をつけた
