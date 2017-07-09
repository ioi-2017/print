#!/bin/bash
PRINT_SERVER_ADDRESS="http://localhost:5000"

if (( $# < 2 || $# > 3 )); then
    echo "Illegal number of arguments, it should be either 2 or 3"
    echo "Usage: mass.sh FILENAME PRINTER [COUNT]"
    echo "  argument COUNT defaults to 1"
    exit 1
fi

FILENAME=$1
PRINTER=$2
COUNT=${3:-1}

if [ ! -f "${FILENAME}" ]; then
    echo "File not found!"
    exit 1
fi

SERVER_FILENAME=`curl --form "pdf=@${FILENAME}" --form "type=mass" ${PRINT_SERVER_ADDRESS}/upload`

curl --data "filename=${SERVER_FILENAME}&printer=${PRINTER}&count=${COUNT}" ${PRINT_SERVER_ADDRESS}/mass
