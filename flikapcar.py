from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as urReq

from main import beautifyed_html

flipcart_url = "https://www.flipkart.com/search?q=" + "iphone11"

response_website = urReq(flipcart_url)

response_website.read()

data_flipcart = response_website.read()

bigbox = beautifyed_html.find_all("div", {"class": "_1AtVbE col-12-12"})

product6 = "https://www.flipkart.com" + bigbox[6].div.div.div.a['href']

import requests

product66 = requests.get(product6)

product66.encoding = 'utf-8'

bs(product66.text, "html.parser")
