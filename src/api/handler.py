import json

from helpers import scraper_zap_imovel, scraper_vivareal

def handler(event, context):
    urls = json.loads(event.get('body'))

    viva_real_response, zap_imovel_response, response = [], [], []

    for url in urls:
        viva_real = url.get('viva_real')
        zap_imovel = url.get('zap_imovel')

        if viva_real is not None:
            viva_real_response = scraper_vivareal(viva_real)
            response.extend(viva_real_response)

        if zap_imovel is not None:
            zap_imovel_response = scraper_zap_imovel(zap_imovel)    
            response.extend(zap_imovel_response)  

    return {
        "statusCode": 200,
        "body": json.dumps(response, ensure_ascii=False).encode('utf8')
    }
