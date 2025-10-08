import sys
from scapy.all import IP, UDP, Raw, send

def send_packet(dst_ip, payload):
    print(f"Target IP address: {dst_ip}")

    # 1. Create IP packet
    packet = IP(dst=dst_ip) / UDP(dport=8888) / Raw(load=payload)
    print("\n--- Packet to sent ---")
    packet.show()
    print("--------------------\n")

    # 2. Send packet
    send(packet, verbose=True)
    print(f"\nSuccessfully sent packet to {dst_ip}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage：sudo python ip.py <Target IP address>")
        print("Example: sudo python ip.py 192.168.0.105")
        sys.exit(1)

    target_ip = sys.argv[1]
    payload = b"Test payload sent over IP."

    send_packet(target_ip, payload)