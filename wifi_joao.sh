sudo airmon-ng start wlp2s0
sudo ifconfig wlp2s0mon -trailers allmulti up multicast promisc
iwconfig
sudo airodump-ng wlan0mon
