import requests


def get_dw():
    cookies = {
        'deg_expose_marked': '[]',
        '_pk_id.2.5bbb': 'a28e2af57f5fe6eb.1644520044.',
        'cookie-tracking': 'decline',
        'cookie-marketing': 'accept',
        'cookie-maps': 'accept',
        'cookie-immo': 'accept',
        'cookie-youtube': 'accept',
        'degewo-cookie-consent': 'true',
        'TS0194984b': '01fe90c44264fcdb94e6fe68f16311d117d8e29c7eb3a1dffed5c1029dff0d0826433165743db1d1886469b7c2346e8f22ecf0a1de',
        '_pk_ref.2.5bbb': '%5B%22%22%2C%22%22%2C1647816865%2C%22https%3A%2F%2Fwww.degewo.de%2F%22%5D',
        '_pk_ses.2.5bbb': '1',
        '_immo-search_session': 'VFNPRnVJZ082b21Sa2ZzWExRV1NSeWt3d3Z6S1YxVzZCZkk2Mi9EanRia1ZjejI2a0tidklhNHhJSDMrbjAvU201TFB4WUZQMjg5QlRhMDg4eGtocEk5T0dGV2VReDR2TFY1UitDL0E2NkxWNHNySFE3bU1Ecng3aXM5SDl1dDRCdFpmOWFwOEZCSjBMOTF6SnRSU2s5ZXJlKzcyOUkvSWE2ZW5XTmRKbkRHcnNVcU9tRTFhaVkyaFVJd3ptK0ZYZW9jYi9xaVowcFJhUGdzWFBVTFlQemxoL05qd3dQOE96MG1aSG9sY2F2aDRRaHE3eUFJYnBRYXgybDF5WkE2NHRCTVRNRmZOR3k1cEpnSUxVZzlGeXdEc2p2R1llNkFad1A3WW1Dc3ozZ1U1MFArK1F0S1pSUHhsck1ZcHNFakgrT3p3VzIxS21Jd205THlpOWJVN29TMytDYVBEVEgvZDlERFVQZTdta0pFQ0JKN1BVemRvUyt3bFdtaUJKbm1Lbk4rNGtoUUlNOXlGaEFNTzF2K1VEUTVVbG4xbi9TY20zTzdjRnIxS2xrQm1nanExRmxDaFJYWk1BYXBWQWpsZCtBdkdOTVNjT3FjMitEZExkNTNnTmFPMlFKZDZsdlhndTRPR1FMOVlEbU1zbVJuMDArTW5hTmNNVTNvUzVISyt1YmZFUE5uUmZVUDl4anJ3SzBZNGRFd3krd09kYzluMDg3WXJXdEZ6QUY4Z3dsZ3JhWVF0RWNPK2l5Z2YxUTJ5RXJsT1paZmVFc2ljRFJCNmZDUzRvaUdha3hiWDNHWXloRktPVWtvMWo3YTh6L3ZPZjFDSms5cThpbVVLcHoyaXBiMDJnVmwrWXMzZzh2WDNSWTVnY2w5NTJDWVJTdFlocDlTU2NxeFRuVDRDUlRrM2VyQkFUSXFuK3JQREFGclU5TVVpSTU3ay93SGVRWVNLUmdzZ0FReFhJaUJzakhTTkxyNDlndDRpSjRKY3dwOXdHS0JMc1BEM3lSZm9tWnRqOSs2OEZBbXdTNnpNQlpoMDVPcC8zMmhCaVgzQTExTkIraUNUQVBFRU1BWT0tLTFvc2JNWlFFWk4yTHhScFM4UHR5TWc9PQ%3D%3D--efbc59ee3cc3367f499c5de13d7a91140b64805a',
    }


    headers = {
        'authority': 'immosuche.degewo.de',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://immosuche.degewo.de/de/search?size=10&page=1&property_type_id=1&categories%5B%5D=1&lat=&lon=&area=&address%5Bstreet%5D=&address%5Bcity%5D=&address%5Bzipcode%5D=&address%5Bdistrict%5D=&address%5Braw%5D=&district=&property_number=&price_switch=true&price_radio=null&price_from=&price_to=&qm_radio=null&qm_from=&qm_to=&rooms_radio=null&rooms_from=&rooms_to=&wbs_required=&order=rent_total_without_vat_asc',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'deg_expose_marked=[]; _pk_id.2.5bbb=a28e2af57f5fe6eb.1644520044.; cookie-tracking=decline; cookie-marketing=accept; cookie-maps=accept; cookie-immo=accept; cookie-youtube=accept; degewo-cookie-consent=true; TS0194984b=01fe90c44264fcdb94e6fe68f16311d117d8e29c7eb3a1dffed5c1029dff0d0826433165743db1d1886469b7c2346e8f22ecf0a1de; _pk_ref.2.5bbb=%5B%22%22%2C%22%22%2C1647816865%2C%22https%3A%2F%2Fwww.degewo.de%2F%22%5D; _pk_ses.2.5bbb=1; _immo-search_session=VFNPRnVJZ082b21Sa2ZzWExRV1NSeWt3d3Z6S1YxVzZCZkk2Mi9EanRia1ZjejI2a0tidklhNHhJSDMrbjAvU201TFB4WUZQMjg5QlRhMDg4eGtocEk5T0dGV2VReDR2TFY1UitDL0E2NkxWNHNySFE3bU1Ecng3aXM5SDl1dDRCdFpmOWFwOEZCSjBMOTF6SnRSU2s5ZXJlKzcyOUkvSWE2ZW5XTmRKbkRHcnNVcU9tRTFhaVkyaFVJd3ptK0ZYZW9jYi9xaVowcFJhUGdzWFBVTFlQemxoL05qd3dQOE96MG1aSG9sY2F2aDRRaHE3eUFJYnBRYXgybDF5WkE2NHRCTVRNRmZOR3k1cEpnSUxVZzlGeXdEc2p2R1llNkFad1A3WW1Dc3ozZ1U1MFArK1F0S1pSUHhsck1ZcHNFakgrT3p3VzIxS21Jd205THlpOWJVN29TMytDYVBEVEgvZDlERFVQZTdta0pFQ0JKN1BVemRvUyt3bFdtaUJKbm1Lbk4rNGtoUUlNOXlGaEFNTzF2K1VEUTVVbG4xbi9TY20zTzdjRnIxS2xrQm1nanExRmxDaFJYWk1BYXBWQWpsZCtBdkdOTVNjT3FjMitEZExkNTNnTmFPMlFKZDZsdlhndTRPR1FMOVlEbU1zbVJuMDArTW5hTmNNVTNvUzVISyt1YmZFUE5uUmZVUDl4anJ3SzBZNGRFd3krd09kYzluMDg3WXJXdEZ6QUY4Z3dsZ3JhWVF0RWNPK2l5Z2YxUTJ5RXJsT1paZmVFc2ljRFJCNmZDUzRvaUdha3hiWDNHWXloRktPVWtvMWo3YTh6L3ZPZjFDSms5cThpbVVLcHoyaXBiMDJnVmwrWXMzZzh2WDNSWTVnY2w5NTJDWVJTdFlocDlTU2NxeFRuVDRDUlRrM2VyQkFUSXFuK3JQREFGclU5TVVpSTU3ay93SGVRWVNLUmdzZ0FReFhJaUJzakhTTkxyNDlndDRpSjRKY3dwOXdHS0JMc1BEM3lSZm9tWnRqOSs2OEZBbXdTNnpNQlpoMDVPcC8zMmhCaVgzQTExTkIraUNUQVBFRU1BWT0tLTFvc2JNWlFFWk4yTHhScFM4UHR5TWc9PQ%3D%3D--efbc59ee3cc3367f499c5de13d7a91140b64805a',
    }

    params = [
        ('utf8', '\u2713'),
        ('property_type_id', '1'),
        ('categories[]', '1'),
        ('property_number', ''),
        ('address[raw]', ''),
        ('address[street]', ''),
        ('address[city]', ''),
        ('address[zipcode]', ''),
        ('address[district]', ''),
        ('district', ''),
        ('price_switch', 'false'),
        ('price_switch', 'on'),
        ('price_from', ''),
        ('price_to', ''),
        ('price_from', ''),
        ('price_to', ''),
        ('price_radio', 'null'),
        ('price_from', ''),
        ('price_to', ''),
        ('qm_radio', 'null'),
        ('qm_from', ''),
        ('qm_to', ''),
        ('rooms_radio', 'null'),
        ('rooms_from', ''),
        ('rooms_to', ''),
        ('features[]', ''),
        ('wbs_required', ''),
        ('order', 'rent_total_without_vat_asc'),
    ]

    response = requests.get('https://immosuche.degewo.de/de/search.json',
                            headers=headers, params=params, cookies=cookies)

    json = response.json()

    return json


def get_degewo():


    headers = {
        'authority': 'immo-api.deutsche-wohnen.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        'sec-ch-ua-platform': '"macOS"',
        'origin': 'https://www.deutsche-wohnen.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'en-US,en;q=0.9',
    }

    data = '{"infrastructure":{},"flatTypes":{},"other":{},"commercializationType":"rent","utilizationType":"flat","location":"Berlin","city":"Berlin","locale":"de"}'

    response = requests.post('https://immo-api.deutsche-wohnen.com/estate/findByFilter', headers=headers, data=data)

    return response.json()