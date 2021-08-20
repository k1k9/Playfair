#!/usr/bin/env python3
import argparse
import re
from playfair import encrypt, decrypt

parser = argparse.ArgumentParser(description="Encrypt or decrypt your message via Playfair cipher")
parser.add_argument('-e', '--encrypt',action="store_false",help="Encrypt <plaintext> <key> (default enabled)")
parser.add_argument('-d', '--decrypt',action="store_true",help="Decrypt <cipher> <key>")
parser.add_argument('plaintext', metavar="plaintext",help="Message or cipher to encrypt or decrypt")
parser.add_argument('key', metavar="key",help="Key for cipher, only alphabetic chars!!")
args = parser.parse_args()

# Check key requirements
regex = re.compile(r'[a-ik-zA-IK-Z]')
if not regex.match(args.key):
    quit()

if args.decrypt:
    decrypted = decrypt(args.plaintext, args.key)
    print(f"\nCipher: {args.plaintext}\nKey: {args.key}\nDecrypted: {decrypted}\n")
elif not args.decrypt:
    encrypted = encrypt(args.plaintext, args.key)
    print(f"\nPlaintext: {args.plaintext}\nKey: {args.key}\nEncrypted: {encrypted}\n")
