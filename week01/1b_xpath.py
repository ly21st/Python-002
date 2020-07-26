# -*- coding:utf-8 -*-

import requests
import lxml.etree
import time

url_prefix = 'https://maoyan.com'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
g_cookie = '''__mta=209615149.1595728239331.1595728255897.1595728267402.3; uuid_n_v=v1; uuid=D4891950CE7D11EAAE7D95D379FC6A679F54D9A787A54A84AE2204C05DBD1458; _csrf=b47edceb615c7315ffacc1e61ae72b53bbce77da192b8868dae3ac63296bbb11; _lxsdk_cuid=173863d7d71c8-03f902ea598eef-5313f6f-1fa400-173863d7d71c8; _lxsdk=D4891950CE7D11EAAE7D95D379FC6A679F54D9A787A54A84AE2204C05DBD1458; mojo-uuid=64aeff716e5dbe6d8dc3c1b56386d227; mojo-session-id={"id":"8cdcb2def9991d8bc252ee8b3456b9ae","time":1595728239212}; lt=wUjaNDjOTFWG7lzHtyjqfXRv6YwAAAAAHwsAAPyuQeVuwXqimhOwhDVDR5Ivtb7fIn_tcPutlWuGcHRHTC_U7y9Qf7dzLtAdg7fMnQ; lt.sig=e8vCYYgobOndcIeudlZQU-jtxqI; mojo-trace-id=5; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595728239,1595728256,1595728275; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595728275; __mta=209615149.1595728239331.1595728267402.1595728275377.4; _lxsdk_s=17388d09783-f6b-485-d36%7C101922119%7C9'''

def get_url(myurl):
    header = {'user-agent': user_agent}
    header['Cookie'] = g_cookie
    response = requests.get(myurl, headers=header)
    # print(response.text)
    selector = lxml.etree.HTML(response.text)

    url_list = selector.xpath('//div[@class="channel-detail movie-item-title"]/a/@href')
    print("url_list:", url_list)
    return [url_prefix + url for url in url_list[:10]]


def get_movie_info(myurl):
    header = {'user-agent': user_agent}
    header['Cookie'] = g_cookie
    response = requests.get(myurl, headers=header)
    # print(response.text)
    selector = lxml.etree.HTML(response.text)

    movie_info = []
    # movie_info.append(myurl)
    movie_container = selector.xpath('//div[1][@class="movie-brief-container"]')
    print('movie_container:', movie_container)
    if (not movie_container):
        return

    movie_container = movie_container[0]
    filename = movie_container.xpath('./h1[@class="name"]/text()')
    print('filename:', filename)
    movie_info.append(" ".join(filename))

    file_type = movie_container.xpath('./ul/li[1]/a/text()')
    print('file_type:', file_type)
    movie_info.append("/".join(file_type))

    file_date = movie_container.xpath('./ul/li[3]/text()')
    print('file_date:', file_date)
    movie_info.append(" ".join(file_date))

    return movie_info


def get_movies_info():
    urls = get_url('https://maoyan.com/films?showType=3&offset=0')
    all_movies = []
    for url in urls:
        print(url)
        time.sleep(5)
        movie = get_movie_info(url)
        all_movies.append(movie)

    for movie in all_movies:
        print(movie)
    return all_movies


import pandas as pd
def save_to_csv(all_movies):
    df = pd.DataFrame(data=all_movies)
    df.to_csv("./movies.csv", encoding='utf8', index=False, header=False)


movies = get_movies_info()
save_to_csv(movies)