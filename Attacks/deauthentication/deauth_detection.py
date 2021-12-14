
import argparse;
import os;
import sys;
import json;

###############################################################################
def deauth_guard(file):
    
    f = open(file);
    data = json.load(f);
    
    deauth_dict = {};
    
    #Check for deauthentication packets
    for pkt in data:
        if "_source" in pkt:
            if "layers" in pkt["_source"]:
                if "wlan" in pkt["_source"]["layers"]:
                    if "wlan.fc.type_subtype" in pkt["_source"]["layers"]["wlan"]:
                        if(pkt["_source"]["layers"]["wlan"]["wlan.fc.type_subtype"] == "12"):
                            
                            source_addr = pkt['_source']['layers']['wlan']['wlan.sa'];
                            receiver_addr = pkt['_source']['layers']['wlan']['wlan.ra'];
                            
                            #Only fill the dict if the address is still unknown
                            if(source_addr not in deauth_dict):
                                if(receiver_addr not in deauth_dict):
                                    deauth_dict[source_addr] = receiver_addr;
    #Display the results                                
    for (sa, ra) in deauth_dict.items():
        print(f"\t● Deauthentication attack detected on {sa} connected to AP {ra}.");
    
###############################################################################
def main():
    
    parser = argparse.ArgumentParser();
    parser.add_argument("--file", metavar='<pcap file name>',
                        help='path of the capture file', required = True);
    args = parser.parse_args();

    if args.file:          
        file = args.file;
        
        if not os.path.isfile(file):
            print(f"{file} does not exist.");
            sys.exit(-1);
        
        print('   Opening {}...\n'.format(file));
        deauth_guard(args.file); 

###############################################################################
if __name__ == '__main__':
    main();


