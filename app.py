from sms import message_to_list_el as sms
from sms import message_to_list_ml as mlsms
from sms import price_message_ml as gensmsml
from sms import price_message_el as gensmsel
from sms import addMessage as add
from backup import data_backup as b
import config as env
def price(userNmae):
    from time import strptime
    import datetime
    import requests as req
    from bs4 import BeautifulSoup as bs4
    import pymongo
    userNmae = userNmae
    html = req.get(env.url)  # url of website
    data = bs4(html.text, 'lxml')
    # Get Data End
    # Data Prossessing
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
    value = []
    for i in range(1, len(result)+1):
        value.append(result[i-1].get_text())
    datein = value[1].split('-')
    value[1] = str(datein[0])+'-' + \
        str(strptime(datein[1], '%b').tm_mon)+'-'+str(datein[2])
    result = []
    lenofvalue = int(len(value))
    Number = lenofvalue/8
    day = datein[0]
    month = str(strptime(datein[1], '%b').tm_mon)
    year = str(datein[2])
    morning = {}
    evening = {}
    if (Number == 1):
       morning['seller'] =value[2]
       morning['lots'] =value[3]
       morning['arrived'] =value[4]
       morning['sold'] =value[5]
       morning['max'] =value[6]
       morning['avg'] =value[7]
       morning['time']="morning"
       morning['day']=day
       morning['month']=month
       morning['year']=year
       morning['date']=value[1]
    if (Number == 2):
        morning['seller'] =value[2]
        morning['lots'] =value[3]
        morning['arrived'] =value[4]
        morning['sold'] =value[5]
        morning['max'] =value[6]
        morning['avg'] =value[7]
        morning['time']="morning"
        morning['day']=day
        morning['month']=month
        morning['year']=year
        morning['date']=value[1]
        evening['seller'] =value[10]
        evening['lots'] =value[11]
        evening['arrived'] =value[12]
        evening['sold'] =value[13]
        evening['max'] =value[14]
        evening['avg'] =value[15]
        evening['time']="evening"
        evening['day']=day
        evening['month']=month
        evening['year']=year
        evening['date']=value[1]
    from add_data import cardamom_price_add_to_database as add
    from config import db
    from config import collection
    client = pymongo.MongoClient(env.Mogo_URL)
    add(morning,client,db,collection,userNmae)
    add(evening,client,db,collection,userNmae)
def app():
    # key=['SL No', 'Date of Auction', 'Auctioneer', 'Number of Lots','Total Qty Arrived (Kgs)', 'Qty Sold (Kgs)', 'Maximum Price (Rs/Kg)', 'Average Price (Rs/Kg)']
    price('Abin')
