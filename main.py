import requests
import os
import argparse
from dotenv import load_dotenv
from pathlib import Path


def shorten_link(token, url):
    data = {"long_url": url}
    bitly_url = 'https://api-ssl.bitly.com/v4/shorten'
    answer = requests.post(bitly_url,
                           json=data,
                           headers={'Authorization': f'Bearer {token}'})
    answer.raise_for_status()
    return answer.json().get('link')


def count_clicks(token, bitlink):
    data = {'unit': 'day', 'units': -1}
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(bitly_url,
                            params=data,
                            headers={'Authorization': f'Bearer {token}'})
    response.raise_for_status()
    return response.json()['total_clicks']


def get_access_token():
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    return os.getenv("ACCESS_TOKEN")


def read_links_from_args():
    args_parser = argparse.ArgumentParser(description='''This script can get short version 
    of your links or get total clicks for bitlink''')
    args_parser.add_argument("links", type=str, nargs='+',
                             help="links for shorter version or bitlink")
    return args_parser.parse_args().links


def main():
    urls = read_links_from_args()
    access_token = get_access_token()
    for url in urls:
        if url.startswith('bit.ly') or url.startswith('http://bit.ly'):
            try:
                bitlink = url.replace('http://', '')
                total_clicks = count_clicks(access_token, bitlink)
                print(f'Total clicks for {url} : {total_clicks}')
            except requests.exceptions.HTTPError:
                print("Can't get count for bitlink")
        else:
            try:
                bitlink = shorten_link(access_token, url)
                print(f'Your bitlink for {url} : {bitlink}')
            except requests.exceptions.HTTPError:
                print("Can't get a bitlink")


if __name__ == '__main__':
    main()
