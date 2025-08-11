                                                                                                                    
┌──(alvan㉿vbox)-[~/htb/rainbow]
└─$ ftp 10.129.234.171      
Connected to 10.129.234.171.
220 Microsoft FTP Service
Name (10.129.234.171:alvan): 
331 Password required
Password: 
530 User cannot log in.
ftp: Login failed
ftp> quit
221 Goodbye.
                                                                                                                    
┌──(alvan㉿vbox)-[~/htb/rainbow]
└─$ ftp 10.129.234.171
Connected to 10.129.234.171.
220 Microsoft FTP Service
Name (10.129.234.171:alvan): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> ls
229 Entering Extended Passive Mode (|||50100|)
125 Data connection already open; Transfer starting.
01-18-22  08:22AM                  258 dev.txt
01-18-22  08:30AM                54784 rainbow.exe
01-16-22  01:34PM                  479 restart.ps1
01-16-22  12:14PM       <DIR>          wwwroot
226 Transfer complete.
ftp> get dev.txt
local: dev.txt remote: dev.txt
229 Entering Extended Passive Mode (|||50101|)
125 Data connection already open; Transfer starting.
100% |***********************************************************************|   258        0.96 KiB/s    00:00 ETA
226 Transfer complete.
WARNING! 5 bare linefeeds received in ASCII mode.
File may not have transferred correctly.
258 bytes received in 00:00 (0.96 KiB/s)
ftp> get rainbow.exe
local: rainbow.exe remote: rainbow.exe
229 Entering Extended Passive Mode (|||50102|)
125 Data connection already open; Transfer starting.
100% |***********************************************************************| 54784       68.21 KiB/s    00:00 ETA
226 Transfer complete.
WARNING! 78 bare linefeeds received in ASCII mode.
File may not have transferred correctly.
54784 bytes received in 00:00 (68.18 KiB/s)
ftp> get restart.ps1
local: restart.ps1 remote: restart.ps1
229 Entering Extended Passive Mode (|||50103|)
125 Data connection already open; Transfer starting.
100% |***********************************************************************|   479        1.92 KiB/s    00:00 ETA
226 Transfer complete.
479 bytes received in 00:00 (1.91 KiB/s)
ftp> cd wwwroot
250 CWD command successful.
ftp> ls
229 Entering Extended Passive Mode (|||50104|)
125 Data connection already open; Transfer starting.
01-16-22  11:48AM                 1523 index.html
226 Transfer complete.
ftp> get index.html
local: index.html remote: index.html
229 Entering Extended Passive Mode (|||50105|)
125 Data connection already open; Transfer starting.
100% |***********************************************************************|  1523        5.93 KiB/s    00:00 ETA
226 Transfer complete.
1523 bytes received in 00:00 (5.90 KiB/s)
ftp> ls -la
229 Entering Extended Passive Mode (|||50106|)
125 Data connection already open; Transfer starting.
01-16-22  11:48AM                 1523 index.html
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> pwd
Remote directory: /
ftp> ls -la
229 Entering Extended Passive Mode (|||50107|)
125 Data connection already open; Transfer starting.
01-18-22  08:22AM                  258 dev.txt
01-18-22  08:30AM                54784 rainbow.exe
01-16-22  01:34PM                  479 restart.ps1
01-16-22  12:14PM       <DIR>          wwwroot
226 Transfer complete.
ftp> quit
221 Goodbye.
                                                                                                                    
┌──(alvan㉿vbox)-[~/htb/rainbow]
└─$ ls
dev.txt  index.html  nmap_scan  rainbow.exe  restart.ps1
                                                                                                                    
┌──(alvan㉿vbox)-[~/htb/rainbow]
└─$ cat dev.txt              
* Our webserver has been crashing a lot lately. Instead of touching the code we added a restart script! 
* The server will dynamically pick a port when its default port is unresponsive (8080-8090).
* We'll fix this later by adding load balancer.

- dev team
                                                                                                                    
┌──(alvan㉿vbox)-[~/htb/rainbow]
└─$ cat restart.ps1
Set-Location -Path c:\rainbow
for(;;){
try{
If (!(Get-Process -Name rainbow -ErrorAction SilentlyContinue))
{Invoke-Expression "C:\rainbow\rainbow.exe" }
$proc = Get-Process -Name rainbow | Sort-Object -Property ProcessName -Unique -ErrorAction SilentlyContinue
If (!$proc -or ($proc.Responding -eq $false) –or ($proc.WorkingSet -GT 200000*1024)) {
$proc.Kill()
Start-Sleep -s 10
Invoke-Expression "C:\rainbow\rainbow.exe"}
}
catch    {    }
Start-sleep -s 30
}                                                                                                                    
