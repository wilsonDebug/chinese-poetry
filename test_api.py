# -*- coding: utf-8 -*-
import requests

BASE_URL = 'http://127.0.0.1:5000/api/ci'

def test_get_all_ci():
    resp = requests.get(BASE_URL)
    print('获取所有宋词:', resp.status_code, len(resp.json()))

def test_get_by_author():
    author = '苏轼'
    resp = requests.get(f'{BASE_URL}/author/{author}')
    print(f'获取作者为{author}的宋词:', resp.status_code, len(resp.json()))

def test_get_by_rhythmic():
    rhythmic = '水调歌头'
    resp = requests.get(f'{BASE_URL}/rhythmic/{rhythmic}')
    print(f'获取词牌名为{rhythmic}的宋词:', resp.status_code, len(resp.json()))

if __name__ == '__main__':
    test_get_all_ci()
    test_get_by_author()
    test_get_by_rhythmic()