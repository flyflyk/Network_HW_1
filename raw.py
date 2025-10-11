import sys
import time
from getmac import get_mac_address
from scapy.all import Ether, Raw, sendp, AsyncSniffer

def send_ether(nic, dst_mac, msg):
    # 1. Get source MAC address.
    src_mac = get_mac_address(interface=nic)
    print(f"Using NIC: {nic}")
    print(f"Source MAC: {src_mac}")
    print(f"Destination MAC: {dst_mac}")

    # 2. Craft the Ethernet frame.
    ether_frame = Ether(dst=dst_mac, src=src_mac) / Raw(load=msg)
    print("\n--- Frame to be sent ---")
    ether_frame.show()
    print("------------------------\n")

    # 3. Send the frame and start asynchronous sniffer.
    filter_str = f"ether src {src_mac} and ether dst {dst_mac}"
    print(f"Starting sniffer with filter: '{filter_str}'...")
    sniffer = AsyncSniffer(iface=nic, filter=filter_str)
    sniffer.start()
    time.sleep(1)
    print("Sending packet...")
    sendp(ether_frame, iface=nic, verbose=False)
    time.sleep(1)
    print("Stopping sniffer...")
    captured_packets = sniffer.stop()

    # 4. Result
    print("\n--- Result ---")
    if captured_packets:
        print(f"[SUCCESS] Captured {len(captured_packets)} packet(s) on {nic}.")
        print("Captured packet summary:")
        captured_packets.nsummary()
    else:
        print(f"[FAILURE] Did not capture the sent packet on {nic}.")
    print("---------------------------\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: sudo python raw.py <NIC name> <Destination MAC address>")
        print("Example (Linux): sudo python raw.py eth0 00:11:22:33:44:55")
        print("Example (Windows): python raw.py \"Wi-Fi\" 00:11:22:33:44:55")
        sys.exit(1)

    nic_name = sys.argv[1]
    dst_mac = sys.argv[2].replace('-', ':')
    msg = "Test message from raw.py"

    send_ether(nic_name, dst_mac, msg)