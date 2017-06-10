#!/bin/bash

PRINT_SERVER_IP="192.168.100.52"
PRINT_SERVER_USERNAME="print_user"
PRINT_SERVER_SSH_ADDRESS="${PRINT_SERVER_USERNAME}@${PRINT_SERVER_IP}"

if (( $# != 2 )); then
    echo "Illegal number of arguments, it should be 2"
    echo "Usage: cms_request.sh REQUEST_MSG CONTESTANT_IP"
    exit 1
fi

REQUEST_MSG=$1
CONTESTANT_IP=$2

ssh "$PRINT_SERVER_SSH_ADDRESS" -C "ioiprint cms '$REQUEST_MSG' '$CONTESTANT_IP'"
