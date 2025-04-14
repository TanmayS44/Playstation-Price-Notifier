import requests, pprint
from bs4 import BeautifulSoup
from time import sleep

FIRST_URL = "https://psdeals.net/in-store/all-games/1?platforms=ps5%2Cps4&sort=release-date-newest"
BASE_URL = "https://psdeals.net"

def parse_names(names: list):
    for name in names:
        game_name = name.text.strip()
        pprint.pp(game_name)

def parse_platforms(available_platforms: list):
    for platform in available_platforms:
        relevant_platforms = platform.text.strip()
        main_platform = "PS5" if "PS5" in relevant_platforms else "PS4"
        pprint.pp(main_platform)

def save_game_data(current_url):

    while current_url:

        r = requests.get(current_url)

        soup = BeautifulSoup(r.content, 'html.parser')

        names = soup.select('.game-collection-item-details-title')
        available_platforms = soup.select('.game-collection-item-top-platform')

        parse_names(names)
        parse_platforms(available_platforms)

        next_page = soup.select_one('.next a')

        if next_page is None:
            current_url = None
        else:
            next_page_link = next_page.get('href')
            current_url = f"{BASE_URL}{next_page_link}"
        
        sleep(10)

save_game_data(FIRST_URL)
