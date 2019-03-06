sudo airmon-ng start wlx00117f1b1e50
sudo ifconfig wlan0mon -trailers allmulti up multicast promisc
ifconfig
sudo airodump-ng wlan0mon
