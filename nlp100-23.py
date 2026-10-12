import json
import re
df = [json.loads(line)
        for line in open("jawiki-country.json", 'r', encoding='utf-8')]

for i in range(len(df)):
     if df[i]['title']=='イギリス':
        UK=df[i]['text']

pattern = r'(={2,4})(.*?)(={2,4})'
result = re.findall(pattern, UK)
print(result)


#https://qiita.com/Tadataka_Takahashi/items/073335639b472d7e782c
#コレクションモジュール使えそう？25とかでも？
