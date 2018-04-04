import requests
from main import write_json
import re

def parse_text(text):
    pattern = r'/\w+'
    crypta = re.search(pattern, text).group()
    return crypta[1:]

def get_price(crypta):
    url = 'https://api.coinmarketcap.com/v1/ticker/{}'.format(crypta)
    r = requests.get(url).json()
    price = r[-1]['price_usd']
    #write_json(r.json(), filename='price.json')
    return price



def main():
    #print(get_price())
    print(get_price(parse_text('Сколько стоит /bitcoin')))

if __name__ == '__main__':
    main()
