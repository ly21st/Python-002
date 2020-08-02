# -*- coding: utf-8 -*-

import requests


def get_proxyips():
    url = 'https://ip.jiangxianli.com/api/proxy_ips'

    response = requests.get(url)
    body = response.json()
    if body['code'] != 0:
        return []
    datas = body['data']['data']
    http = ['http://' + e['ip'].strip() + ':' + e['port'].strip()
            for e in datas if e['protocol'] == 'http']
    return http

# http = get_proxyips()
# print('http:', http)
