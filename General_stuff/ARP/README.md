# ARP weaknesses

1. The CAM table of the router and the ARP table of the clients are by default dymanic

2. ARP request are sent in clear text

3. Sender's MAC and IP addresses for ARP replies are never checked on previous connections to detect ARP spoofing / MiTM attacks

