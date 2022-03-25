from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime
import json

# This program calls CoinMarketCap's API to get the current USD value of Bitcoin and Ethereum, 
# calculates the price of however many Bitcoin and Ethereum you'd like to see the price of,
# and saves it into a text file with the current date and time if you'd like to keep a log of the prices of Bitcoin and Ethereum.

api_key = '982e091c-f241-47d8-aecf-8cec4fec523f'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

while True:

    try:
        btc = float(input('How much Bitcoin would you like to see the price of? '))
        break

    except ValueError:
        print("Enter a valid number.")

while True:

    try:
        eth = float(input('How much Ethereum would you like to see the price of? '))
        break

    except ValueError:
        print("Enter a valid number.")

    

parameters = {
    'symbol': 'BTC,ETH'
}

headers = {

    'Accepts' : 'application/json',
    'X-CMC_PRO_API_KEY': api_key
}

session = Session()
session.headers.update(headers)


try: 
    response = session.get(url, params = parameters)
    data = json.loads(response.text)

    btc_price = str(round(btc * float(data['data']['BTC']['quote']['USD']['price']), 2))
    eth_price = str(round(eth * float(data['data']['ETH']['quote']['USD']['price']), 2))

    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")

    print('Current price of', btc, 'Bitcoin: $' + '{:,.2f}'.format(float(btc_price)))
    
    print('Current price of', eth,  'Ethereum: $' + '{:,.2f}'.format(float(eth_price)))

    while True:

        inp = input('Would you like to save the current prices in a file? y/n ')

        if inp == 'y':

            try: 
                btc_write = str('Price of ' + str(btc) + ' Bitcoin at ' + current_time + ': ' + '$' + '{:,.2f}'.format(float(btc_price)) + '\n')
                eth_write = str('Price of ' + str(eth) + ' Ethereum at ' + current_time + ': ' + '$' + '{:,.2f}'.format(float(eth_price)) + '\n')

                f = open('prices.txt', 'a')
                f.write(btc_write)
                f.write(eth_write)
                f.close()

                print('Thank you for using the BTC and ETH price fetcher / calculator!')
                exit()

            except Exception:
                print("Failed to save file.")

            finally:
                f.close()

        if inp == 'n':
            print('\nThank you for using the BTC and ETH price fetcher / calculator!')
            exit()
        
        else:
            print('Please enter y or n.')
            continue

    

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)





