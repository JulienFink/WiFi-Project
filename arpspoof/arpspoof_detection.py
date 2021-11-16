
import argparse;
from scapy.all import *;

###############################################################################
def arpspoof_guard(filename):
        
    filename = "arpspoof_capture.pcapng";    
    packets = rdpcap(filename);
    
    #Keep only the ARP packets
    packets = packets.filter(lambda packet: ARP in packet);
    
    #Create a dictionary to match IP addresses with MAC addresses
    IP_with_MAC = {};
    i = 0;
    
    for packet in packets:
        i += 1;
        
        #if packet["ARP"].op is equal to 1, then the operation is "who-has"
        #if packet["ARP"].op is equal to 2, then the operation is "is-at"        
        if( packet["ARP"].op == 2 ):
            
            #If the IP is already in the dictionary
            if( packet["ARP"].psrc in IP_with_MAC ):
                
                #If the same IP address has two different MAC addresses ! 
                if(packet["ARP"].hwsrc != IP_with_MAC[packet["ARP"].psrc]):
                    print(f"\nFor the IP address {packet['ARP'].psrc}," 
                          +" multiple MAC addresses were found :");
                    print("\t● " + packet["ARP"].hwsrc);
                    print("\t● " + IP_with_MAC[packet["ARP"].psrc]);
                    print(f"\nArpspoofing attack detected packet n°{i}.");
            
            if( packet["ARP"].psrc not in IP_with_MAC ):
                IP_with_MAC[packet["ARP"].psrc] = packet["ARP"].hwsrc;
    
###############################################################################
def main():
    
    parser = argparse.ArgumentParser();
    parser.add_argument("--file", help='path of the capture file', nargs='+');
    args = parser.parse_args();

    if args.file:
        arpspoof_guard(args.file);
    else:
        print("Please provide the file you want to analyse...");

###############################################################################
if __name__ == '__main__':
    main();

