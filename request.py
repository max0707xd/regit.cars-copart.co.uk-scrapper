import re
import requests
n = requests.get('http://regit.cars/car/ve18nnz')
al = n.text
print(al[al.find('<title>') + 7 : al.find('</title>')])
