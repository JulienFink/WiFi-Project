# Deauthentication

* ### What is it about ?
As shown in the *.pcapng file, multiple deauthentications are carried out by device X. However, this is actually a fake deauthentication performed by device Z who copied the MAC address of device X, resulting in an interruption of the Wi-Fi connection for device X.
<br>
<br> Device Z remains totally anonymous since the 802.11 protocol does not require any authentication to perform a deauth.
<br>
<br> Device X can only retrieve his Wi-fi connection if :
<br> - device Z interrupts the attack,
<br> - or if device X changes its MAC address software-side.
