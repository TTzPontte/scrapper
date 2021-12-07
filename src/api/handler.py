from helpers import scraper_zap_imovel, scrape_vivareal

def handler(event, context):
    viva_real = scrape_vivareal('https://www.vivareal.com.br/venda/santa-catarina/florianopolis/bairros/trindade/casa_residencial/#')
    zap_imovel_response = scraper_zap_imovel('https://www.zapimoveis.com.br/venda/apartamentos/sp+cajamar/?transacao=Venda&tipoUnidade=Residencial,Apartamento&tipo=Im%C3%B3vel%20usado&onde=,S%C3%A3o%20Paulo,Cajamar,,,,,city,BR%3ESao%20Paulo%3ENULL%3ECajamar,-23.335852,-46.840144')

    print('VIVA REAL', viva_real)
    print('ZAP IMOVEL', zap_imovel_response)

    return {
        "statusCode": 200
    }