from requests import get, utils
import json
import pprint
# import pprint

def currency_rates(val):
    response = get('http://www.cbr-xml-daily.ru/daily_json.js')
    # print(type(response))
    # encodings = utils.get_encoding_from_headers(response.headers)
    # content = response.content.decode(encoding=encodings)
    dict = json.loads(response.text)
    pprint.pprint('Курс ' + val + ' на: ' + dict['Date'][0:10] + ' = ' + str(dict['Valute'][val]['Value']))
    # pprint.pprint('Курс ' + val + ' '+ str(dict['Valute'][val]['Value']))
    # pprint.pprint(dict['Курс' + val['Valute'][val]['Value']])
    # pprint.pprint(dict)