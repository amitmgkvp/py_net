import socket
import struct
import binascii

rawsocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
ip_port_dict = {}
while True:
	pkt = rawsocket.recvfrom(2048)
	
#Print EthernetHeader
	ether_header = pkt[0][0:14]
	ether_hdr = struct.unpack("!6s6s2s", ether_header)
	#print("Destination Address: "+str(binascii.hexlify(ether_hdr[0])))
	#print("Source Address: "+str(binascii.hexlify(ether_hdr[1])))
	#print("Packet Type: "+str(binascii.hexlify(ether_hdr[2])))
#	print("----------------------------------------------------------")
#Print IP Header
	ip_header = pkt[0][14:34]
	ip_hdr = struct.unpack("!12s4s4s", ip_header)
	#ip_set.add(socket.inet_ntoa(ip_hdr[1]))
	#print("Source IP Address: "+str(socket.inet_ntoa(ip_hdr[1])))
	#print("Destination IP Address: "+str(socket.inet_ntoa(ip_hdr[2])))
#Print TCP Header	
	tcp_header = pkt[0][34:54]
	tcp_hdr = struct.unpack("!HH16s", tcp_header)
	#port_set.add(str(tcp_hdr[1]))
	#print("Source_Port: "+str(tcp_hdr[0])) 
	#print("Destination Port: "+str(tcp_hdr[1]))
	#print("------------------------------------------------------------")
	#print(ip_set)
	#print("--------------")
	#print(port_set)
	if(str(socket.inet_ntoa(ip_hdr[1])) not in ip_port_dict):
		port_list = set([str(tcp_hdr[1])])
		ip_port_dict[str(socket.inet_ntoa(ip_hdr[1]))] = port_list
	else:
		port_list = ip_port_dict[str(socket.inet_ntoa(ip_hdr[1]))]
		port_list.add(str(tcp_hdr[1]))
		ip_port_dict[str(socket.inet_ntoa(ip_hdr[1]))] = set(port_list)

	max_port = 0
	max_ip = ''
	for key in ip_port_dict.keys():
		lent = len(ip_port_dict[key])
		#print(lent)
		if(max_port < int(lent)):
			max_port = len(ip_port_dict[key])
			max_ip = key
	print(max_ip+" "+str(max_port))
