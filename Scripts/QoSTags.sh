#!/bin/sh

# input a pcap file from standard input
INPUT_PCAP_FILE=$1
HEADER=y
SEPARATOR=,
QUOTE=n

# display standard output 
tshark \
-r ${INPUT_PCAP_FILE} \
-T fields \
-E header=${HEADER} \
-E separator=${SEPARATOR} \
-E quote=${QUOTE} \
-e wlan.sa \
-e wlan.da \
-e wlan.fc.ds \
-e wlan.fc.retry \
-e wlan.country_info.code \
-e wlan.wfa.ie.wme.acp \
-e wlan.qbss.scount \
-e wlan.qbss.cu >> AP_results.csv
