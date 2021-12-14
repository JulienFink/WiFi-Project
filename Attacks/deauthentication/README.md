# Deauthentication

![Demonstration of the script](https://user-images.githubusercontent.com/64968597/142769016-4318cf68-400f-47e0-acb2-cfa2ccb6a31f.png)

* ### What is it about ?
As shown in the *.pcapng file, multiple deauthentications are carried out by device X. However, this is actually a fake deauthentication performed by device Z who copied the MAC address of device X, resulting in an interruption of the Wi-Fi connection for device X.
<br>
<br> Device Z remains totally anonymous since the 802.11 protocol does not require any authentication to perform a deauthentication.
<br>
<br> Device X can only retrieve his Wi-fi connection if :
<br> - device Z interrupts the attack,
<br> - or if device X changes its MAC address software-side.

* ### Usage
This script provides a deauthentication detection by analysing a *.json.
<br>
<br> If some deauthentication packets are detected, these ErROrS are detected and printed to the user.

1. Run the following command :  
```
python deauth_detection.py --file deauthentication_capture.json
```
Just replace the --file parameter with your own file after converting it to a *.json format ^^.
