#!/usr/bin/env python3
from urllib.request import urlopen

NetAdminURL = 'netadmin.ioi2017.org'
ContestantDataAddressURL = 'http://{url}/api/nodes/ip/{{ip}}/'.format(url=NetAdminURL)

def get_contestant_data(ip):
    url_address = ContestantDataAddressURL.format(ip=ip)
    data = json.loads(urlopen(url_address).read().decode('utf-8'))
    return {
        floor: data.desk.room,
        # TODO: pass on location, after hamed puts it in
        # location: data.desk.id,
        contestant_id: data.contestant.id,
        contestant_name: data.contestant.name,
        contestant_country: data.contestant.country,
        desk_image_url: 'http://' + NetAdminURL + data.desk.map,
    }
