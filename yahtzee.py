import requests

l = []

for i in range(5):
    r = requests.get('http://rollthedice.setgetgo.com/get.php')
    l.append(r.text)

print " ".join(l)
