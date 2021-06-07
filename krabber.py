import json
import requests
import os
import shutil

def parse(url):
    # url = 'https://entertain.naver.com/photo/issue/1058865'
    url = url.replace("issue/", "issueItemList.json?cid=") + "&page="
    print(url)
    n = 0
    while True:
        response = requests.get(url + str(n))
        naverJson = json.loads(response.text)
        for i in naverJson['results'][0]['thumbnails']:
            imagelink = i['thumbUrl'].split("?")[0]
            download(imagelink)
        n += 1
        if len(naverJson['results'][0]['thumbnails']) <= 0:
            break


def download(url):
    (dirname, filename) = os.path.split(url)
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


#parse("https://entertain.naver.com/photo/issue/1058865")