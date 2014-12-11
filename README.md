XSS2SHELL v3
=========

Changelog:<br />
v3 - Akismet is now used for backdooring WP; Themes are no longer used.<br />
V2 - Added Joomla support

Videos:<br />
Exploiting CVE-2014-9031 with XSS2SHELL (V3): http://youtu.be/hRIuaLQfOhs<br />
XSS2SHELL - Video Walkthrough & Introduction (V1): http://youtu.be/-EGUfPgK_lw

XSS2SHELL is a piece of software which allows you to get instant php code execution on WordPress and Joomla! installations via XSS vulnerabilities. The tool is designed to operate as follows:

1. User generates his javascript payload by using the python builder
2. User uploads the payload and injects it into an existing XSS vuln
3. Payload is triggerd by a WP/Joomla! admin, and the attacker's php is evaled

Some notes:
  1. The WordPress payload is always saved to "/wp-content/plugins/akismet/index.php"
  2. The Joomla! payload is always saved to "/administrator/templates/isis/pay.php"

Feel free to contribute to this repo by reporting bugs or making productive pull requests.
