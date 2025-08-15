What ports did the threat actor initially find open? Format: from lowest to highest, separated by a comma.
<img width="959" height="503" alt="image" src="https://github.com/user-attachments/assets/aeff2a04-fcbd-4ab1-94c4-e017d3554fd7" />
tcp.flags.syn == 1 && tcp.flags.ack == 1
53,80,88,135,139,389,445,464,593,636,3268,3269,5357
The threat actor found four valid usernames, but only one username allowed the attacker to achieve a foothold on the server. What was the username? Format: Domain.TLD\username
http.authorization {HTTP Authorization header is used by clients to send credentials to a server for authentication}
<img width="957" height="204" alt="image" src="https://github.com/user-attachments/assets/e63b9756-1ead-44c6-96f8-dd6e59ebb048" />
directory.thm\larry.doe
The threat actor captured a hash from the user in question 2. What are the last 30 characters of that hash?
f8716efbaa984508ddde606756441480805ab8be8cfb018a282718f7c040cd43924c6f9afeb6171230bbd3dccc79294dcf2f877a44c1a0981aadb7bb7a9510dd52d8dda4039ef4dcb444f18c9902be1623035e10aebf16ce4bdf5f7064f480e67e96ec2eb32bad95c5a1247bd7a241273fe80e281f4e6a99926f7969fcf803190c7096b947a33407f8578d4c0fb8b52d2aa8d0405a44b72bd21e014563cb71e82aee0e12538d0d440c930b98abf766e18ddc99a964e6e812ecf8dc8994a912a02074d40e5e6906915c1d216653d45df88636b51656f2c37de2020a2fd86ee7ecf6f0afe3f509fd31144e1573f9587155616532b664cd0b50cda8d4ba469f
<img width="959" height="503" alt="image" src="https://github.com/user-attachments/assets/fea1ef08-27aa-4c37-aafe-de4c81a4034e" />

What is the user's password?
$krb5asrep$18$larry.doe@directory.thm:f8716efbaa984508ddde606756441480805ab8be8cfb018a282718f7c040cd43924c6f9afeb6171230bbd3dccc79294dcf2f877a44c1a0981aadb7bb7a9510dd52d8dda4039ef4dcb444f18c9902be1623035e10aebf16ce4bdf5f7064f480e67e96ec2eb32bad95c5a1247bd7a241273fe80e281f4e6a99926f7969fcf803190c7096b947a33407f8578d4c0fb8b52d2aa8d0405a44b72bd21e014563cb71e82aee0e12538d0d440c930b98abf766e18ddc99a964e6e812ecf8dc8994a912a02074d40e5e6906915c1d216653d45df88636b51656f2c37de2020a2fd86ee7ecf6f0afe3f509fd31144e1573f9587155616532b664cd0b50cda8d4ba469f
hashcat -m 18200 -a 0 hash.txt /usr/share/wordlists/rockyou.txt

What were the second and third commands that the threat actor executed on the system? Format: command1,command2
What is the flag?


