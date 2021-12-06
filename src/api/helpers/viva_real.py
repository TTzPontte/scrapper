import requests
from bs4 import BeautifulSoup

class VivaReal():
    def __init__(self, url):
        self.soup = None
        self.property_url = None
        self.main_url = url
        self.link_list = ['']
        self.base_url = 'https://www.vivareal.com.br/'

    def scrape_page(self, main):
        link = (self.property_url, self.main_url)[main]
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        soup.prettify()
        self.soup = soup

    def list_all_links_in_page(self):
        all_links = []
        for link in self.soup.find_all('a'):
            all_links.append(link.get('href'))

        '''
        filter links in page
        '''
        link_list = [item for item in all_links if item is not None and item.startswith('/imovel')]
        return link_list

    def get_a_property_info(self, url):
        self.property_url = url
        self.scrape_page(main=False)
        ul_tag = self.soup.find('ul', class_='features')

        li_tags = [li for li in ul_tag if isinstance(li, str) is False]

        info_list = [{i.attrs['title']: i.get_text()} for i in li_tags]
        return info_list

    def activate(self):
        self.scrape_page(main=True)
        link_list = self.list_all_links_in_page()
        self.link_list = link_list
        return [self.get_a_property_info(self.base_url + i) for i in link_list if i.__len__() > 1]