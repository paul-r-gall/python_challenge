from lxml import html
import requests

default = "and the next nothing is "
def check(s):
    if s[:len(default)] == default:
        return (s[len(default):])
    else:
        return None
#page=requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345").text
urlBase = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
url = urlBase + str(63579)
while True:
    page = requests.get(url).text
    newNum = check(page)
    if newNum == None:
        print(page)
        break
    print(newNum)
    url=urlBase + str(newNum)
