import requests


def brute_force(page_url: str):
    fois = "fois"
    increment = 0
    url = ""
    while fois == "fois":
        increment += 1
        page_url = "http://univcergy.phpnet.org/scenario3/811193524111958/index.php?open=" + str(increment) + \
                   "&action=Donne+moi+la+solution"
        print(page_url)
        url = requests.get(page_url)
        fois = url.text.split('.mp3')[0][-4:]

    return url


if __name__ == '__main__':
    brute_force('http://univcergy.phpnet.org/scenario3/811193524111958/index.php?open=')
