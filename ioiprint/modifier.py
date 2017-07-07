import os
import subprocess
from datetime import datetime

from jinja2 import Environment, FileSystemLoader, select_autoescape

from ioiprint import PATH, MAX_NUM_OF_PAGES_FOR_CONTESTANTS
from ioiprint.utils import get_temp_directory, html_to_pdf

JINAJ_ENV = Environment(
    loader=FileSystemLoader(os.path.join(PATH, 'template')),
    autoescape=select_autoescape(['html'])
)


def make_translation_pdf(file_path):
    pass


def make_contestant_pdf(file_path, contestant_id, contestant_name,
                        contestant_country, desk_id, desk_map_img, print_id):
    formatted_time = datetime.now().strftime('%a, %H:%M:%S')
    num_pages = int(subprocess.check_output(
        'pdftk %s dump_data | '
        'grep NumberOfPages | '
        'awk \'{ print $2 }\'' % file_path,
        shell=True)[:-1]
    )
    original_num_pages = None

    if num_pages > MAX_NUM_OF_PAGES_FOR_CONTESTANTS:
        original_num_pages = num_pages
        num_pages = MAX_NUM_OF_PAGES_FOR_CONTESTANTS

    first_page_template = JINAJ_ENV.get_template('first.html.jinja2')
    first_page_html = first_page_template.render(
        static_path=os.path.join(PATH, 'static'),
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
        static_path=os.path.join(PATH, 'static'),
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
        'cat', 'F1', 'I1-%s' % num_pages, 'L1', 'output', final_pdf_path],
        check=True)
    return final_pdf_path


def make_cms_pdf(message):
    pass
