from flask import Flask , render_template , request , jsonify

from bs4 import BeautifulSoup as bs

from urllib.request import urlopen as urReq

flipcart_url = "https://www.flipkart.com/search?q="+"iphone11"

print(flipcart_url)

print(urReq(flipcart_url))

respose_website =  urReq(flipcart_url)

print(respose_website)

print(respose_website.read())

