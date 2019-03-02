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
-e frame.number \
-e frame.time_relative \
-e frame.len \
-e wlan_radio.phy \
-e wlan_radio.frequency \
-e wlan_radio.signal_dbm \
-e wlan_radio.data_rate \
-e wlan_radio.duration \
-e wlan.fc.type_subtype \
-e wlan.fc.type \
-e wlan.fc.subtype \
-e wlan.duration \
-e wlan.fc.ds \
-e wlan.fc.retry \
-e wlan.fcs.status \
-e wlan.qos.priority \
-e data.len>> ${INPUT_PCAP_FILE}_results.csv
