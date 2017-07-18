#!/bin/bash
PRINT_SERVER_ADDRESS="http://localhost:5000"

if (( $# != 2 )); then
    echo "Illegal number of arguments, it should be 2"
    echo "Usage: cms_request.sh REQUEST_MSG CONTESTANT_IP"
    exit 1
fi

REQUEST_MSG=$1
CONTESTANT_IP=$2

curl --data "request_message=${REQUEST_MSG}&ip=${CONTESTANT_IP}" ${PRINT_SERVER_ADDRESS}/cms_request
