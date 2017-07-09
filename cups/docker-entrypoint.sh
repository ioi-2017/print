#!/bin/bash

useradd ${CUPS_ADMIN_USER} --system -G root,lpadmin --no-create-home --password $(mkpasswd ${CUPS_ADMIN_PASSWORD})

exec /usr/sbin/cupsd -f