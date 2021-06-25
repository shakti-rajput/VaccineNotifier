import time
from datetime import date
from datetime import timedelta
import requests
from twilio.rest import Client
today = date.today()
res = (today + timedelta(days=10)).strftime("%d-%m-%Y")
print(res)
data = {
    "mobile": "7397xxxxxx"
}
API_ENDPOINT = "https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP"
flag = 1
while flag:
    for x in range(6):
        time.sleep(5)
        res = (today + timedelta(days=x)).strftime("%d-%m-%Y")
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=639&date=" + res
        r = requests.get(url=URL)
        data = r.json()
        centers = (data['centers'])
        print(x)
        for center in centers:
            sessions = center['sessions']
            for session in sessions:
                minAge = int(session['min_age_limit'])
                available_capacity_dose1 = session['available_capacity_dose1']
                if minAge == 18 and available_capacity_dose1 > 0:
                    flag = 0
                    account_sid = "ACef032f6a67bea858exxxxxxxxxxxxxxxx"
                    auth_token = "59bc83108bc9722xxxxxxxxxxxxxx"
                    client = Client(account_sid, auth_token)
                    message = client.messages.create(
                        body="Testing 1, 2, 3",  # Message you send"
                        from_="+1865205xxxx",  # Provided phone number
                        to="+91739732xxxxx")  # Your phone number
                    message.sid
                    break
            if flag == 0:
                break
