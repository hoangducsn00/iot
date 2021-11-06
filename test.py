import traceback

import requests

URL_Authenticate = 'http://203.171.20.94:8901/api/DeviceController/Authenticate'
URL_UpDate = 'http://203.171.20.94:8901/api/DeviceController/UpdateDeviceState'

header = {'Content-type': 'application/json'}
body = {
    'username': 'test',
    'password': 'test'
}



try:
    response = requests.post(URL_Authenticate, headers=header, json = body)
    responseData = response.json()
    print("Response from Authenticate: ")
    print(responseData)
    print('\n')
    token = responseData['token']
    header = {
        'Content-type': 'application/json',
        'Authorization': 'Bear ' + token
    }

    body = {
        "Imei": "10200ed25a298b5f",
        "ReceiveTime": "20210920:11:28:00",
        "Latitude": 20.9,
        "Longitude": 105.8,
        "State": "OK",
        "PinPercentage": 51,
        "UserName": "Admin"
    }
    response = requests.post(URL_UpDate, headers=header, json=body)
    print('sau update HEHE:')
    print(response.text)
except:
    print(traceback.format_exc())
