import socket

target = input("target IP or hostname: ")

try:
    ip = socket.gethostbyname(target)
except socket.gaierror:
    print("invalid hostname")
    exit()

start_port = int(input("start port: "))
end_port = int(input("end port: "))

if not (1 <= start_port <= 65535):
    print("invalid start port")
    exit()
if not (start_port <= end_port <= 65535):
    print("invalid end port")
    exit()

print("\nscanning:", ip, "\n")

for port in range(start_port, end_port+1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.01)
            result = s.connect_ex((ip, port))

            if result == 0:
                print(f" {port}: OPEN")

    except socket.error as e:
        print(f"error on port {port}: {e}")

print("\nDONE.")
#MadMad_36