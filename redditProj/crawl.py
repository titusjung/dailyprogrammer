import urllib
import urllib.request
import json
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import time
#based on code from http://t-redactyl.io/blog/2015/11/analysing-reddit-data-part-2-extracting-the-data.html
hdr = {'User-Agent': 'osx:r/relationships.single.result:v1.0 (by /u/<uninformednobody>)'}
url =  'https://www.reddit.com/r/relationships/top/.json?sort=top&t=all&limit=1'
req = urllib.request.Request(url,headers=hdr)
response = urllib.request.urlopen(req)
text_data = response.read().decode('utf-8')
#print(text_data)
print(isinstance(text_data,str))
data = json.loads(text_data)
#print(data)
print(" ")
#print(data['data']['children'][0]['data']['name'])
data_all = data['data']['children']

while (len(data_all) <= 800):
    time.sleep(0.1)
    last = data_all[-1]['data']['name']
    url = 'https://www.reddit.com/r/relationships/top/.json?sort=top&t=all&limit=100&after={!s}'.format(last)
    if len(data_all)<10: 
        print(url)
    req =  urllib.request.Request(url, headers=hdr)
    text_data = urllib.request.urlopen(req).read().decode('utf-8')
    data = json.loads(text_data)
    data_all += data['data']['children']

f = open('workfile','w')
#f.write(data_all)
json.dump(data_all,f)
f.close()

print("done")
print(len(data_all))
#
#article_title = []
#article_flairs = []
#article_date = []
#article_comments = []
#article_score = []

#for i in range(0, len(data_all)):
 #   article_title.append(data_all[i]['data']['title'])
#    article_flairs.append(data_all[i]['data']['link_flair_text'])
#    article_date.append(data_all[i]['data']['created_utc'])
#    article_comments.append(data_all[i]['data']['num_comments'])
 #   article_score.append(data_all[i]['data']['score'])
    
#rel_df = DataFrame({'Date': article_date,
  #                  'Title': #article_title,
#                    'Flair': article_flairs,
 #                   'Comments': article_comments,
 #                   'Score': article_score})
#rel_df = rel_df[['Date', 'Title', 'Flair', 'Comments', 'Score']]    
#rel_df[:5]
#print(rel_df[1])