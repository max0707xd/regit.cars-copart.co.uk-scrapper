# from urllib.request import urlopen
from scrapgen import bruteforce
import requests
import bs4

#http address from which we start scrapping
p = 'https://www.regit.cars/car/ae51'

# for this example we are trying to use last 3 letters
# registration plate consists of 7 characters. [AA00BBB]
# and my goal is to find proper BBB combination
# im using https://www.regit.cars/car/ae51aaf seat ibiza for example

r = requests.get(p)
html = bs4.BeautifulSoup(r.text, 'html.parser')

guesses = list(bruteforce('abcdefghijklmnopqrstuvwxyz', 3, 3))
# print(guess)

urls = []
for i, guess in enumerate(guesses[0:25]):
    r = requests.get(p+guess)
    html = bs4.BeautifulSoup(r.text, 'html.parser')
    if len(str(html.title)) > 91:
        print(html.title)
        urls.append([str(html.title) + f'plate number {i}.--------------------'])
print(urls)        

'''
print(len("<title>Find out more about AE51 AAD - value, MOT history, tax and insurance details</title>"))
print(type(html.title))
if len(str(html.title)) == 91:
    print('no vehicle')
else:
    print(html.title)
    

list=list(bruteforce('1234', 4, 3))

for i in range(200):
    #r =requests.get(p+list[i])
    print(p+list[i])
    
    '''