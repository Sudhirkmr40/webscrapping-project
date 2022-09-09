from flask import Flask, render_template, request, jsonify

from bs4 import BeautifulSoup as bs

from urllib.request import urlopen as urReq

flipcart_url = "https://www.flipkart.com/search?q=" + "iphone11"

print(flipcart_url)

print(urReq(flipcart_url))

respose_website = urReq(flipcart_url)

print(respose_website)

print(respose_website.read())

data_flipcart = respose_website.read()

print(bs(data_flipcart, "html.parser"))

beautifyed_html = bs(data_flipcart, "html.parser")

print(beautifyed_html)

print(beautifyed_html.find_all("div", {"class": "_1AtVbE col-12-12"}))