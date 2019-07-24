import json
from urllib.request import urlopen

from ioiprint import CONTESTANT_DATA_ADDRESS_URL, NET_ADMIN_URL


def get_contestant_data(ip):
    #url_address = CONTESTANT_DATA_ADDRESS_URL.format(ip=ip)
    #data = json.loads(urlopen(url_address).read().decode('utf-8'))
    return {
        'contestant_id': '3',#data['contestant']['id'],
        'contestant_name': 'Jamal Hasanov', #data['contestant']['name'],
        'contestant_country': 'AZE', #data['contestant']['country'],
        'zone': 'A', #data['desk']['zone'],
        'desk_id': '13', #data['desk']['id'],
        'desk_image_url': 'https://ioi2019.az/images/logo_ioi2019.png' #'http://' + NET_ADMIN_URL + data['desk']['map']
    }
