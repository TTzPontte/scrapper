import re
import requests
from bs4 import BeautifulSoup

class VivaReal():
  def __init__(self, url_result_search):
    self.URL = url_result_search
    self.BASE_URL = 'https://www.vivareal.com.br'

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

      list_of_properties = [link_property.get('href') for link_property in page_result_search.find_all('a')]
      requests = [f'{self.BASE_URL}{link}' for link in list_of_properties if link is not None and link.startswith('/imovel')]
      
      pages = [self.__scraper_page(request) for request in requests]

      response = []
      for page_content in pages:
        address = page_content.select_one('div.address-container p.js-address')
        areas = page_content.find('li', class_='js-area') 
        bedrooms = page_content.find('li', class_='js-bedrooms')
        parking_spaces = page_content.find('li', class_='js-parking')
        bathrooms = page_content.find('li', class_='js-bathrooms')
        condominium = page_content.select_one('div.price-container span.js-condominium')
        iptu = page_content.select_one('div.price-container span.js-iptu')
        price = page_content.select_one('div.price-container h3.js-price-sale')

        formatted_address = self.__format_address(address.get_text(strip=True) if address is not None else '')
        
        response.append({
          'logradouro': formatted_address.get('street'),
          'bairro': formatted_address.get('neighborhood'),
          'cidade': formatted_address.get('city'),
          'estado': formatted_address.get('state'),
          'areaTerreno': areas and areas.get_text(strip=True) or '',
          'areaPrivativa': 0,
          'quartos': bedrooms and bedrooms.get_text(strip=True) or '',
          'vagas': parking_spaces and parking_spaces.get_text(strip=True) or '',
          'banheiros': bathrooms and bathrooms.get_text(strip=True) or '',
          'andares': 0,
          'valorCondominio': condominium and condominium.get_text(strip=True) or '',
          'valorTotal': price and price.get_text(strip=True) or '',
          'IPTU': iptu and iptu.get_text(strip=True) or '',
        })

      return response
    except Exception as err:
      print(f'ERROR OCCURRED - {err}')
      return err
