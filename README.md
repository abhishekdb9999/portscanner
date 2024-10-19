
## Port Scanner

This Python script scans a specified target IP address (or multiple addresses) to identify open and closed ports within a given range. It's a valuable tool for network diagnostics and security testing.

### Features

- Scan multiple target IP addresses simultaneously.
- Identify both open and closed ports for enhanced visibility.
- Colored terminal output for improved readability.
- Error handling to gracefully manage connection issues.

### Prerequisites

- Python 3.x installed on your system.
- The `termcolor` module for colored output in the terminal. You can install it using:

```bash
pip install termcolor
```

### Installation

1. **Clone the repository or download the script file (port_scanner.py).**
2. **Open your terminal and navigate to the directory containing the script.**

### Usage

1. **Run the script using the following command:**

```bash
python port_scanner.py
```

2. **When prompted, enter the target IP address(es):**
   - Enter a single IP address for a single target (e.g., 192.168.1.1).
   - Separate multiple IP addresses with commas (e.g., 192.168.1.1, 192.168.1.2).

3. **Enter the number of ports you want to scan.**

### Example Output

```
[*] Enter Targets To Scan (separated by commas): 192.168.1.1
[*] Enter How Many Ports You Want To Scan: 10

Starting Scan For 192.168.1.1
[+] Port 22 is Open
[-] Port 23 is Closed
...
[+] 1 open ports found on 192.168.1.1
```

### How It Works

The script utilizes the Python `socket` library to check each specified port on the target IP address. It attempts to establish a connection to each port:

- If the connection succeeds, the port is marked as open.
- If the connection fails or times out, the port is marked as closed.

### Limitations

- This tool scans TCP ports only.
- Port scanning on networks you don't own or have permission to test might be illegal. Use responsibly.

### Contributing

We welcome contributions to this project! Feel free to fork the repository and submit a pull request with your improvements.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments

- Built using the Python `socket` module for networking functionality.
- Uses `termcolor` for colorful terminal output to enhance user experience.

