import os
import hashlib
from cryptography.fernet import Fernet

class CaesarCipher:
    def __init__(self, key=None):
        if key is None:
            if os.path.exists("key.txt"):
                self.load_key()
            else:
                self.key = self.generate_key()
                self.save_key()
        else:
            self.key = key
        self.cipher = Fernet(self.key)

    def generate_key(self):
        return Fernet.generate_key()

    def encrypt(self, plaintext):
        return self.cipher.encrypt(plaintext.encode()).decode()

    def decrypt(self, ciphertext):
        try:
            return self.cipher.decrypt(ciphertext.encode()).decode()
        except Exception as e:
            return f"Error during decryption: {e}"

    def save_key(self, filename="key.txt"):
        with open(filename, "wb") as f:
            f.write(self.key)

    def load_key(self, filename="key.txt"):
        try:
            with open(filename, "rb") as f:
                self.key = f.read()
                self.cipher = Fernet(self.key)
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
        choice = input("Would you like to (e)encrypt / (d)decrypt / (ef)encrypt file / (df)decrypt file / (s)Save key / (l)load key / (v)verify integrity / (q)quit? ").lower()
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

