import requests
from scrapgen import brutefotce

#http address from which we start scrapping
p = 'https://www.regit.cars/car/ae51'

# for this example we are trying to use last 3 letters
# registration plate consists of 7 characters. [AA00BBB]
# and my goal is to find proper BBB combination
# im using https://www.regit.cars/car/ae51aaf seat ibiza for example

  r = requests.get()