from sms import message_to_list_el as sms
from sms import message_to_list_ml as mlsms
from sms import price_message_ml as gensmsml
from sms import price_message_el as gensmsel
from sms import addMessage as add
from backup import data_backup as b
import config as env
def price(userNmae,key):
    from datetime import datetime
    from time import strptime
    import datetime
    import requests as req
    from bs4 import BeautifulSoup as bs4
    import pymongo 
    #Date set up
    class IST(datetime.tzinfo):
        def utcoffset(self, dt):
            return datetime.timedelta(hours=5, minutes=30)
        def tzname(self, dt):
            return "IST"
        def dst(self, dt):
            return datetime.timedelta()
    tz = IST()
    # print (datetime.datetime.now(tz))
    Time = datetime.datetime.now(tz)
    #Date set up End
    #Get Data
    userNmae = userNmae
    html = req.get(env.url)  #url of website
    data = bs4(html.text, 'lxml')
    #Get Data End
    #Data Prossessing
    table = data.select('table')
    data = bs4(str(table[1]), 'lxml')
    tr = data.select('tr')
    new_tr = []
    for i in range(2, len(tr)):
        new_tr.append(tr[i])
    data = bs4(str(new_tr), 'lxml')
    td = data.select('td')
    data = bs4(str(td), 'lxml')
    result = data.select('td')
    key = key
    value = []
    for i in range(1, len(result)+1):
        value.append(result[i-1].get_text())

    datein = value[1].split('-')
    value[1] = str(datein[0])+'-'+str(strptime(datein[1],'%b').tm_mon)+'-'+str(datein[2])
    result =[]
    tem ={}
    lenofkey 	= int(len(key))
    lenofvalue 	= int(len(value))
    Number 	= int(lenofvalue/lenofkey)
    if (Number == 2):
        value[9] = value[1]
    print(value[1]) 
    # j=0
    # for i in value:
    #     tem[key[j]] = i
    #     if (j !=7 ):
    #         j+=1
    #     else:
    #         j=0
    #     result.append(tem)
    #     tem={}
    #Data Prossessing End
    #Data To Mongodb database
    client = pymongo.MongoClient(env.Mogo_URL)
    # update={}
    # update['number']=Number
    # if (Number == 1 ):
    #     update['_id']=value[1]
    # elif(Number == 2 ):
    #     update['_id']=value[1]
    # update[value[1]]=result
    # r =[]
    # r.append(update)
  
    y=[]
    x={}
    j=0
    for i in value:
        tem =str(j)
        x[tem]=i
        j+=1
        if (j==8):
            y.append(x)
            x={}
            j=0
    x =len(y)
    j=0 
    k={} 
    for i in y:
        tem =str(j) 
        k[tem] = i
        j+=1
    k['number']=Number
    k['_id'] =value[1]

    #db = client["price"]
    #collection = db['today']
    #collection.insert_many(r)
    db =client["price"]
    col = db['today']
    x = col.find_one({'_id' : value[1]} ) 
    # Log manegment
    if(x == None):
        client["price"]['today'].insert_one(k)
        print(userNmae +' Data Added successfully \nLog At' +Time.strftime("\nTime : %I:%M %p \nDate:%d/%m/%Y"))
        x = col.find_one({'_id' : value[1]} ) 
        print(x['number'])
        if ( x['number'] == 1):
            date =value[1]
            maxp=value[6]
            avg=value[7]
            el_1=gensmsel(date,maxp,avg)
            ml_1=gensmsml(date,maxp,avg)
            sms(el_1)
            mlsms(ml_1)
        elif ( x['number'] == 2):
            date =value[1]
            maxp=value[6]
            avg=value[7]
            el_1=gensmsel(date,maxp,avg)
            ml_1=gensmsml(date,maxp,avg)
            maxp=value[14]
            avg=value[15]
            el_2=gensmsel(date,maxp,avg)
            ml_2=gensmsml(date,maxp,avg)
            res_1=add(el_1,el_2)
            # print (res_1)
            sms(res_1)
            res_2=add(ml_1,ml_2)
            # print(res_2)
            mlsms(res_2)
        else:
            print("error from null if"+str(x['number']))
        # b()
    elif(x['number'] == 1):
        if ( Number == 2):
           # client["price"]['today'].remove({'_id':value[1]})  
            client["price"]['today'].find_one_and_update({'_id':value[1]},{'$set':k},upsert=True)
            print("Data deted and updated sussfully \nLog At" +Time.strftime("\nTime : %I:%M %p \nDate:%d/%m/%Y"))
            # date =value[1]
            # maxp=value[6]
            # avg=value[7]
            # el_1=gensmsel(date,maxp,avg)
            # ml_1=gensmsml(date,maxp,avg)
            # maxp=value[14]
            # avg=value[15]
            # el_2=gensmsel(date,maxp,avg)
            # ml_2=gensmsml(date,maxp,avg)
            # res_1=add(el_1,el_2)
            # # print (res_1)
            # sms(res_1)
            # res_2=add(ml_1,ml_2)
            # # print(res_2)
            # mlsms(res_2)
            print(Number)
            date =value[1]
            maxp=value[6]
            avg=value[7]
            el_1=gensmsel(date,maxp,avg)
            ml_1=gensmsml(date,maxp,avg)
            maxp=value[14]
            avg=value[15]
            el_2=gensmsel(date,maxp,avg)
            ml_2=gensmsml(date,maxp,avg)
            res_1=add(el_1,el_2)
            # print (res_1)
            sms(res_1)
            res_2=add(ml_1,ml_2)
            # print(res_2)
            mlsms(res_2)
            # b()
        else:
            print(userNmae +' Evening option price not yet published \nLog At'+ Time.strftime("\nTime : %I:%M %p \nDate:%d/%m/%Y"))
            # b()
    elif (x['_id'] == value[1]):
        print(userNmae +' evary thig is upto date \nLog At' + Time.strftime("\nTime : %I:%M %p \nDate:%d/%m/%Y"))
        # b()
    else:
        print(userNmae +' sumthing is wrong \nLog At'+Time.strftime("\nTime : %I:%M %p \nDate:%d/%m/%Y"))
        # b()
    #Log manegment End
    #Date to mongodb database end

def app():
    key=['SL No', 'Date of Auction', 'Auctioneer', 'Number of Lots','Total Qty Arrived (Kgs)', 'Qty Sold (Kgs)', 'Maximum Price (Rs/Kg)', 'Average Price (Rs/Kg)']
    UserNames ='Abin'
    price(UserNames,key)
