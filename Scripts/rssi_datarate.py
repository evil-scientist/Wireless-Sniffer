import pandas as pd 
import matplotlib.pyplot as matplot
import numpy as  np

capture_file = "netflix" #without the .pcap extension

data = pd.read_csv(capture_file + "_results.csv")

rate_values = []
rssi_values = []

colors_list = ['white', 'yellow', 'black', 'cyan', 'red', 'magenta', 'blue', 'green' ]
phy_meanings = ['none0', 'none1', 'none2', 'none3', '802.11b',
                                 'none5', '802.11g', '802.11n']

possible_rssi_values = [i for i in range(-100,0, 1)]

possible_phy_values = [i for i in range(1,7+1)]  #range for wlan_radio.phy (1-7)
wanted_phy_values = [4, 6, 7]

#just so that the each phy value corresponds to the required plot and no (k-1) is necessary
rate_values.append([])
rssi_values.append([])

for i in possible_phy_values:  #min and max values for wlan_radio.phy
    rate_values.append([])
    rssi_values.append([])



for k in possible_phy_values:
    for i in possible_rssi_values:
        rate_values[k].append(data[(data['wlan_radio.signal_dbm'] == i) & 
            (data['wlan_radio.phy'] == k)]['wlan_radio.data_rate'].mean())
        rssi_values[k].append(i)
    if k in wanted_phy_values:
        print(str(k) + " is done\n")
        matplot.scatter(rssi_values[k], rate_values[k], 
                    marker='x', s = 5**2, color=colors_list[k], label=phy_meanings[k])
    



print("Done :)")

matplot.legend()
matplot.title("Data Rate as a function of Signal Strength)")
matplot.xlabel("Signal Strength [dBm]")
matplot.ylabel("Data Rate [Mbps]")

matplot.savefig(capture_file + "_rssi_dataratePLOT")
matplot.show()
#matplot.figure()

