#!/bin/sh
cp /root/printers.conf /etc/cups/printers.conf
cp /root/${PRINTER_NAME}.ppd /etc/cups/ppd/${PRINTER_NAME}.ppd
cp /root/ioi-filter /usr/lib/cups/filter/ioi-filter

exec /root/start-cups.sh
