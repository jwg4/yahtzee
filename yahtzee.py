import requests


def get_dice_rolls():
    """ Rolls a 6-sided dice 5 times, using the API, and returns the result """
    l = []

    for i in range(5):
        r = requests.get('http://rollthedice.setgetgo.com/get.php')
        l.append(r.text)

    return l


def display_dice(values):
    print ", ".join(values)


if __name__ == '__main__':
    result = get_dice_rolls()
    display_dice(result)
