#!/usr/bin/env python
import os
import random
import string

from flask import Flask, request

from ioiprint import PATH_FOR_TYPE, PRINTER_FOR_TRANSLATION, PRINTER_FOR_ZONE
from ioiprint.modifier import make_cms_request_pdf, make_contestant_pdf, \
    make_translation_pdf
from ioiprint.netadmin import get_contestant_data
from ioiprint.print import print_file
from ioiprint.utils import download

app = Flask('ioiprint')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['pdf']
    random_file_name = ''.join(
        random.choice(string.ascii_uppercase + string.digits) 
        for _ in range(10)
    ) + '.pdf'
    file.save(os.path.join(PATH_FOR_TYPE[request.form['type']],
                           random_file_name))
    return random_file_name


@app.route('/mass', methods=['POST'])
def mass():
    filename = request.form['filename']
    printer = request.form['printer']
    count = int(request.form['count'])
    for _ in range(count):
        print_file(os.path.join(PATH_FOR_TYPE['mass'], filename), printer)
    return "OK"


@app.route('/translation', methods=['POST'])
def translation():
    filename = request.form['filename']
    country_code = request.form['country_code']
    country_name = request.form['country_name']
    count = int(request.form['count'])
    final_pdf_path = make_translation_pdf(
        os.path.join(PATH_FOR_TYPE['translation'], filename),
        country_code,
        country_name
    )
    for _ in range(count):
        print_file(final_pdf_path, PRINTER_FOR_TRANSLATION)
    return "OK"


@app.route('/cms_request', methods=['POST'])
def cms_request():
    request_message = request.form['request_message']
    ip = request.form['ip']
    contestant_data = get_contestant_data(ip)
    desk_map_img = download(contestant_data['desk_image_url'], 'desk_map.svg')
    request_pdf_path = make_cms_request_pdf(
        request_message,
        contestant_data['contestant_id'],
        contestant_data['contestant_name'],
        contestant_data['desk_id'],
        desk_map_img
    )
    print_file(request_pdf_path, PRINTER_FOR_ZONE[contestant_data['zone']])
    return "OK"


@app.route('/contestant', methods=['POST'])
def contestant():
    filename = request.form['filename']
    ip = request.form['ip']
    cups_job_id = request.form['cups_job_id']
    contestant_data = get_contestant_data(ip)
    desk_map_img = download(contestant_data['desk_image_url'], 'desk_map.svg')
    final_pdf_path = make_contestant_pdf(
        os.path.join(PATH_FOR_TYPE['contestant'], filename),
        contestant_data['contestant_id'],
        contestant_data['contestant_name'],
        contestant_data['contestant_country'],
        contestant_data['desk_id'],
        desk_map_img,
        cups_job_id
    )
    print_file(final_pdf_path, PRINTER_FOR_ZONE[contestant_data['zone']])
    return "OK"

if __name__ == '__main__':
    app.run(debug=True)
