import sys

from ioiprint import PRINTER_FOR_ZONE, PRINTER_FOR_TRANSLATION
from ioiprint.modifier import make_cms_pdf, make_contestant_pdf, \
    make_translation_pdf
from ioiprint.netadmin import get_contestant_data
from ioiprint.print import print_file
from ioiprint.utils import download


def print_usage_and_exit():
    print("Usage:")
    print("ioiprint translation FILE_PATH COUNTRY_CODE COUNTRY_NAME COUNT")
    print("ioiprint cms REQUEST_MESSAGE IP")
    print("ioiprint contestant FILE_PATH IP CUPS_JOB_ID")
    print("ioiprint mass FILE_PATH PRINTER COUNT")
    exit(1)


def main():
    if len(sys.argv) < 2:
        print_usage_and_exit()
    command = sys.argv[1]
    if command == 'translation':
        if len(sys.argv) < 6:
            print_usage_and_exit()
        file_path = sys.argv[2]
        country_code = sys.argv[3]
        country_name = sys.argv[4]
        count = int(sys.argv[5])
        final_pdf_path = make_translation_pdf(file_path, country_code,
                                              country_name)
        for _ in range(count):
            print_file(final_pdf_path, PRINTER_FOR_TRANSLATION)
    elif command == 'cms':
        if len(sys.argv) < 4:
            print_usage_and_exit()
        request_message = sys.argv[2]
        ip = sys.argv[3]
        contestant_data = get_contestant_data(ip)
        desk_map_img = download(contestant_data['desk_image_url'],
                                'desk_map.svg')
        request_pdf_path = make_cms_pdf(
            request_message,
            contestant_data['contestant_id'],
            contestant_data['contestant_name'],
            contestant_data['desk_id'],
            desk_map_img
        )
        print_file(request_pdf_path,
                   PRINTER_FOR_ZONE[contestant_data['zone']])
    elif command == 'contestant':
        if len(sys.argv) < 4:
            print_usage_and_exit()
        file_path = sys.argv[2]
        ip = sys.argv[3]
        cups_job_id = sys.argv[4]
        contestant_data = get_contestant_data(ip)
        desk_map_img = download(contestant_data['desk_image_url'],
                                'desk_map.svg')
        final_pdf_path = make_contestant_pdf(
            file_path,
            contestant_data['contestant_id'],
            contestant_data['contestant_name'],
            contestant_data['contestant_country'],
            contestant_data['desk_id'],
            desk_map_img,
            cups_job_id
        )
        print_file(final_pdf_path, PRINTER_FOR_ZONE[contestant_data['zone']])
    elif command == 'mass':
        if len(sys.argv) < 5:
            print_usage_and_exit()
        file_path = sys.argv[2]
        printer = sys.argv[3]
        count = int(sys.argv[4])
        for _ in range(count):
            print_file(file_path, printer)
    else:
        print_usage_and_exit()
