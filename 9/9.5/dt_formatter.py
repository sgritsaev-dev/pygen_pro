from datetime import *

d = {'ru': '%d.%m.%Y',
     'us': '%m-%d-%Y',
     'ca': '%Y-%m-%d',
     'br': '%d/%m/%Y',
     'fr': '%d.%m.%Y',
     'pt': '%d-%m-%Y', }


def date_formatter(country_code):
    def returner(dte):
        res = datetime.strftime(dte, d[country_code])
        return res
    return returner
