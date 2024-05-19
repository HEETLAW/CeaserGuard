import os
import hashlib

class CaesarCipher:
    def __init__(self, shift=3):
        self.shift = shift

    def encrypt(self, plaintext):
        return ''.join([self._shift_char(char, self.shift) for char in plaintext])

    def decrypt(self, ciphertext):
        return ''.join([self._shift_char(char, -self.shift) for char in ciphertext])

    def _shift_char(self, char, shift):
        if char.isalpha():
            shift = shift % 26
            code = ord(char) + shift
            if char.islower():
                if code > ord('z'):
                    code -= 26
                elif code < ord('a'):
                    code += 26
            elif char.isupper():
                if code > ord('Z'):
                    code -= 26
                elif code < ord('A'):
                    code += 26
            return chr(code)
        return char

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

    def verify_integrity(self, filename, original_hash):
        with open(filename, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        return file_hash == original_hash

    def calculate_hash(self, filename):
        with open(filename, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

def main():
    cipher = CaesarCipher()

    while True:
        choice = input("Would you like to (e)encrypt / (d)decrypt / (ef)encrypt file / (df)decrypt file / (v)verify integrity / (q)quit? ").lower()
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice == 'e':
            plaintext = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            cipher.shift = shift
            print("Encrypted message:", cipher.encrypt(plaintext))
        elif choice == 'd':
            ciphertext = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            cipher.shift = shift
            print("Decrypted message:", cipher.decrypt(ciphertext))
        elif choice == 'ef':
            input_file = input("Enter the input file path: ")
            output_file = input("Enter the output file path: ")
            cipher.encrypt_file(input_file, output_file)
        elif choice == 'df':
            input_file = input("Enter the input file path: ")
            output_file = input("Enter the output file path: ")
            cipher.decrypt_file(input_file, output_file)
        elif choice == 'v':
            filename = input("Enter the file path to verify integrity: ")
            original_hash = input("Enter the original hash value: ")
            if cipher.verify_integrity(filename, original_hash):
                print("Integrity verified: The file has not been altered.")
            else:
                print("Integrity verification failed: The file has been altered.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
