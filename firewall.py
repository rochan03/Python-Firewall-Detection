
#necessary imports in order for the script to work
from scapy.all import sniff, IP, TCP, UDP

#main function that make sure the firewall function works
def firewall():

    #This could be changed in your liking (I allowed all IPS)
    allowed_ips = []

    #This could be changed in your liking
    blocked_ips = ['192.168.0.216']

    #List of blocked Ports - you can change this
    allowed_ports = [80, 445, 5353]

    def log_to_terminal(message):
        print(message)

    # function to check traffic in each packet
    def check_traffic(packet):
        if packet.haslayer(IP):
            source_ip = packet[IP].src
            
            #Uncomment if you added allowed IPS on line 9
            #if source_ip in blocked_ips:
                #log_to_terminal(f"{source_ip} is blocked. Not Allowed")
                #return
            
            #check if the packet is TCP OR UDP
            if packet.haslayer(TCP) or packet.haslayer(UDP):
                destination_port = packet[TCP].dport if packet.haslayer(TCP) else packet[UDP].dport

                #Check if the destination port is not in the allowed port list
                if destination_port not in allowed_ports:
                     log_to_terminal(f"port: {destination_port} is not allowed")
                     return
                log_to_terminal(f"allowded traffic from {source_ip}")

    #This captures packets and applies the check_traffic function
    sniff(prn = check_traffic, filter = "ip", store = 0)

if __name__ == "__main__":
    firewall()







