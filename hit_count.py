import pandas as pd
import json
import os

file = pd.read_csv('prodata0.csv',encoding='utf8')
name=list(file['name'])
male=list(file['M'])
female=list(file['F'])
sum=list(file['sum'])


dict={}
for i in range(len(name)):
    list1 = []
    list1.append((str(male[i])))
    list1.append (str(female[i]))
    list1.append(str(sum[i]))
    dict[name[i]]=(list1)
dict['台湾']=['0','0','0']
dict['香港']=['0','0','0']
dict['澳门']=['0','0','0']
print(dict)

with open("hits_data4.json",'w',encoding='utf-8') as json_file:
         json.dump(dict,json_file)
         pass