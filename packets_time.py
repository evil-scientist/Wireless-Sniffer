import pandas as pd 
import matplotlib.pyplot as matplot
import numpy as  np

capture_file = "WhatsAppCall"

data = pd.read_csv(capture_file + "_results.csv")

print("Percentage of retries: " + "%0.2f%%" % (data[data['wlan.fc.retry'] == 1]['wlan.fc.retry'].count()/data["frame.number"].count()*100))

data_len = []
nr_packets = []

length_of_bins = 1 #seconds

end_of_capture = data['frame.time_relative'][data['frame.number'].count()-1]

time_bins = [i for i in range(0,round(float(end_of_capture)), length_of_bins)]

for i in time_bins:
    aux = data[(i < data['frame.time_relative']) & (data['frame.time_relative'] < (i+length_of_bins))]
    data_len.append(aux['data.len'].mean())
    nr_packets.append(aux['frame.number'].count())




a1 = matplot.figure(1)
matplot.plot(time_bins, data_len)

matplot.title("Data Length as a function of Time)")
matplot.xlabel("Time [s]")
matplot.ylabel("Data Length [bits]")

matplot.savefig(capture_file + "datalen_timePLOT")



a2 = matplot.figure(2)
matplot.plot(time_bins, nr_packets)

matplot.title("Nr of packets as a function of Time)")
matplot.xlabel("Time [s]")
matplot.ylabel("Nr of packets")

matplot.savefig(capture_file + "nrpackets_timePLOT")



matplot.show()