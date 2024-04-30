# Port Scanner

A simple port scanner implemented in Python. This tool allows you to scan ports on a specified IP address to identify open services.

## Overview

Port scanners are commonly used by security researchers to identify services available on a given machine. They work by iterating through a range of ports and attempting to connect to each port. If a connection is successful, it indicates that a service is listening on that port.

## Features

- Scans ports 80, 443, 22, 25, and 53 by default
- Supports specifying a custom IP address to scan
- Sets a default timeout for port response (100ms)
- Handles exceptions such as connection timeouts and socket errors
- Prints the open ports for the given IP address

## Usage

To use the port scanner, simply run the `port_scanner.py` script and provide the target IP address as a command-line argument:

```bash
python port_scanner.py <IP_ADDRESS>
