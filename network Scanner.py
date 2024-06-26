import socket
import threading

# Set up the target IP range
target_ip_range = "192.168.1."

# Function to scan a single IP address
def scan_ip(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, 22))  # Port 22 for SSH
        if result == 0:
            print(f"{ip} is open")
        sock.close()
    except socket.error:
        print(f"{ip} is not open")

# Scan the IP range using multiple threads
threads = []
for i in range(1, 255):
    ip = target_ip_range + str(i)
    t = threading.Thread(target=scan_ip, args=(ip,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()