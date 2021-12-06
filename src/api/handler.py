from helpers import scraper_zap_imovel

def handler(event, context):
    zap_imovel_response = scraper_zap_imovel('https://www.zapimoveis.com.br/venda/casas/sp+sao-joao-da-boa-vista++s-joao-da-boa-vista/?onde=,S%C3%A3o%20Paulo,S%C3%A3o%20Jo%C3%A3o%20da%20Boa%20Vista,,SAO%20JOAO%20DA%20BOA%20VISTA,,,neighborhood,BR%3ESao%20Paulo%3ENULL%3ESao%20Joao%20da%20Boa%20Vista%3EBarrios%3ESAO%20JOAO%20DA%20BOA%20VISTA,-21.979946,-46.816809&transacao=Venda&tipoUnidade=Residencial,Casa&tipo=Im%C3%B3vel%20usado&pagina=1')

    print(zap_imovel_response)

    return {
        "statusCode": 200
    }