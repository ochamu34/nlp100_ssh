import json
import re
df = [json.loads(line)
        for line in open("jawiki-country.json", 'r', encoding='utf-8')]

for i in range(len(df)):
     if df[i]['title']=='イギリス':
        UK=df[i]['text']


pattern = r'\[\[Category:.*\]\]'
Category = re.findall(pattern, UK)
print(Category)

#.(任意の文字列)が*(0回以上)