import pandas as pd
from datetime import datetime
dataAll={}
for i in range(1,32):
    dataAll['201610'+str("%02d" % i)]={'PERSONID':[],'SITEID':[],'XB':[],'STARTTIME':[],'ONLINETIME':[],
                                       'AREAID':[],'AGE':[]}
for i in range(1,31):
    dataAll['201611'+str("%02d" % i)]={'PERSONID':[],'SITEID':[],'XB':[],'STARTTIME':[],'ONLINETIME':[],
                                       'AREAID':[],'AGE':[]}
for i in range(1,32):
    dataAll['201612'+str("%02d" % i)]={'PERSONID':[],'SITEID':[],'XB':[],'STARTTIME':[],'ONLINETIME':[],
                                       'AREAID':[],'AGE':[]}
print(sorted(list(dataAll.keys())))
# PERSONID,SITEID,XB,CUSTOMERNAME,ONLINETIME,OFFLINETIME,AREAID,BIRTHDAY
for i in range(14,15):
    print('is---'+str(i)+'---------')
    data_path='data/hydata_swjl_'+str(i)+'.csv'
    df=pd.read_csv(data_path,encoding='utf-8')
    df=df.dropna()
    # df['ONLINETIME'] = [str(x)[:4] + '/' + str(x)[4:6] + '/' + str(x)[6:8] + '/' + str(x)[8:10] + '/' + str(x)[10:12] +
    #                     '/' + str(x)[12:14] for x in df['ONLINETIME']]
    # print(df['ONLINETIME'])
    # df['OFFLINETIME'] = [
    #     str(x)[:4] + '/' + str(x)[4:6] + '/' + str(x)[6:8] + '/' + str(x)[8:10] + '/' + str(x)[10:12] +
    #     '/' + str(x)[12:14] for x in df['OFFLINETIME']]
    df['ONLINETIME_format'] = pd.to_datetime(df['ONLINETIME'],format='%Y%m%d%H%M%S')
    print(df['ONLINETIME_format'][0])
    df['OFFLINETIME_format'] = pd.to_datetime(df['OFFLINETIME'],format='%Y%m%d%H%M%S')
    print(df['OFFLINETIME_format'][0])
    # print(str(df['OFFLINETIME_format'][0]-df['ONLINETIM_format'][0])[-8:])

    for i in range(len(df)):
        print(i)
        # print(df['ONLINETIME'][i])
        datetime=str(df['ONLINETIME'][i])[:8]
        starttime = str(df['ONLINETIME'][i])[-6:]
        endtime=str(df['OFFLINETIME'][i])[-6:]
        birth=str(df['BIRTHDAY'][i])
        onlinetime=str(df['OFFLINETIME_format'][0]-df['ONLINETIME_format'][0])[-8:]
        if datetime[4:8]>=birth:
            age=int(datetime[:4])-int(birth[:4])
        else:
            age=int(datetime[:4])-int(birth[:4])-1
        if(df['XB'][i]=='男'):
            xb=1
        else:
            xb=0
        print(df['PERSONID'][i])
        print(df['SITEID'][i])
        print(xb)
        print(str(df['ONLINETIME'][i])[-6:])
        print(onlinetime)
        print(str(df['AREAID'][i]))
        print(age)
        print('--------------------------------------------')
        # {'PERSONID': [], 'SITEID': [], 'XB': [], 'STARTTIME': [], 'ONLINETIME': [],
        #  'AREAID': [], 'AGE': []}
        dataAll[datetime]['PERSONID'].append(df['PERSONID'][i])
        dataAll[datetime]['SITEID'].append(df['SITEID'][i])
        dataAll[datetime]['XB'].append(xb)
        dataAll[datetime]['STARTTIME'].append(str(df['ONLINETIME'][i])[-6:])
        dataAll[datetime]['ONLINETIME'].append(onlinetime)
        dataAll[datetime]['AREAID'].append(str(df['AREAID'][i]))
        dataAll[datetime]['AGE'].append(age)
        # time0=str(df['ONLINETIME'][i])
        # time1=str(df['OFFLINETIME'][i])
        # time0=datetime.datetime()
        # print(onlinetime,end=' ')
        # print(age)
for key in dataAll.keys():
    df=pd.DataFrame(dataAll[key])
    df.to_csv('dealed-data14/'+str(key)+'.csv',encoding='utf-8')