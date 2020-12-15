# Download the helper library from https://www.twilio.com/docs/python/install
import config as env
from backup import b1
def sendSMS(message,to):
    import requests
    url = "https://http-api.d7networks.com/send"
    querystring = {
    "username":env.d7networks_UserName,
    "password":env.d7networks_Password,
    "from":"Test%20SMS",
    "content":message,
    "dlr-method":"POST",
    "dlr-url":"https://4ba60af1.ngrok.io/receive",
    "dlr":"yes",
    "dlr-level":"3",
    "to":to
    }
    headers = {
    'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    if(response.status_code != 200):
        print("fust backup")
        b1(message,to)
def message_to_list_el(mess):
    # sendSMS(mess,env.PHONE_A)#env.PHONE_A is  phone number
    # sendSMS(mess,env.PHONE_B)
    # sendSMS(mess,env.PHONE_AL)
    # sendSMS(mess,env.PHONE_AMMA)
    # sendSMS(mess,env.PHONE_A_JIO)
    print("\nmessege send to amma")
    print("messege is \n"+mess)

# message_to_list_el(mess)
def message_to_list_ml(mess):
    # sendSMS(mess,env.PHONE_PAPPA)
    # sendSMS(mess,env.PHONE_A_JIO)
    print("messege send to pappa")
    print("messege is \n"+mess)

    # print("messege is \n"+mess)
def addMessage(message1 , message2):
    return "\n"+message1 +"\n" + message2
def price_message_ml(time,date,maxprice,avgprice):
    # return "\nതീയതി"+str(date)+"\n"+"പരമാവധി വില" +str(maxprice)+"\n" +"ശരാശരി വില" +str(avgprice)
    return str(date) +"\n" +str(time) +"\n"+ str(maxprice) +"\n" +str(avgprice)
def price_message_el(time,date,maxprice,avgprice):
    return "Date : "+str(date)+"\n"+"Time : "+str(time)+"\n"+"Maximum Price : " +str(maxprice)+"\n" +"Average price : " +str(avgprice)

