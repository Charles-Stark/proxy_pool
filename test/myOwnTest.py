import requests


def get_proxy():
    return requests.get('http://127.0.0.1:5010/get').json().get('proxy')


twitter_url = 'http://twitter.com'

proxy = get_proxy()
resp = requests.get(twitter_url, proxies={'http': 'http://{}'.format(proxy)})
print(resp.text)
print(resp.status_code)
print(proxy)
