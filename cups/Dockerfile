FROM aadl/cups-alpine

ARG PRINTER_NAME=ioi_printer

RUN apk add --update --no-cache curl

COPY printers.conf.template /root/printers.conf
COPY printer.ppd /root/$PRINTER_NAME.ppd
COPY ioi-filter /root/ioi-filter
COPY docker-entrypoint.sh /root/docker-entrypoint.sh

RUN sed -i "s/PRINTER_NAME/$PRINTER_NAME/g" /root/printers.conf
RUN chown root:lp /root/printers.conf && \
    chmod 640 /root/printers.conf && \
    chown root:lp /root/$PRINTER_NAME.ppd && \
    chmod 640 /root/ioi_printer.ppd && \
    chown root:root /root/ioi-filter && \
    chmod 755 /root/ioi-filter && \
    chmod +x /root/docker-entrypoint.sh

ENTRYPOINT ["/root/docker-entrypoint.sh"]
