import socket

target = input("enter a host to scan:")
target_IP = socket.gethostbyname(target) 

try:
        for port in range(0,1000):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((target_IP, port))
        
            if result == 0:
                print("Port {}:   Open".format(port))
            
            else:
                print("Port {}:   Close".format(port))
            sock.close()

except:
    print("Hatalı durum")  