"""
Python Port Scanner

Description:
    Scans a given target host for open ports using the python-nmap librar.
    This version supports service detetction (-sV) and Nmap's default script scan (-sC).

Disclaimer:
    This tool has only been used on networks and systems I own or have explicit permission to scan.
"""


import nmap 

# --- Configuration ---
target = "45.33.32.156" 
options = "-sV -sC scan_results" 

# --- Create the scanner instance --- 
scanner = nmap.PortScanner()


                                 
scanner.scan(target, arguments=options)

# --- Process results ---
# Loops through each discovered host and displays its scan results
# For rach host, list of all protocols are found and the open/closed state of each port
for host in nm.all_hosts(): # Outer loop iterates list of hosts, returned by all_hosts method of scanner
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for protocol in nm[host].all_protocols(): # Inner loop iterates through list of protocols, used by that indivdual host, returns a list of protocols (TCP UDP dicovered during host scan)
        print("Protocol: %s" % protocol)
        port_info = nm[host][protocol]
        for port, state in port_info.items(): # Inner most loop iterates through the list of ports and their states for the current protocol
            print("Port: %s\tState: %s" % (port, state))
