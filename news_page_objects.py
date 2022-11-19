import bs4
import requests
from common import config

class HomePage:

    def __init__(self, news_site_uid, url):
        self._codeldiario = config()['news_sites'][news_site_uid]    # eluniversal / elpais
        self._patrondequerie = self._codeldiario['queries']                 # .field-content a
        self._html = None

        self._visit(url)                                        # url = http://eluniversal.com.mx 

    @property
    def article_links(self):
        link_list = []
        for link in self._select(self._patrondequerie['homepage_article_links']):
            if link and link.has_attr('href'):
                link_list.append(link)
        return set(link['href'] for link in link_list)

    def _select(self, query_string):
        return self._html.select(query_string)

    def _visit(self, url):                                      # url = http://eluniversal.com.mx
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0 Edg/91.0.864.59'}
        response = requests.get(url, headers=headers)           # url = http://eluniversal.com.mx
        response.raise_for_status()                             # si da cod status <> 200 se corta

        self._html = bs4.BeautifulSoup(response.text, 'html.parser')    # arbol de text de la pagina web
        



    
