import os
import subprocess

_TMP_DIR = None


def get_temp_directory():
    global _TMP_DIR
    if _TMP_DIR is None:
        process = subprocess.run(['mktemp', '-d'], stdout=subprocess.PIPE,
                                 check=True)
        _TMP_DIR = process.stdout[:-1].decode()
    return _TMP_DIR


def download(url):
    pass


def html_to_pdf(html, name):
    html_file_path = os.path.join(get_temp_directory(), '%s.html' % name)
    with open(html_file_path, 'w') as html_file:
        html_file.write(html)
    pdf_file_path = os.path.join(get_temp_directory(), '%s.pdf' % name)
    subprocess.run(['wkhtmltopdf', html_file_path, pdf_file_path], check=True)
    return pdf_file_path
