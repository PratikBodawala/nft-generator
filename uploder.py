import os

import requests


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


auth = os.environ.get('SECRET')
session = requests.session()

for _ in range(100):
    image_response = session.post('https://api.nft.storage/upload',
                                  files={'file': open(f'/tmp/{_}.png', 'rb'), 'type': 'image/png'},
                                  auth=BearerAuth(auth))
    cid = image_response.json()['value']['cid']
    link = f'https://nftstorage.link/ipfs/{cid}'
    print(cid)

