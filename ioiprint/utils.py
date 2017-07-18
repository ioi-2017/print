import os
import subprocess
import urllib.request

_TMP_DIR = None


def create_temp_directory():
    process = subprocess.run(['mktemp', '-d'], stdout=subprocess.PIPE,
                             check=True)
    return process.stdout[:-1].decode()


def download(url, file_name, temp_directory):
    downloaded_file_path = os.path.join(temp_directory, file_name)
    urllib.request.urlretrieve(url, downloaded_file_path)
    return downloaded_file_path


def html_to_pdf(html, name, temp_directory):
    html_file_path = os.path.join(temp_directory, '%s.html' % name)
    with open(html_file_path, 'w') as html_file:
        html_file.write(html)
    pdf_file_path = os.path.join(temp_directory, '%s.pdf' % name)
    subprocess.run(['wkhtmltopdf', html_file_path, pdf_file_path], check=True)
    return pdf_file_path
