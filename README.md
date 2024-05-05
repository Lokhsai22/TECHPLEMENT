Random Password Generator
-------------------------

This command-line tool generates random passwords with customizable length and complexity.

Usage:
  python password_generator.py 12 -u -l -d -s 

Options:
  -u, --uppercase      Include uppercase letters in the password.
  
  -l, --lowercase      Include lowercase letters in the password.
  
  -d, --digits         Include digits in the password.
  
  -s, --special        Include special characters in the password.


Examples:

  Generate a password of length (12) with uppercase letters, lowercase letters, and digits:
     python password_generator.py 12 -u -l -d

  Generate a password of length 16 with uppercase letters, lowercase letters, digits, and special characters:
     python password_generator.py 16 -u -l -d -s

  Generate a password of length 10 with only lowercase letters:
     python password_generator.py 10 -l

  Generate a password of length 8 with only digits:
     python password_generator.py 8 -d

Notes:
  - If no character sets are selected, the tool will use the default settings (uppercase, lowercase, and digits).
  - The generated password will be displayed in the console.
