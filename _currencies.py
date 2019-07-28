import requests


def currencies():
    url_cur = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    resp_cur = requests.get(url_cur)
    currencies_json = resp_cur.json()

    currencies_info = ""
    for cur in currencies_json:
        currencies_info += f"{cur['Cur_Name']} ({cur['Cur_Scale']}) - {cur['Cur_OfficialRate']}\n"

    return currencies_info
