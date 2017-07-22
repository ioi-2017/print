import subprocess

from ioiprint import CUPS_SERVER_ADDRESS


def print_file(file_path, printer):
    subprocess.run(['lpr', '-H', CUPS_SERVER_ADDRESS, '-P', printer,
                    file_path], check=True)
