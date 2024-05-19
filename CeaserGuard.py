import os
import random
import string
import hashlib
from cryptography.fernet import Fernet

class CaesarCipher:
    def __init__(self, key=None):
        self.key = key or self.generate_key()

    def generate_key(self):
        return ''.join(random.choice(string.ascii_letters) for _ in range(16))

    def encrypt(self, plaintext):
        cipher = Fernet(self.key.encode())
        return cipher.encrypt(plaintext.encode()).decode()

    def decrypt(self, ciphertext):
        cipher = Fernet(self.key.encode())
        return cipher.decrypt(ciphertext.encode()).decode()

    def save_key(self, filename="key.txt"):
        with open(filename, "w") as f:
            f.write(self.key)

    def load_key(self, filename="key.txt"):
        try:
            with open(filename, "r") as f:
                self.key = f.read()
        except FileNotFoundError:
            print("Key file not found.")

    def verify_integrity(self, filename):
        with open(filename, "rb") as f:
            original_hash = hashlib.sha256(f.read()).hexdigest()
        return original_hash == self.calculate_hash(filename)

    def calculate_hash(self, filename):
        with open(filename, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    def encrypt_file(self, input_file, output_file):
        try:
            with open(input_file, 'r') as file:
                plaintext = file.read()
                ciphertext = self.encrypt(plaintext)
            with open(output_file, 'w') as file:
                file.write(ciphertext)
            print(f"Encrypted file saved as: {output_file}")
        except FileNotFoundError:
            print(f"File not found: {input_file}")

    def decrypt_file(self, input_file, output_file):
        try:
            with open(input_file, 'r') as file:
                ciphertext = file.read()
                plaintext = self.decrypt(ciphertext)
            with open(output_file, 'w') as file:
                file.write(plaintext)
            print(f"Decrypted file saved as: {output_file}")
        except FileNotFoundError:
            print(f"File not found: {input_file}")

def main():
    cipher = CaesarCipher()

    while True:
        choice = input("Would you like to (e)encrypt /n (d)decrypt /n (ef)encrypt file /n (df)decrypt file /n (s)Save key /n (l)load key /n (v)verify integrity /n  (q)quit? ").lower()
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice == 'e':
            plaintext = input("Enter the message to encrypt: ")
            print("Encrypted message:", cipher.encrypt(plaintext))
        elif choice == 'd':
            ciphertext = input("Enter the message to decrypt: ")
            print("Decrypted message:", cipher.decrypt(ciphertext))
        elif choice == 'ef':
            input_file = input("Enter the input file path: ")
            output_file = input("Enter the output file path: ")
            cipher.encrypt_file(input_file, output_file)
        elif choice == 'df':
            input_file = input("Enter the input file path: ")
            output_file = input("Enter the output file path: ")
            cipher.decrypt_file(input_file, output_file)
        elif choice == 's':
            cipher.save_key()
            print("Key saved successfully.")
        elif choice == 'l':
            cipher.load_key()
            print("Key loaded successfully.")
        elif choice == 'v':
            filename = input("Enter the file path to verify integrity: ")
            print("Integrity verified:", cipher.verify_integrity(filename))
        else:
          print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

