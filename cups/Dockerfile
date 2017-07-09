FROM ubuntu:xenial-20170619

RUN apt-get -yq update && \
    apt-get -yq install cups cups-pdf whois

ADD cupsd.conf /etc/cups/cupsd.conf

ADD docker-entrypoint.sh /root/docker-entrypoint.sh
RUN chmod +x /root/docker-entrypoint.sh

CMD ["/root/docker-entrypoint.sh"]
