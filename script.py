import requests
from bs4 import BeautifulSoup

html = requests.get('https://produto.mercadolivre.com.br/MLB-3245013753-luva-boxe-muay-thai-maximum-new-classic-white-black-_JM', headers={'User-Agent': 'Mozilla/5.0'}).content
html_limpo = BeautifulSoup(html, 'html.parser')

price = html_limpo.select_one('.andes-money-amount__fraction').text.strip() 

print(price)