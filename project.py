import socket
import termcolor


def scan(target, ports):
    open_ports_count = 0  # Initialize the counter for open ports
    print('\n' + ' Starting Scan For ' + str(target))
    for port in range(1, ports + 1):
        if scan_port(target, port):
            open_ports_count += 1  # Increment the counter if the port is open
    print(termcolor.colored(f"\n[+] {open_ports_count} open ports found on {target}", 'yellow'))


def scan_port(ipaddress, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to avoid long waits
        sock.connect((ipaddress, port))
        print(termcolor.colored(f"[+] Port {port} is Open", 'green'))
        sock.close()
        return True  # Return True if the port is open
    except (socket.timeout, ConnectionRefusedError):
        print(termcolor.colored(f"[-] Port {port} is Closed", 'red'))  # Indicate that the port is closed
        return False  # Return False if the port is closed
    except Exception as e:
        print(termcolor.colored(f"[-] Error scanning port {port}: {e}", 'red'))
        return False


targets = input("[*] Enter Targets To Scan (separated by commas): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

if ',' in targets:
    print(termcolor.colored("[*] Scanning Multiple Targets", 'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), ports)
else:
    scan(targets.strip(), ports)

