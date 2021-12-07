import re
import requests
from bs4 import BeautifulSoup

class ZapImovel():
  def __init__(self, url_result_search):
    self.URL = url_result_search
    self.BASE_URL = 'https://www.zapimoveis.com.br/'

  def __format_address(self, address):
    state = re.match(r'.+- ([^-]+)$', address)
    city = re.match(r'.+, ([^,]+) - [^-]+$', address)
    neighborhood = re.match(r'.+- ([^-]+), ([^,]+) - [^-]+$', address)
    street = re.match(r'(.+) - ([^-]+), ([^,]+) - [^-]+$', address)
    
    return {
        'state': state.group(1) if street is not None else '',
        'city': city.group(1) if city is not None else '',
        'neighborhood': neighborhood.group(1) if neighborhood is not None else '',
        'street': street.group(1) if street is not None else ''
      }

  def __scraper_page(self, url):
    session = requests.Session()
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = session.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    soup.prettify()

    return soup

  def activate(self):
    try:
      page_result_search = self.__scraper_page(self.URL)
      list_property_ids = page_result_search.select('div[data-id]')
      
      requests = [f'{self.BASE_URL}imovel/{property_id.get("data-id")}' for property_id in list_property_ids if property_id is not None]
      pages = [self.__scraper_page(request) for request in requests]

      response = []
      for page_content in pages:
        address = page_content.find('span', attrs={'itemprop': 'address'})
        areas = page_content.find('li', class_='js-areas') 
        bedrooms = page_content.find('li', class_='js-bedrooms')
        parking_spaces = page_content.find('li', class_='js-parking-spaces')
        bathrooms = page_content.find('li', class_='js-bathrooms')
        floor = page_content.find('li', class_='js-floor')
        condominium = page_content.select_one('li.condominium span')
        iptu = page_content.select_one('li.iptu span')

        formatted_address = self.__format_address(address.get_text(strip=True) if address is not None else '')
        
        response.append({
          'logradouro': formatted_address.get('street'),
          'bairro': formatted_address.get('neighborhood'),
          'cidade': formatted_address.get('city'),
          'estado': formatted_address.get('state'),
          'areaTerreno': areas and areas.get_text(strip=True) or '',
          'quartos': bedrooms and bedrooms.get_text(strip=True) or '',
          'vagas': parking_spaces and parking_spaces.get_text(strip=True) or '',
          'banheiros': bathrooms and bathrooms.get_text(strip=True) or '',
          'andares': floor and floor.get_text(strip=True) or '',
          'valorCondominio': condominium and condominium.get_text(strip=True) or '',
          'IPTU': iptu and iptu.get_text(strip=True) or '',
        })

      return response
    except Exception as err:
      print(f'ERROR OCCURRED - {err}')
      return err
