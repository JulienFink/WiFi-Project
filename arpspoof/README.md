# Arpspoof

* ### Prerequisites
0. Check the 'requirements.txt' file

* ### Usage
This script provides an arpspoof detection by analysing a *.pcapng, *.pcap, *.cap, *.snoop file.
<br> If the same IP address refers to two different MAC addresses within a capture file, this eRrOr is detected and printed to the user.

1. Run the following command :  
```
python arpspoof_detection.py --file arpspoof_capture.pcapng
```
Just replace the --file parameter by your own file ^^.
