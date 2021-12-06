from .zap_imovel import ZapImovel

def scraper_zap_imovel(url):
  zap_imovel = ZapImovel(url)
  return zap_imovel.get()