import socket
import ipaddress
import re
import common_ports

def get_open_ports(target, port_range=[], vebrose=False):
  open_ports = []
  s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  istargetip = re.findall("\d",target);

  if(istargetip):
    try:
      high = ipaddress.ip_address(target)

    except ValueError:
       return "Error: Invalid IP address";
    
  else:
   try: 
     low = socket.gethostbyname(target)
   except socket.gaierror: 
   #return low;
    # if(socket.gethostbyname(target)):
    #   return "ip address"
     return "Error: Invalid hostname";     

  if(vebrose):
     port_str = "";
     if(istargetip):
       port_str="Open ports for "+target+"\n";
     else:
       port_str="Open ports for "+target+" "+"("+socket.gethostbyname(target)+")\n" 

     port_str+="PORT     SERVICE\n"

     for portnum in range(port_range[0],port_range[1]):
         if(s.connect_ex((target,portnum))):
           port_str+=portnum
           add_space=" "*(4-len(portnum));
           port_str+=add_space+"     "+common_ports.ports_and_services[portnum]+"\n"
     return port_str;

  else:  
     for portnum in range(port_range[0],port_range[1]):
         if(s.connect_ex((target,portnum))):
             open_ports.append(portnum);
     return open_ports