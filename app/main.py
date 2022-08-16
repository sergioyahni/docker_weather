from read_api import GetWeather
from document_creator import Html
from mail import Send
import config

weather = GetWeather()
df = weather.weather()
doc = Html()
send = Send(mail=config.email, password=config.psw, smtp_server='smtp.gmail.com')

today = df.iloc[0]
content = doc.body(df,
               min=today['temperature_min'],
               max=today['temperature_max'],
               sunrise=today['sunrise'],
               sunset=today['sunset'])
send.send_email(to=['sergioy@tourism.gov.il', 'sergioyahni@gmail.com', 'sergioyahni2@gmail.com'],
                subject="Your Weather Report",
                rich_body=content)
