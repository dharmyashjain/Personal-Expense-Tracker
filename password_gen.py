# Password Generator CLI
# Generates secure passwords with customizable length and character sets.
# Usage: python password_gen.py --length 16 --count 3 --no-symbols

import random
import string
import argparse

def generate_password(length, use_symbols=True, use_digits=True):
    # Start with letters as the base character pool
    chars = string.ascii_letters

    # Add digits if the user hasn't disabled them
    if use_digits:
        chars += string.digits

    # Add symbols if the user hasn't disabled them
    if use_symbols:
        chars += "!@#$%^&*"

    # Randomly pick characters from the pool to build the password
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    # Set up command-line arguments so the user can customize the output
    parser = argparse.ArgumentParser(description="Secure password generator")
    parser.add_argument("--length", type=int, default=12, help="Password length (default: 12)")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude special symbols")
    parser.add_argument("--no-digits", action="store_true", help="Exclude numbers")
    parser.add_argument("--count", type=int, default=1, help="How many passwords to generate")
    args = parser.parse_args()

    # Generate and print each password with a numbered label
    for i in range(args.count):
        pwd = generate_password(args.length, not args.no_symbols, not args.no_digits)
        print(f"[{i+1}] {pwd}")

if __name__ == "__main__":
    main()
