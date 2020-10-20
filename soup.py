import os
from ba4 import BeautifuSoup as bs
import requests as req

''' Uncomment the following lines after run the script for the first time'''
'''
os.syste("pip install bs4")
os.syste("pip python-lxml")
os.syste("pip install python-html5lib")
'''
url = req.get('https://google.com')

contents = url.content
soup = bs(content, "lxml")

finder = soup.find_all("a")
print(finder)
