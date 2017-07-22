#!/bin/sh
cp /root/printers.conf /etc/cups/printers.conf
cp /root/ioi_printer.ppd /etc/cups/ppd/ioi_printer.ppd && \
cp /root/ioi-filter /usr/lib/cups/filter/ioi-filter

exec /root/start-cups.sh
