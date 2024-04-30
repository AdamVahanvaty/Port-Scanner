#imports the necessary modules for port scanning
import socket
import sys

#The scan_ports function which passes the input IP.
def scan_ports(ip):
    #These are the ports that need to be scanned for the inputted IP
    ports = [80, 443, 22, 25, 53]
    #Sets the default timeout for port response to 0.1 seconds (100ms) 
    timeout = 0.1
    #loops through each of the listed ports for the IP and attempts to connect
    for port in ports:
        try:
            #Create a socket object that will be used for connecting to ports. AF_INET specifies its IPV4 and SOCK_STREAM is the type of socket used. This type uses TCP which is essential for knowing if the port is open or not. (TCP Handshake) If the port is open it responds with SYN-ACK, if closed it responds with RST (reset).
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #sets the default timeout for the socket.
            s.settimeout(timeout)
            
            #attempts to connect to the specific port for the IP and stores the result in a variable. 0 = no error, != 0 = error
            result = s.connect_ex((ip, port))
            
            #Check if the connection was successful, if it was print "Port <PORT> is open", if not print "Port <PORT> is closed"
            if result == 0:
                print("Port " + str(port) + " is open")
            else:
                print("Port " + str(port) + " is closed")
                
            #Close the socket object after the scan is complete
            s.close()
            
        except socket.timeout:
            #Catches any socket error exceptions if the default timeout value is exceeded
            print("Connection to port " + str(port) + " timed out")
            
        except socket.error as e:
            #Catches any socket error exceptions that occur during the scanning process, outputting the port and the specific error
            print("Socket Error " + str(port) + ": " + str(e))
            
        except KeyboardInterrupt:
            #Catches any exceptions when user manually stops scan (ctrl + c) and stops the program
            print("Scan Stopped")
            sys.exit()
            
        except Exception as e:
            #Catches any other exceptions that may arise during scanning process and prints a generic error message
            print("Error: " + str(e))
            
#calls the main function when the script is run
if __name__ == "__main__":
    #If number of commands in CLI != 2, prints a guide and exits program
    if len(sys.argv) != 2:
        print("Help: python port_scanner.py <IP ADDRESS>")
        sys.exit(1)
        
    #Gets IP from CLI argument and stores in variable. (e.g. python port_scanner.py 192.168.0.1) (argv[0]) = port_scanner.py | (argv[1]) = 192.168.0.1
    ip = sys.argv[1]
    
    #this calls the scan_ports function with the input IP, starting the scanning process
    scan_ports(ip)
