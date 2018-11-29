from lxml import etree
import requests

info = list()

bus = input("введите номер автобуса: ")
adress = 'http://www.ot76.ru/mob/getroutestr.php?vt=1&nmar=' + bus
htmlreq = requests.get(adress)

parser = etree.HTMLParser()
doc = etree.HTML(htmlreq.text)
xp = etree.XPath('//td')

for item in xp(doc):
    if item.tag == 'td' and item.text != None:
        info.append(item.text)

# print(info)

for i in range(len(info)):
    if i % 5 == 1:
        print("борт", info[i], "прибудет на остановку", info[i+1], "в", info[i+2], "с задержкой в", info[i+3], "минут")
