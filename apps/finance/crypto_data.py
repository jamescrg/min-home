
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

import config.settings_local


# fetch the data for each asset from the coinmarketcap api
def fetch(symbols):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    params = {
        'symbol': symbols,
        'convert': 'USD',
        'CMC_PRO_API_KEY': config.settings_local.CRYPTO_API_KEY,
    }

    try:
        response = requests.get(url, params=params)
        result = response.json()['data']

    except (ConnectionError, Timeout, TooManyRedirects):
        result = None

    return result


# extract the most relevant data into a smaller dict
# include the name of the symbol in the dict data
def condense(data):
    condensed_data = {}
    for key, val in data.items():
        condensed_data[key] = data[key]['quote']['USD']
        condensed_data[key]['symbol'] = key
        condensed_data[key]['name'] = data[key]['name']
        condensed_data[key]['market_cap'] = condensed_data[key]['market_cap'] / 1000000000
    return condensed_data


# convert the dict to a list and sort the list according
# to the chosen field
def sort(data, ord='market_cap'):

    # convert to a list of dicts
    sequential_data = []
    for key in data.keys():
        sequential_data.append(data[key])

    # sort list of dicts by common key
    sorted_data = sorted(sequential_data, key=lambda k: k[ord], reverse=True)
    return sorted_data