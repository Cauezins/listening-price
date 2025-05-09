import requests
import os
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from plyer import notification

html = requests.get('https://produto.mercadolivre.com.br/MLB-3245013753-luva-boxe-muay-thai-maximum-new-classic-white-black-_JM', headers={'User-Agent': 'Mozilla/5.0'}).content
html_limpo = BeautifulSoup(html, 'html.parser')

preco_desejado = 300.00

preco_html = html_limpo.select_one('.andes-money-amount__fraction').text.strip() 

preco = float(preco_html.replace('R$', '').replace('.', '').replace(',', '.'))

data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

arquivo = 'historico_precos.csv'
df = pd.DataFrame([[data_atual, preco]], columns=['Data', 'Preco'])

if os.path.exists(arquivo):
    df.to_csv(arquivo, mode='a', header=False, index=False)
else:
    df.to_csv(arquivo, mode='w', header=True, index=False)

if preco < preco_desejado:
    notification.notify(
        title='Preço Baixou!',
        message=f'O produto está por R$ {preco:.2f}!',
        timeout=10
    )
else:
    print(f'Preço atual: R$ {preco:.2f}')