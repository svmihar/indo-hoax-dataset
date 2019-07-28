import requests, random
from bs4 import BeautifulSoup

link ='https://turnbackhoax.id/2019/07/01/klarifikasi-disebut-ada-mafia-lakukan-jual-beli-darah-hasil-donor-pmi-angkat-bicara/'

def ambil(link):
    r = requests.get(link, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')
    isi = soup.find('div', {'class': 'entry-content mh-clearfix'})
    kumpulan_p = isi.find_all('p')
    paragrafs = [p.text for p in kumpulan_p]
    return " ".join([p for p in paragrafs if not p == '==='])