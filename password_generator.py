import argparse
import string
import random

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special=True):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase     # A string containing all ASCII uppercase letters
    if include_lowercase:
        characters += string.ascii_lowercase     # A string containing all ascii lowercase letters
    if include_digits:
        characters += string.digits              # A string containing all digits 0 to 9
    if include_special:
        characters += string.punctuation         # A string containing all punctuation characters

    password = "".join(random.choices(characters, k=length))
    return password

if __name__ == "__main__":
     # Parse command-line arguments for specifying the password length and character set options
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("length", type=int, help="Length of the password")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Include uppercase letters")
    parser.add_argument("-l", "--lowercase", action="store_true", help="Include lowercase letters")
    parser.add_argument("-d", "--digits", action="store_true", help="Include digits")
    parser.add_argument("-s", "--special", action="store_true", help="Include special characters")
    args = parser.parse_args()
    
    # Generating password based on the command-line arguments
    password = generate_password(args.length, args.uppercase, args.lowercase, args.digits, args.special) 
    print(f"Generated password: {password}")