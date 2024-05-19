# CeaserGuard


This advanced version of the Caesar Cipher program includes the following features:

1. **Key Management**: Provides methods to save and load encryption keys to/from a file.

2. **File Encryption/Decryption**: Supports encryption and decryption of text files.

3. **File Integrity Verification**: Implements file integrity verification using hash functions to ensure data integrity.

4. **Exception Handling**: Includes error handling for file operations and user inputs to enhance robustness.

5. **CLI Interaction**: Offers a command-line interface for users to perform encryption, decryption, file operations, and key management.

6. **Random Key Generation**: Generates a random encryption key if not provided, enhancing security.

7. **Cryptographic Library**: Utilizes the Fernet symmetric encryption algorithm from the cryptography library for secure encryption and decryption.

8. **User Input Validation**: Validates user inputs to prevent invalid operations and enhance user experience.

9. **Quit Option**: Allows users to exit the program gracefully.

10. **Documentation**: Provides descriptive comments and docstrings to improve code readability and maintainability.

This advanced version enhances the functionality and usability of the Caesar Cipher program, making it suitable for real-world encryption and decryption tasks, including file encryption and integrity verification.

# **How to Get and Use CeaserGuard**

### Step 1: Clone the Repository

1. **Open Terminal**: Open your terminal (Command Prompt, PowerShell, or any terminal you use).

2. **Clone the Repository**: Use the `git clone` command followed by the URL of your GitHub repository.

    ```sh
    git clone https://github.com/HEETLAW/CeaserGuard.git
    ```

### Step 2: Navigate to the Repository Directory

```sh
cd CeaserGuard
```

### Step 3: Ensure Required Libraries are Installed

1. **Install Requirements**:

    ```sh
    pip install -r requirements.txt
    ```

### Step 4: Run the Script

You can now run your Caesar Cipher tool. Assuming your main script is named `CeaserGuard.py`, you would run:

```sh
python CeaserGuard.py
```

### Step 5: Using the Tool

Follow the prompts provided by the script to use the various functionalities:

1. **Encryption**:
    - Select `(e)` to encrypt a message.
    - Enter the message you want to encrypt.
    - Enter the shift value (for Caesar Cipher).

2. **Decryption**:
    - Select `(d)` to decrypt a message.
    - Enter the encrypted message.
    - Enter the shift value used during encryption.

3. **Encrypt File**:
    - Select `(ef)` to encrypt a file.
    - Enter the input file path.
    - Enter the output file path.

4. **Decrypt File**:
    - Select `(df)` to decrypt a file.
    - Enter the input file path.
    - Enter the output file path.

5. **Save Key**:
    - Select `(s)` to save the current key to a file.

6. **Load Key**:
    - Select `(l)` to load a key from a file.

7. **Verify Integrity**:
    - Select `(v)` to verify the integrity of a file.
    - Enter the file path to verify integrity.

8. **Quit**:
    - Select `(q)` to quit the application.

### Example Commands

- To encrypt a message: 
    ```sh
    Would you like to (e)encrypt / (d)decrypt / (ef)encrypt file / (df)decrypt file / (s)Save key / (l)load key / (v)verify integrity / (q)quit? e
    Enter the message to encrypt: hello
    Enter the shift value: 3
    ```

- To decrypt a message:
    ```sh
    Would you like to (e)encrypt / (d)decrypt / (ef)encrypt file / (df)decrypt file / (s)Save key / (l)load key / (v)verify integrity / (q)quit? d
    Enter the message to decrypt: khoor
    Enter the shift value: 3
    ```
# **How to Get and Use Advance_CeaserGuard**

### Step 1: Clone the Repository

1. **Open Terminal**: Open your terminal (Command Prompt, PowerShell, or any terminal you use).

2. **Clone the Repository**: Use the `git clone` command followed by the URL of your GitHub repository.

    ```sh
    git clone https://github.com/HEETLAW/CeaserGuard.git
    ```

### Step 2: Navigate to the Repository Directory

```sh
cd CeaserGuard
```

### Step 3: Ensure Required Libraries are Installed

1. **Install Requirements**:

    ```sh
    pip install -r requirements.txt
    ```

### Step 4: Run the Script

You can now run your Caesar Cipher tool. Assuming your main script is named `Advance_CeaserGuard.py`, you would run:

```sh
python Advance_CeaserGuard.py
```

### Step 5: Usage Instructions

   When you run the script, you'll be prompted with several options:

   ```
   Would you like to (e)encrypt / (d)decrypt / (ef)encrypt file / (df)decrypt file / (s)Save key / (l)load key / (v)verify integrity / (q)quit?
   ```
   
   - **(e)**: Encrypt a message.
     ```sh
     Enter the message to encrypt: hello
     ```
     
   - **(d)**: Decrypt a message.
     ```sh
     Enter the message to decrypt: <encrypted_message>
     ```
     
   - **(ef)**: Encrypt a file.
     ```sh
     Enter the input file path: input.txt
     Enter the output file path: encrypted_output.txt
     ```
     
   - **(df)**: Decrypt a file.
     ```sh
     Enter the input file path: encrypted_output.txt
     Enter the output file path: decrypted_output.txt
     ```
     
   - **(s)**: Save the encryption key to a file.

   - **(l)**: Load the encryption key from a file.

   - **(v)**: Verify the integrity of a file.
     ```sh
     Enter the file path to verify integrity: input.txt
     ```

