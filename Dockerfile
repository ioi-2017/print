FROM ubuntu:xenial-20170619

RUN apt-get -yq update && \
    apt-get install -yq python3 python3-pip wkhtmltopdf pdftk cups cups-pdf xvfb

ADD . /usr/src/print-system/
WORKDIR /usr/src/print-system/

RUN pip3 install .

ENTRYPOINT ['bash']
