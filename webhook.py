import requests
# https://api.telegram.org/bot{토큰}/setWebhook?url={pythonanywhere}

TOKEN = '1812230637:AAE0sQYZgNLajWyuGAC-HOCo7gAgwj3uI3c'
pythonanywhere = 'jongyun.pythonanywhere.com'
url = f'https://api.telegram.org/bot{TOKEN}/setWebhook?url={pythonanywhere}/telegram'

print(requests.get(url))