# WiFi-Project

Pre-connection attacks, gaining access & post-connection attacks on WEP, WPA & WPA2. 🛰✔️

* ## Prerequisites
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

* ## Pre-connection attacks
1. Discover the networks around you:
```
airodump-ng wireless_adapter_name
```
![Discover networks around you](https://user-images.githubusercontent.com/64968597/134020395-c7a67e4b-d7d0-4a84-a155-8a67fdf449c9.JPG)

2. Sniff the packets from a specified network:
```
airodump-ng --bssid target_MAC --channel N (--write file_name) wireless_adapter_name
```

3. Deauthentication attack (disconnect any device from the network):

```
aireplay-ng --deauth time_out -a router_addr -c target_mac_addr wireless_adapter_name
```
This attack will always work ! The only way around it is to change the MAC address of the target machine.

* ## Gaining access

1. WEP cracking : (~100% success)
   
   Each packet is encrypted using a unique key stream.
   <br/> A random initialization vector (IV) is used to generate the keys stream. This initialization vector is only 24 bits long.
   <br/> The IV is too small and sent in plain text, so in busy networks, IV's will repeat, making it vulnerable to statistical attacks. Therefore, the key stream can be determined and the encryption broken.

   To crack WEP, we need a large number of packets/IVs to analyse the IVs and crack the router's key.

   Step 1:
   <br/> Capture a large number of packets 
   ```
   airodump-ng --bssid MAC --channel N --write file_name wireless_adapter_name
   ```
   
   Step 2:
   <br/> Run aircrack-ng to crack the password
   ```
   aircrack-ng .cap_file_captured_previously
   ```
   Gets cracked instantly !
   
2. WPA/WPA2 cracking : (~40% success)
   
   The goal is to capture the handshake (4 packets) between the router and a device.
   
   Step 1: 
           <br/> Run a deauthentication attack against a device connected to the router and wait for him to connect back to it OR wait for a new client to connect.
           
   Step 2:
           <br/> Catch the 4-way handshake (EAPOL) using "airodump-ng" of a client (re)connecting.
           <br/>
           <br/> In a straight forward way, the handshake doesn't contain data that helps recover the key.
           <br/> However, it contains data that can be used to compute if a key is valid or not !
           <br/> Useful information in the handshake - Message Integrity Code (MIC): SP address, STA address, AP nonce, STA nonce, EAPOL, Payload
           
   Step 3: 
           <br/> Start guessing the router's passphrase by computing the PTK and the resulting MIC (from KCK key).
           <br/> The passphrase generates the PSK --> the PSK generates the PMK --> the PMK generates the PTK --> the PTK generates the MIC with the KCK key.
           <br/>
           <br/> Create a wordlist/dictionnary:
           <br/> Example: "crunch 6 8 abc123 -o wordlist.txt" --> creates a wordlist of length 6 to 8 with characters abc123 in a file called wordlist.txt
           <br/> Argument "-d 1@" is specified for non-repeating letters.
           
   ```
   aircrack-ng file_containing_handshake.cap -w word_list
   ```
   Step 4 : 
           <br/> The aircrack-ng command will generate new MICs from the wordlist and compare each of them to the (2nd message) MIC of the 4-way handshake.
           <br/> if(new_MIC == MIC_handshake), then the passphrase generating this MIC is the router's password !
           
            
https://user-images.githubusercontent.com/64968597/134026257-af761b17-4b0b-4c87-95aa-b7999ee1a2b3.mp4

![password_crack](https://user-images.githubusercontent.com/64968597/134026466-bfc08a47-8d84-4f6f-98af-816a25209824.JPG)


   Another method:
            <br/> Exploit the WPS feature (except if PBC is enabled: Push Button Authentication)
            <br/> The WPS feature allows clients to connect without a password.
            <br/> Authentication is done using a 8 digit pin, which can be cracked under a minute.

* ## Post-connection attacks

![https_bypass_blur](https://user-images.githubusercontent.com/64968597/134031635-1eb1f336-2dc0-4400-8f64-566ddcf44f2f.png)

1. ARP poisoning using bettercap, arpspoof, etc.:
   <br/> The captured packets are then easily analysed (using Wireshark) to gather passwords, emails, usernames, etc.
