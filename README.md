# Python Scapy Firewall

## Project Overview
This project is a simple Python-based firewall/Network Dectection System built using the Scapy library to monitor and filter network traffic based on IPs and ports.

## Features
- Monitor incoming network traffic using Scapy.
- Block traffic to specific ports based on defined rules.
- Allow all IP addresses (no IP filtering), but log and filter traffic based on allowed ports.
- Real-time logging of both blocked and allowed traffic.

## Technologies used
- Python 3.x
- Scapy (Python based interactive packet manipulation program)
- Kali Linux OS

## Setup Instructions

### Prerequisites
- **Python 3.x** installed.
- **Scapy** installed via pip:
    ```bash
    pip install scapy
    ```

### Steps to Run
1. **Clone this repository** to your local machine:
    ```bash
    git clone https://github.com/Rochan03/python-scapy-firewall.git
    ```

2. **Navigate into the project directory**:
    ```bash
    cd python-scapy-firewall
    ```

3. **Run the firewall script** with superuser privileges (since it requires access to network interfaces):
    ```bash
    sudo python3 firewall.py
    ```

### Example Output
Once you run the firewall, you’ll see output in the terminal showing allowed and blocked traffic.
Refer here for example: [EXAMPLE OUTPUT](loggingfirewall.png)


### Customization

#### Modify Allowed Ports
You can customize which ports are allowed by modifying the `allowed_ports` list in `firewall.py`.

```python
allowed_ports = [80, 445, 5353]  # Add more ports as needed
