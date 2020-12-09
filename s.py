import sms
from sms import message_to_list_el as sms
from sms import price_message_ml as gensmsml
from sms import price_message_el as gensmsel
from sms import addMessage as add
from sms import sendSMS as mlsms
import config as env
import pymongo 

client = pymongo.MongoClient(env.Mogo_URL)
db =client["price"]
col = db['today']
# x = col.find({}) 
print(col.find().count() )

# print (data)
# for i in x:
#     print(i)
# print (datetime.datetime.now(tz))
# Time = datetime.datetime.now(tz)
# now = datetime.datetime.now()
# today12am = now.replace(hour=0, minute=0, second=0, microsecond=0 date)
# print(today12am)
# print (Time.strftime("\nTime : %I:%M %p"))
# print(Time.strftime("%d-%m-%Y"))
