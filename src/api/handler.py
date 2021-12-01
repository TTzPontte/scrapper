import json
import time
import os
import sys
import shutil
import subprocess

from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.chrome import GeckoDriverManager
# from selenium_firefox import Firefox

def handler(event, context):
    try:
        options = Options()
        options.headless = True
        
        binary = FirefoxBinary('/opt/python/common/firefox/firefox')
        
        geckodriver = Service('/opt/python/common/geckodriver', log_path='/tmp/geckodriver.log')
        
        
        print('EXECUTANDO SHELL')
        subprocess.call(['ls', '/tmp/'])
        print('CAT')
        subprocess.call(['cat', '/tmp/geckodriver.log'])
        
        
        browser = Firefox(service=geckodriver, options=options, firefox_binary=binary)

        url = "https://www.imovelweb.com.br/casas-venda-centro-sao-joao-da-boa-vista-mais-de-2-quartos.html"
        
        browser.get(url) 
        
        print(browser.page_source)
        
        # browser.quit()
        # print(soup.prettify())
        
        # print('START')

        # ff = Firefox(headless=True)
        # ff.get('https://www.imovelweb.com.br/')

        # print(ff.current_url)

        time.sleep(1.5)
        browser.quit()
    finally:
        print('Done')
