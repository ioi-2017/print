import os

PATH = os.path.dirname(os.path.realpath(__file__))

STATIC_PATH = os.path.join(PATH, 'static')
TEMPLATES_PATH = os.path.join(PATH, 'template')

MAX_NUM_OF_PAGES_FOR_CONTESTANTS = 12

PRINTER_FOR_FLOOR = {
    'floor1': 'floor1',
    'floor2': 'floor2'
}

PRINTER_FOR_TRANSLATION = 'default'
