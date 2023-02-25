from json import dumps
import os
import inflect
import requests

p = inflect.engine()


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


session = requests.session()

for _ in range(100):
    image_response = session.post('https://api.nft.storage/upload',
                                  files={'file': open(f'/tmp/{_}.png', 'rb'), 'type': 'image/png'},
                                  auth=BearerAuth(os.environ.get('SECRET')))
    cid = image_response.json()['value']['cid']
    link = f'https://nftstorage.link/ipfs/{cid}'
    with open(f'/tmp/{_}.json', 'w') as file_json:
        data = {
            "name": p.number_to_words(_),
            "symbol": f"{_}",
            "uri": link,
            "seller_fee_basis_points": 0
        }
        file_json.write(dumps(data))
