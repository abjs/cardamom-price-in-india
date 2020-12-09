# Download the helper library from https://www.twilio.com/docs/python/install
import config as env
def sendSMS(message,to):
    import config
    import os
    from twilio.rest import Client
    account_sid = config.TWILIO_ACCOUNT_SID
    auth_token =config.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body=message,
                        from_=config.TWILIO_ACCOUNT_PHONE,
                        to=to
                    )
    print(message.sid)

def message_to_list(mess):
    sendSMS(mess,env.TWILIO_ACCOUNT_PHONE_A)#env.TWILIO_ACCOUNT_PHONE_A is  phone number
    sendSMS(mess,env.TWILIO_ACCOUNT_PHONE_B)
    sendSMS(mess,env.TWILIO_ACCOUNT_PHONE_AL)
    sendSMS(mess,env.TWILIO_ACCOUNT_PHONE_AM)
# message_to_list(mess)


def addMessage(message1 , message2):
    return "\n"+message1 +"\n" + message2
def price_message_ml(date,maxprice,avgprice):
    return "\nതീയതി\t:"+str(date)+"\n" +"പരമാവധി വില\t:" +str(maxprice)+"\n" +"ശരാശരി വില\t:" +str(avgprice)
def price_message_el(date,maxprice,avgprice):
    return "\nDate\t:"+str(date)+"\n" +"Maximum Price\t:" +str(maxprice)+"\n" +"Average price\t:" +str(avgprice)

