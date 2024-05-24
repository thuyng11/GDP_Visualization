'''
This module contains functions to fetch data about real GDP
of the United States
'''
import urllib
import requests


def fetch_GDP_data(api_key) -> list:
    """
    Fetches daily adjusted real GDP data

    :param api_key: Alpha Vantage API key.

    Returns:
    Data
    """
    try:
        url = f'http://www.alphavantage.co/query?function=REAL_GDP&interval=annual&apikey={api_key}'

        response = requests.get(url, timeout=10)
        data = response.json()
        return data['data']
    except urllib.error.HTTPError as e:
        print(f'The server couldn\'t fulfill: {0}'.format(e))
    except urllib.error.URLError as e:
        print(f'Failed to download contents of the file: {0}'.format(e))
