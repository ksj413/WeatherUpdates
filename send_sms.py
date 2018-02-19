
from twilio.rest import Client
import os
import requests

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Seattle&APPID='+os.environ["OPENWEATHER_API_KEY"]+'&units=imperial')
result = r.json()

weather_info = result['weather'][0]
temp_info = result['main']

account_sid=os.environ["TWILIO_ACCOUNT_SID"]
account_auth_token=os.environ["TWILIO_AUTH_TOKEN"]

client=Client(account_sid, account_auth_token)

client.messages.create(
    to=os.environ["MY_TWILIO_NUMBER"],
    from_=os.environ["TWILIO_NUMBER"],
    body="Today's weather in Seattle \n {} \n Details: {} \n Temperature: {}(min) - {}(max)".format(weather_info['main'], weather_info['description'], temp_info['temp_min'], temp_info['temp_max'])
)
