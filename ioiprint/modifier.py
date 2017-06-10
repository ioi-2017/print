import os
import subprocess
from datetime import datetime

from jinja2 import Environment, FileSystemLoader, select_autoescape

from ioiprint import PATH
from ioiprint.utils import get_temp_directory, html_to_pdf

JINAJ_ENV = Environment(
    loader=FileSystemLoader(os.path.join(PATH, 'template')),
    autoescape=select_autoescape(['html'])
)


def make_translation_pdf(file_path):
    pass


def make_contestant_pdf(file_path, contestant_id, contestant_name,
                        contestant_country, desk_id, desk_map_img, print_id):
    num_pages = 10
    original_num_pages = None
    formatted_time = datetime.now().strftime('%a, %H:%M:%S')

    first_page_template = JINAJ_ENV.get_template('first.html.jinja2')
    first_page_html = first_page_template.render(
        static_path=os.path.join(PATH, 'template'),
        contestant_id=contestant_id,
        desk_id=desk_id,
        contestant_name=contestant_name,
        num_pages=num_pages,
        original_num_pages=original_num_pages,
        time=formatted_time,
        print_id=print_id,
        desk_map_img=desk_map_img
    )
    first_page_pdf = html_to_pdf(first_page_html, 'first')

    last_page_template = JINAJ_ENV.get_template('last.html.jinja2')
    last_page_html = last_page_template.render(
        static_path=os.path.join(PATH, 'template'),
        print_id=print_id,
        num_pages=num_pages,
        original_num_pages=original_num_pages,
        time=formatted_time,
        contestant_id=contestant_id,
        desk_id=desk_id,
        country_name=contestant_country,
        contestant_name=contestant_name
    )
    last_page_pdf = html_to_pdf(last_page_html, 'last')

    final_pdf_path = os.path.join(get_temp_directory(), 'final.pdf')
    subprocess.run([
        'pdftk',
        'I=%s' % file_path,
        'F=%s' % first_page_pdf,
        'L=%s' % last_page_pdf,
        'cat', 'F1', 'I', 'L1', 'output', final_pdf_path], check=True)
    return final_pdf_path


def make_cms_pdf(message):
    pass
