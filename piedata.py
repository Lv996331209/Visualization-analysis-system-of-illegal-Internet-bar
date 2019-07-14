import pandas as pd
import json
import os

folder='data/'
filenames = os.listdir(folder)
name = ['男/0-17', '男/18-25', '男/26-34', '男/35-44', '男/45+', '女/0-17', '女/18-25', '女/26-34', '女/35-44', '女/45+']
kind=['AGE<18','AGE>=18 & AGE<25','AGE>=26 & AGE<34','AGE>=35 & AGE<44','AGE>=45']
for i in filenames:
    if "csv" in i:
        print(i)
        df = pd.read_csv(folder + i)
        list_age=list(df['AGE'])
        length=len(list_age)
        count=[]
        count2=[]
        for trans in kind:
            df1 = df.query(trans)
            list_sex = list(df1['XB'])
            all=len(list_sex)
            count.append(sum(list_sex))
            count2.append(all-sum(list_sex))
        count=count+count2
        dict = {'allusers': name, 'count': count}
        df3 = pd.DataFrame(dict)
        df3.drop(1)
        print(df3)
        df3.to_csv(path_or_buf='piedata/' + i,header=None,index=None)
    else:
        print(i)