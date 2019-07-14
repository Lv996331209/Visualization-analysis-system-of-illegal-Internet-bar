import  pandas as pd
import  os
folder='data/'
filenames = os.listdir(folder)
count=0
for i  in filenames:
    if "csv" in i:
        df = pd.read_csv(folder + i)
        list_age=list(df['AGE'])
        print(i)
        for j in list_age:
            if j<0:
             print(list_age.index(j))
             count=count+1
print('count:'+str(count))##直接使用未成年人身份证上网的共70788人##895人年龄为负数？？