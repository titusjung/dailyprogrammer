import json
import sys

file = open('workfile.json','r',encoding='utf-8')
jfile = json.load(file)
#testResult = jfile[0]['data']['num_comments']
#print(testResult) 
max =0
min = sys.maxsize
totalComments =0
numItems = 0
for item in jfile:
    numComments = item['data']['num_comments']
    if numComments > max:
        max = numComments
    if numComments < min:
        min = numComments
    totalComments += numComments
    numItems+=1
print("Max is ",max)
print("Min is", min)
print("Average is ",totalComments/numItems)
print("number of comments is ",numItems)

