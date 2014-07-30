xss2shell
=========

xss2shell is a piece of software which allows you to get instant php code execution on wordpress installations via XSS vulnerabilities. The tool is designed to operate as follows:

1. User generates his javascript payload by using the python builder
2. User uploads the payload and injects it into an existing XSS vuln
3. Payload is triggerd by a WP admin, and the attacker's php is evaled

Some notes:
  1. The current footer.php file that's used by xss2shell is from the twentyfourteen theme.
  2. While xss2shell can be used with any theme, footer.php will still be replaced with the one included
  3. When using a custom PHP payload, remove all PHP tags so that it will be evaled correctly
  4. When entering a theme name, make sure it matches what wordpress uses exactly.

Future Goals:
  1. Joomla Implementation

Feel free to contribute to this repo by reporting bugs or making productive pull requests.
