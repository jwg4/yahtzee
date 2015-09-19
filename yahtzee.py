import requests

r = requests.get('http://rollthedice.setgetgo.com/get.php')
print r.text
