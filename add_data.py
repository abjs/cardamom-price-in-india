
from sms import message_to_list_el as sms
from sms import message_to_list_ml as mlsms
from sms import price_message_ml as gensmsml
from sms import price_message_el as gensmsel
from datetime import datetime
import datetime
class IST(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=5, minutes=30)
    def tzname(self, dt):
        return "IST"
    def dst(self, dt):
        return datetime.timedelta()
tz = IST()
Time = datetime.datetime.now(tz)
def cardamom_price_add_to_database(doc,client,db,collection,username):
    if (doc !={}):
        date=doc['date']
        time=doc['time']
        db= client[db]
        collection=db[collection]
        resudlt = collection.find_one({"date":date, "time":time})
        if (not(resudlt)):
            collection.insert_one(doc)
            avgp=doc['avg']
            maxp=doc['max']
            el_1=gensmsel(time,date,maxp,avgp)
            ml_1=gensmsml(time,date,maxp,avgp)
            sms(el_1)
            mlsms(ml_1)
            print(username+" "+time+ ' option price  added successfully \nLog At' +Time.strftime("\nTime : %I:%M %p \nDate:%d/%m/%Y"))
        else:
            print(username+" "+time+' option price is alrary in database \nLog At'+ Time.strftime("\nTime : %I:%M %p \nDate:%d/%m/%Y"))
    else:
        print(username+' Evening option price not yet published \nLog At'+ Time.strftime("\nTime : %I:%M %p \nDate:%d/%m/%Y"))

