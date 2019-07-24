import os
import subprocess
from datetime import datetime

from jinja2 import Environment, FileSystemLoader, select_autoescape

from ioiprint import MAX_NUM_OF_PAGES_FOR_CONTESTANTS, STATIC_PATH, \
    TEMPLATES_PATH
from ioiprint.utils import html_to_pdf

JINAJ_ENV = Environment(
    loader=FileSystemLoader(TEMPLATES_PATH),
    autoescape=select_autoescape(['html'])
)


def _get_num_of_pages(pdf_file_path):
    num_pages = int(subprocess.check_output(
        'pdftk %s dump_data | '
        'grep NumberOfPages | '
        'awk \'{ print $2 }\'' % pdf_file_path,
        shell=True)[:-1]
    )
    return num_pages


def make_translation_pdf(pdf_file_path, country_code, country_name,
                         temp_directory):
    formatted_time = datetime.now().strftime('%a, %H:%M:%S')
    num_pages = _get_num_of_pages(pdf_file_path)

    first_page_template = JINAJ_ENV.get_template('translation.html.jinja2')
    first_page_html = first_page_template.render(
        static_path=STATIC_PATH,
        country_code=country_code,
        country_name=country_name,
        num_pages=num_pages,
        time=formatted_time
    )
    first_page_pdf = html_to_pdf(first_page_html, 'first', temp_directory)

    final_pdf_path = os.path.join(temp_directory, 'final.pdf')
    subprocess.run([
        'pdftk',
        'I=%s' % pdf_file_path,
        'F=%s' % first_page_pdf,
        'cat', 'F', 'I', 'output', final_pdf_path],
        check=True)
    return final_pdf_path


def make_contestant_pdf(pdf_file_path, contestant_id, contestant_name,
                        contestant_country, zone, desk_id, desk_map_img, print_id,
                        temp_directory):
    formatted_time = datetime.now().strftime('%a, %H:%M:%S')
    num_pages = _get_num_of_pages(pdf_file_path)
    original_num_pages = None

    if num_pages > MAX_NUM_OF_PAGES_FOR_CONTESTANTS:
        original_num_pages = num_pages
        num_pages = MAX_NUM_OF_PAGES_FOR_CONTESTANTS

    first_page_template = JINAJ_ENV.get_template('first.html.jinja2')
    first_page_html = first_page_template.render(
        static_path=STATIC_PATH,
        contestant_id=contestant_id,
        zone=zone,
        desk_id=desk_id,
        contestant_name=contestant_name,
        num_pages=num_pages,
        original_num_pages=original_num_pages,
        time=formatted_time,
        print_id=print_id,
        desk_map_img=desk_map_img
    )
    first_page_pdf = html_to_pdf(first_page_html, 'first', temp_directory)

    last_page_template = JINAJ_ENV.get_template('last.html.jinja2')
    last_page_html = last_page_template.render(
        static_path=STATIC_PATH,
        print_id=print_id,
        num_pages=num_pages,
        original_num_pages=original_num_pages,
        time=formatted_time,
        contestant_id=contestant_id,
        zone=zone,
        desk_id=desk_id,
        country_name=contestant_country,
        contestant_name=contestant_name
    )
    last_page_pdf = html_to_pdf(last_page_html, 'last', temp_directory)

    final_pdf_path = os.path.join(temp_directory, 'final.pdf')
    subprocess.run([
        'pdftk',
        'I=%s' % pdf_file_path,
        'F=%s' % first_page_pdf,
        'L=%s' % last_page_pdf,
        'cat', 'F1', 'I1-%s' % num_pages, 'L1', 'output', final_pdf_path],
        check=True)
    return final_pdf_path


def make_cms_request_pdf(request_message, contestant_id, contestant_name,
                         desk_id, desk_map_img, temp_directory):
    formatted_time = datetime.now().strftime('%a, %H:%M:%S')

    request_template = JINAJ_ENV.get_template('request.html.jinja2')
    request_html = request_template.render(
        static_path=STATIC_PATH,
        contestant_id=contestant_id,
        contestant_name=contestant_name,
        desk_id=desk_id,
        request_message=request_message,
        time=formatted_time,
        desk_map_img=desk_map_img
    )
    request_pdf = html_to_pdf(request_html, 'request', temp_directory)

    return request_pdf
