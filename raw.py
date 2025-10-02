import sys
from getmac import get_mac_address
from scapy.all import Ether, sendp, Raw

def send_ether_frame(nic, dst_mac, msg):
    # 1. Auto-detect source MAC address
    src_mac = get_mac_address(interface=nic)

    print(f"Using NIC: {nic}")
    print(f"Source MAC address: {src_mac}")
    print(f"Target MAC address: {dst_mac}")

    # 2. Create Ethernet frame
    ethernet_frame = Ether(dst=dst_mac, src=src_mac) / Raw(load=msg)

    print("\n--- Frame to send ---")
    ethernet_frame.show()
    print("--------------------\n")

    # 3. Send the Ethernet frame
    sendp(ethernet_frame, iface=nic, verbose=True)

    print(f"\nSuccessfully sent to {dst_mac}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage：sudo python raw.py <NIC name> <Destination MAC address>")
        print("Example(Linux): sudo python raw.py eth0 00:11:22:33:44:55")
        print("Example(Windows): python raw.py \"乙太網路\" 00:11:22:33:44:55")
        sys.exit(1)

    nic_name = sys.argv[1]
    dst_mac = sys.argv[2]
    dst_mac = dst_mac.replace('-', ':')
    msg = "Test message from raw.py"

    send_ether_frame(nic_name, dst_mac, msg)