import json
from urllib.request import urlopen

from ioiprint import CONTESTANT_DATA_ADDRESS_URL, NET_ADMIN_URL


def get_contestant_data(ip):
    url_address = CONTESTANT_DATA_ADDRESS_URL.format(ip=ip)
    data = json.loads(urlopen(url_address).read().decode('utf-8'))
    return {
        'contestant_id': data['contestant']['id'],
        'contestant_name': data['contestant']['name'],
        'contestant_country': data['contestant']['country'],
        'zone': data['desk']['zone'],
        'desk_id': data['desk']['id'],
        'desk_image_url': 'http://' + NET_ADMIN_URL + data['desk']['map']
    }
