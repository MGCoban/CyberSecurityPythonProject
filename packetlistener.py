import scapy.all as scapy
from scapy_http import http
def listen_packet(interface):
    scapy.sniff(iface=interface,store=False,prn=analyze_packets)
    #prn = callback function 
def analyze_packets(packet):
    #packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

listen_packet("eth0")        


#Tam bitmedi!!! Sadece http dinliyor!!!