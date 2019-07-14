import pandas as pd
import json
import os

folder='data/'
filenames = os.listdir(folder)
count=0
for i in filenames:
    if "csv" in i:
        print(i)
        df = pd.read_csv(folder + i)
        list_age=list(df['AGE'])
        list_time=list(df['ONLINETIME'])
        index=len(list_time)
        unadult=0
        final=[]
        for j in range(index):
            time=list_time[j]
            h, m, s = time.strip().split(":")
            h=int(h)
            m=int(m)
            s=int(s)
            time=h*60+m
            final.append(time)
        dict={}
        for j in final:
            t=final.count(j)
            dict[j]=t
        with open('riverdata/' + i[:-4]+'.json', 'w', encoding='utf-8') as json_file:
            json.dump(dict, json_file)

