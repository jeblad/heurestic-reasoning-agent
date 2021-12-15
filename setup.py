
import socket
import setuptools
from time import strftime

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsocketname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
    
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

ip_address__ = get_ip()

setuptools.setup(
    control_url = 'https://%s/hera/'%(get_ip()),
    copyright = '(C) John Erling Blad, 2021-' + strftime('%Y'),
    scripts=['bin/hera']
)