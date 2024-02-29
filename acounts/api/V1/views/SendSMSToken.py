from acounts.api.V1.melipayamak_python_master.melipayamak import Api
import os


def Send_SMS(phone, message):
    username = os.environ('SMS_USERNAME')
    password = os.environ('SMS_PASSWORD')
    api = Api(username, password)
    sms = api.sms()
    to = phone[0]
    _from = '50002710036456'
    # response = sms.send(to = phone, form = '9850002710036456',  50002710036456,  text= message)
    response = sms.send(phone,_from,message)
    print(response)
    print(to)
    print(_from)