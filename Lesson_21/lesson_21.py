import requests
from datetime import datetime

start = datetime.now()
response = requests.get('https://reqres.in/api/users', headers={'accept': 'application/json'})
print(response)
end = datetime.now()
print(end - start)
