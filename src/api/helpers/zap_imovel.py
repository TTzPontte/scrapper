import requests
from bs4 import BeautifulSoup

class ZapImovel():
  def __init__(self, url):
    self.URL = url

  def __format(self, string):
    formatted_string = string.split()
    return " ".join(formatted_string)

  def get(self):
    try:
      session = requests.Session()
      headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
      page = session.get(self.URL, headers=headers)
      soup = BeautifulSoup(page.content, 'html.parser')

      divContainer = soup.find('div', class_='listings__container')
      uls = divContainer.find_all('ul', class_='simple-card__amenities', limit=5)

      response = []
      for li in uls:
        response.append({
          'areas': self.__format(li.find('li', class_='js-areas').get_text()),
          'bedrooms': self.__format(li.find('li', class_='js-bedrooms').get_text()),
          'parking_spaces': self.__format(li.find('li', class_='js-parking-spaces').get_text()),
          'bathrooms': self.__format(li.find('li', class_='js-bathrooms').get_text()),
        })

      return response
    except Exception as err:
      print(f'ERROR OCCURRED - {err}')
      return err
