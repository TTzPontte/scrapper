from .zap_imovel import ZapImovel
from .viva_real import VivaReal

def scrape_vivareal(url):
  viva_real = VivaReal(url)
  return viva_real.activate()

def scraper_zap_imovel(url):
  zap_imovel = ZapImovel(url)
  return zap_imovel.get()