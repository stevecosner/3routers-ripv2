import getpass
import telnetlib


HOST = "192.168.91.135"
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"admin\n")
tn.write(b"conf t\n")
tn.write(b"hostname R2\n")
tn.write(b"int lo 0\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.write(b"exit\n")
tn.write(b"int f0/0\n")
tn.write(b"no shut\n")
tn.write(b"ip address 10.1.1.2 255.255.255.252\n")
tn.write(b"exit\n")
tn.write(b"int f0/1\n")
tn.write(b"no shut\n")
tn.write(b"ip address 10.1.1.5 255.255.255.252\n")
tn.write(b"exit\n")
tn.write(b"router rip\n")
tn.write(b"version 2\n")
tn.write(b"no auto-summary\n")
tn.write(b"network 2.0.0.0\n")
tn.write(b"network 10.0.0.0\n")
tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))
