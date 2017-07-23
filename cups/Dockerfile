FROM aadl/cups-alpine:2.2.3

RUN apk add --update --no-cache curl

COPY printers.conf /root/printers.conf
COPY ioi_printer.ppd /root/ioi_printer.ppd
COPY ioi-filter /root/ioi-filter
COPY docker-entrypoint.sh /root/docker-entrypoint.sh

RUN chown root:lp /root/printers.conf && \
    chmod 640 /root/printers.conf && \
    chown root:lp /root/ioi_printer.ppd && \
    chmod 640 /root/ioi_printer.ppd && \
    chown root:root /root/ioi-filter && \
    chmod 755 /root/ioi-filter && \
    chmod +x /root/docker-entrypoint.sh

ENTRYPOINT ["/root/docker-entrypoint.sh"]
