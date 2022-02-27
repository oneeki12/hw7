import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://yummyanime.club/"
URL = "https://yummyanime.club/catalog?page=1"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='anime-column')
    anime = []

    for item in items:
        anime.append(
            {
                'title': item.find('a', class_='anime-title').get_text(),
                'image': HOST + item.find('a', class_='image-block').find('img').get('src'),
                'year': item.find('span', class_='year-block').get_text(),
            }
        )
    return anime

@csrf_exempt
def parser_func():
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            anime.extend(get_data(html.text))
            return anime
    else:
        raise ValueError('Error maybe permission denied')