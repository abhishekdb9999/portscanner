import socket
import tkinter as tk
from tkinter import messagebox, ttk

def scan_port(ipaddress, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to avoid long waits
        sock.connect((ipaddress, port))
        sock.close()
        return True  # Return True if the port is open
    except (socket.timeout, ConnectionRefusedError):
        return False  # Return False if the port is closed
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return False

def scan():
    target = target_entry.get()
    try:
        ports = int(ports_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of ports.")
        return

    if not target:
        messagebox.showerror("Input Error", "Please enter a target IP address.")
        return

    results_text.delete(1.0, tk.END)  # Clear previous results
    targets = [t.strip() for t in target.split(',')]
    for ip_addr in targets:
        open_ports_count = 0
        results_text.insert(tk.END, f"\nScanning {ip_addr}...\n")
        for port in range(1, ports + 1):
            if scan_port(ip_addr, port):
                results_text.insert(tk.END, f"[+] Port {port} is Open\n")
                open_ports_count += 1
        results_text.insert(tk.END, f"[+] {open_ports_count} open ports found on {ip_addr}\n")

# Create the main window
root = tk.Tk()
root.title("Port Scanner")
root.geometry("500x400")
root.resizable(False, False)

# Create and place widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Target entry
ttk.Label(frame, text="Target(s):", font=("Arial", 10)).grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
target_entry = ttk.Entry(frame, width=40, font=("Arial", 10))
target_entry.grid(row=0, column=1, padx=5, pady=5)

# Ports entry
ttk.Label(frame, text="Ports to Scan:", font=("Arial", 10)).grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
ports_entry = ttk.Entry(frame, width=10, font=("Arial", 10))
ports_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

# Scan button
scan_button = ttk.Button(frame, text="Start Scan", command=scan)
scan_button.grid(row=2, column=0, columnspan=2, pady=10)

# Results display
results_text = tk.Text(frame, height=15, width=60, font=("Courier New", 10))
results_text.grid(row=3, column=0, columnspan=2, pady=10)

# Add a scrollbar
scrollbar = ttk.Scrollbar(frame, command=results_text.yview)
scrollbar.grid(row=3, column=2, sticky=(tk.N, tk.S))
results_text['yscrollcommand'] = scrollbar.set

# Start the Tkinter event loop
root.mainloop()
