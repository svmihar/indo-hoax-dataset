import requests
import random
from bs4 import BeautifulSoup
import datetime

# TODO
# get last page on the new site

user_agent_list = open('user-agents.txt').read().splitlines()

headers = {'User-Agent': random.choice(user_agent_list)}

class Link:
    def __init__(self, last_page):
        self.last_page = last_page
        self.link = 'https://www.turnbackhoax.id/page'
        self._FILE_NAME = datetime.datetime.now().strftime('%d-%m-%y')

    def generate_txt(self):
        print(f'getting {len(self.last_page)} pages...')
        for i in self.last_page:
            link = f'{self.link}/{i}'
            r = requests.get(link, headers = headers, veryfi=False)
            s = BeautifulSoup(r.content, 'lxml')
            a = soup.find_all('a', {'rel': 'bookmark'})
            hoaxes = [x['href'] for x in a]
        print(f'found {len(hoaxes)} links')
        print(f'now writing to {self._FILE_NAME}_hoax_links}')
        with open(f'{self._FILE_NAME}_hoax_links') as f:
            for l in hoaxes:
                f.writelines(l+'\n')

    def get_last_page(self):
        pages = list(range(1, 162))
        return pages

    def run(self):
        pass


class Paragraf:
    def __init__(self, path_to_links):
        self.links = open(path_to_links).read().splitlines()

    def get_paragraf(self, link):
        r = requests.get(link, verify=False)
        soup = BeautifulSoup(r.content, 'lxml')
        isi = soup.find('div', {'class': 'entry-content mh-clearfix'})
        kumpulan_p = isi.find_all('p')
        paragrafs = [p.text for p in kumpulan_p]
        return " ".join([p for p in paragrafs if not p == '==='])

    def run(self):
        pass