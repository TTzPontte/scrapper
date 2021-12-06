from scrapper_dao import viva_real, zap_imovel

def handler(event, context):
    viva_real.message_viva_real()
    zap_imovel.message_zap_imovel()

    return {
        "statusCode": 200
    }