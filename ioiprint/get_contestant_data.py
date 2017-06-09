import json
from urllib.request import urlopen

NET_ADMIN_URL = 'netadmin.ioi2017.org'
CONTESTANT_DATA_ADDRESS_URL = 'http://{url}/api/nodes/ip/{{ip}}/'.format(
    url=NET_ADMIN_URL)


def get_contestant_data(ip):
    url_address = CONTESTANT_DATA_ADDRESS_URL.format(ip=ip)
    data = json.loads(urlopen(url_address).read().decode('utf-8'))
    return {
        'floor': data['desk']['room'],
        # TODO: pass on location, after hamed puts it in location: data.desk.id
        'contestant_id': data['contestant']['id'],
        'contestant_name': data['contestant']['name'],
        'contestant_country': data['contestant']['country'],
        'desk_image_url': 'http://' + NET_ADMIN_URL + data['desk']['map'],
    }
