from flask import Flask , render_template , request , jsonify
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as urReq

flipcart_url = "https://www.flipkart.com/search?q="+"iphone11"

response_website = urReq(flipcart_url)
data_flipcart = response_website.read()
beautifyed_html  = bs(data_flipcart,"html.parser")
print(beautifyed_html)

bigbox = beautifyed_html.find_all("div" , {"class":"_1AtVbE col-12-12" })
product6 = "https://www.flipkart.com" + bigbox[6].div.div.div.a['href']
print(product6)
















