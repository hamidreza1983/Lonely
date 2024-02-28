from melipayamak_python_master.melipayamak import Api
import os


def Send_SMS(phone, message):
    username = os.environ.get('SMS_USERNAME')
    password = os.environ.get('SMS_PASSWORD')
    api = Api('989100536456', 'b1g8e49')
    sms = api.sms()
    to = phone[0]
    _from = '50002710036456'
    # response = sms.send(to = phone, form = '9850002710036456',  50002710036456,  text= message)
    response = sms.send('09100536456',_from,message)
    print(response)
    print(to)
    print(_from)