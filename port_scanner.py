
import socket

print("PORT SCANNER")

target = input("Enter target IP address: ")

print("Scanning target:", target)
print("Scanning ports 1-1024...\n")

for port in range(1, 1025):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print("Port open:", port)

    s.close()

print("\nScan complete.")
