import pandas as pd
dataAll=[]
for i in range(1,32):
    dataAll.append('201610'+str("%02d" % i))
for i in range(1,31):
    dataAll.append('201611'+str("%02d" % i))
for i in range(1,32):
    dataAll.append('201612' + str("%02d" % i))
dataAll.reverse()

for key in dataAll:
    print(key)
    # PERSONID,SITEID,XB,CUSTOMERNAME,ONLINETIME,OFFLINETIME,AREAID,BIRTHDAY
    data_path = 'datedata/' + key + '.csv'
    df = pd.read_csv(data_path, encoding='utf-8')
    df = df.dropna()
    # df=df.drop_duplicates
    PERSONID=[];SITEID=[];XB=[];STARTLINETIME=[];OFFLINETIME=[];AREAID=[];AGE=[];TIME=[]
    areaid_tem = []
    for i in range(len(df)):
        if(str(df['AREAID'][i])[-2:]=='.0'):
            areaid_tem.append(str(df['AREAID'][i])[:-2])
        else:
            areaid_tem.append(str(df['AREAID'][i]))
        if((str(df['ONLINETIME'][i]).isdigit()) and (str(df['OFFLINETIME'][i]).isdigit()) and areaid_tem[i].isdigit()
           and str(df['BIRTHDAY'][i]).isdigit() and len(str(df['ONLINETIME'][i]))==14 and len(str(df['OFFLINETIME'][i]))==14):
            datetime = key
            starttime = str(df['ONLINETIME'][i])[-6:]
            endtime = str(df['OFFLINETIME'][i])[-6:]
            birth = str(df['BIRTHDAY'][i])
            if datetime[4:8] >= birth[4:8]:
                age = int(datetime[:4]) - int(birth[:4])
            else:
                age = int(datetime[:4]) - int(birth[:4]) - 1
            if (df['XB'][i] == '男'):
                xb = 1
            else:
                xb = 0
            PERSONID.append(df['PERSONID'][i])
            SITEID.append(df['SITEID'][i])
            XB.append(xb)
            STARTLINETIME.append(df['ONLINETIME'][i])
            OFFLINETIME.append(df['OFFLINETIME'][i])
            TIME.append(str(df['ONLINETIME'][i])[-6:])
            AREAID.append(areaid_tem[i])
            AGE.append(age)

    df2=pd.DataFrame({'STARTLINETIME':STARTLINETIME,'OFFLINETIME':OFFLINETIME})
    starttime_list= list(pd.to_datetime(df2['STARTLINETIME'], format='%Y%m%d%H%M%S'))
    endtime_list= list(pd.to_datetime(df2['OFFLINETIME'], format='%Y%m%d%H%M%S'))
    list0=[str(endtime_list[i]-starttime_list[i]) for i in range(len(starttime_list))]
    list1=[str(int(x.split('day')[0])*24+int(x[-8:-6]))+ x[-6:] for x in list0]
    # print(list1)
    df3=pd.DataFrame({'PERSONID':PERSONID,'SITEID':SITEID,'XB':XB,'STARTLINETIME':TIME,
                      'AREAID':AREAID,'AGE':AGE})
    df3['ONLINETIME']=list1
    df3.to_csv('data/' + key + '.csv',encoding='utf-8')
print('ALL finished!!')