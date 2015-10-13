import requests

def get_dice_rolls():
    """ Rolls a 6-sided dice 5 times, using the API, and returns the result """
    l = []

    for i in range(5):
        r = requests.get('http://rollthedice.setgetgo.com/get.php')
        l.append(r.text)

    return l

result = get_dice_rolls()
print ", ".join(result)
