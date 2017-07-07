import subprocess


def print_file(file_path, printer):
    subprocess.run(['lpr', '-P', printer, '-o', 'fit-to-page', file_path],
                   check=True)
