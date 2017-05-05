#!/bin/bash
options="$5"
eval `(./ioi-print-contestant-details "$options")`
export JOB_ID=10
export CONTESTANT_ID
export CONTESTANT_NAME
export CONTESTANT_COUNTRY
export CONTESTANT_LOCATION
export CONTESTANT_FLOOR
export NUM_PAGES=6
export LIMITED_STR
export DATE_TIME=$(date "+%a, %X")
export SCRIPT_DIR=$(pwd)
perl -pe 's/%%([^\%]+)%%/$ENV{$1}/g' < aux-template.html > aux.html
phantomjs html2pdf.js aux.html aux.pdf
