import os

PATH = os.path.dirname(os.path.realpath(__file__))

STATIC_PATH = os.path.join(PATH, 'static')
TEMPLATES_PATH = os.path.join(PATH, 'template')

MAX_NUM_OF_PAGES_FOR_CONTESTANTS = 12

PRINTER_FOR_ZONE = {
    'A': os.getenv('ZONE_A_PRINTER'),
    'B': os.getenv('ZONE_B_PRINTER'),
    'C': os.getenv('ZONE_C_PRINTER'),
    'D': os.getenv('ZONE_D_PRINTER'),
    'E': os.getenv('ZONE_E_PRINTER'),
    'F': os.getenv('ZONE_F_PRINTER'),
    'G': os.getenv('ZONE_G_PRINTER'),
    'H': os.getenv('ZONE_H_PRINTER'),
}

DEFAULT_PRINTER = os.getenv('DEFAULT_PRINTER')

NET_ADMIN_URL = os.getenv('NETADMIN_URL')
CONTESTANT_DATA_ADDRESS_URL = 'http://{url}/api/nodes/ip/{{ip}}/'.format(
    url=NET_ADMIN_URL)

PDF_UPLOAD_PATH = os.getenv('UPLOADS_DIRECTORY')

CUPS_SERVER_ADDRESS = os.getenv('CUPS_ADDRESS')
