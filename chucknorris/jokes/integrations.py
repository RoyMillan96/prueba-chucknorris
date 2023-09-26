import requests

def get_fetch_jokes():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    if response.ok:
        data = response.json()
        return data['id'], data['value']