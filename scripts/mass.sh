#!/bin/bash

PRINT_SERVER_IP="192.168.100.52"
PRINT_SERVER_USERNAME="print_user"
PRINT_SERVER_SSH_ADDRESS="${PRINT_SERVER_USERNAME}@${PRINT_SERVER_IP}"

PRINT_SERVER_TMP_FOLDER="~/tmp/mass"

if (( $# < 2 || $# > 3 )); then
    echo "Illegal number of arguments, it should be either 2 or 3"
    echo "Usage: mass.sh FILENAME PRINTER [COUNT]"
    echo "  argument COUNT defaults to 1"
    exit 1
fi

FILENAME=$1
PRINTER=$2
COUNT=${3:-1}

if [ ! -f "$FILENAME" ]; then
    echo "File not found!"
    exit 1
fi

ssh "$PRINT_SERVER_SSH_ADDRESS" -C "mkdir -p '$PRINT_SERVER_TMP_FOLDER'"

NEW_FILENAME="${PRINT_SERVER_TMP_FOLDER}/`date '+%F_%T'`__${PRINTER}__${COUNT}__`echo $FILENAME | rev | cut -d/ -f1 | rev`"
echo $NEW_FILENAME
scp "$FILENAME" "${PRINT_SERVER_SSH_ADDRESS}:${NEW_FILENAME}"

ssh "$PRINT_SERVER_SSH_ADDRESS" -C "ioiprint mass '$NEW_FILENAME' '$PRINTER' '$COUNT'"
