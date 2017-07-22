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

DEFAULT_PRINTER = 'default'

NET_ADMIN_URL = os.getenv('NETADMIN_URL')
CONTESTANT_DATA_ADDRESS_URL = 'http://{url}/api/nodes/ip/{{ip}}/'.format(
    url=NET_ADMIN_URL)

PDF_UPLOAD_PATH = os.getenv('UPLOADS_DIRECTORY')

CUPS_SERVER_ADDRESS = os.getenv('CUPS_ADDRESS')
