import requests

def get_dice_rolls():
    l = []

    for i in range(5):
        r = requests.get('http://rollthedice.setgetgo.com/get.php')
        l.append(r.text)

    return l

result = get_dice_rolls()
print " ".join(result)
