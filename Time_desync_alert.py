import os, datetime, requests, json

url = 'http://worldtimeapi.org/api/timezone/Europe/London'

today = datetime.datetime.now()
today_test = (str(today))

r = requests.get(url)

x = r.json()

API_datetime = x['datetime']
test = API_datetime[11:16]

if test != today_test:
    print("alert")

print(test)
print(today_test[11:16])