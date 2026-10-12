import json
import re
df = [json.loads(line)
        for line in open("jawiki-country.json", 'r', encoding='utf-8')]

for i in range(len(df)):
     if df[i]['title']=='イギリス':
        UK=df[i]['text']

pattern = r'\{\{基礎情報 国\n([\s\S]*)\n\}\}'
st = re.findall(pattern, UK)

pattern2= r'\|(.*?)\ '
sa = re.findall(pattern2, st[0])
print(sa)


#\nは改行
#https://www.www-creators.com/archives/2589