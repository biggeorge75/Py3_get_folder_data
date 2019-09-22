import requests

result = requests.get('https://www.idokep.hu/30napos/Budapest')
print(result.content)
