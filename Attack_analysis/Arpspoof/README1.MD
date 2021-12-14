# Arpspoof

![Demonstration of the script](https://user-images.githubusercontent.com/64968597/142011794-6b83546b-a5ee-414f-8385-699e8221d9f7.png)

* ### Prerequisites
0. Check the 'requirements.txt' file

* ### Usage
This script provides an arpspoof detection by analysing a *.pcapng, *.pcap, *.cap, *.snoop file.
<br>
<br> If the same IP address refers to two different MAC addresses within a capture file, this ErROr is detected and printed to the user.

1. Run the following command :  
```
python arpspoof_detection.py --file arpspoof_capture.pcapng
```
Just replace the --file parameter with your own file ^^.
