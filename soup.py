import os
from ba4 import BeautifuSoup as bs
import requests as req

''' Uncomment the following lines after run the script for the first time'''
'''
os.system("pip install bs4")
os.system("pip python-lxml")
os.system("pip install python-html5lib")
'''
url = req.get('https://google.com')

contents = url.content
soup = bs(contents, "lxml")

finder = soup.find_all("a")
print(finder)
