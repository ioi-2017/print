import os

PATH = os.path.dirname(os.path.realpath(__file__))

STATIC_PATH = os.path.join(PATH, 'static')
TEMPLATES_PATH = os.path.join(PATH, 'template')

MAX_NUM_OF_PAGES_FOR_CONTESTANTS = 12

PRINTER_FOR_ZONE = {
    'A': 'floor1',
    'B': 'floor1',
    'C': 'floor1',
    'D': 'floor1',
    'E': 'floor2',
    'F': 'floor2',
    'G': 'floor2',
    'H': 'floor2',
}

PRINTER_FOR_TRANSLATION = 'default'

NET_ADMIN_URL = 'netadmin.ioi2017.org'
CONTESTANT_DATA_ADDRESS_URL = 'http://{url}/api/nodes/ip/{{ip}}/'.format(
    url=NET_ADMIN_URL)

PDF_UPLOAD_PATH = os.path.join(PATH, 'uploads')
PATH_FOR_TYPE = {
    'translation': os.path.join(PDF_UPLOAD_PATH, 'translation'),
    'contestant': os.path.join(PDF_UPLOAD_PATH, 'contestant'),
    'mass': os.path.join(PDF_UPLOAD_PATH, 'mass')
}
