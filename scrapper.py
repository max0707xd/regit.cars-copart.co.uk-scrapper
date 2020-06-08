from urllib.request import urlopen
from scrapgen import bruteforce
import requests

#http address from which we start scrapping
p = 'https://www.regit.cars/car/ae51'

# for this example we are trying to use last 3 letters
# registration plate consists of 7 characters. [AA00BBB]
# and my goal is to find proper BBB combination
# im using https://www.regit.cars/car/ae51aaf seat ibiza for example


list=list(bruteforce('1234', 4, 3))

for i in range(200):
    #r =requests.get(p+list[i])
    print(p+list[i])