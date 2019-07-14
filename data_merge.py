import  pandas as pd

folder1='datedata/'
df1=pd.read_csv(folder1 + '20161111.csv')
df2=pd.read_csv('网吧信息.csv')

#AIMD=pd.merge(df1,df2,on=['SITEID'])
#AIMD.to_csv('xxx.csv')
#print(df1['CUSTOMERNAME'])
users=list(df1['CUSTOMERNAME'])
wangba=list(df2['TITLE'])
users=users[100:300]
wangba=wangba[100:300]
print(users)
print(wangba)

dict={'users':users,'bar':wangba}
df3=pd.DataFrame(dict)
print(df3)
df3.to_csv('info.csv')