import json
import re
df = [json.loads(line)
        for line in open("jawiki-country.json", 'r', encoding='utf-8')]
#https://qiita.com/ys_dirard/items/f08659676bd996401266
#https://hayamihyou.net/linux-command/

for i in range(len(df)):
     if df[i]['title']=='イギリス':
        UK=df[i]['text']
        print(UK)

#[i]番目のtitleがイギリスだったら[i]番目のtextをだす？
