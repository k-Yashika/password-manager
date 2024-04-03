
# Password Manager

The pasdsword manager is a Python project designed to securely store and manage passwords for various accounts. It uses excryption to protect sensitive information and provides dfeatures such as password generation and storage.

## Features

- Encryption/Decryption: Utilizes the Fernet symmetric encryption algorithm for secure encryption and decryption of passwords
- Password Generation: Generates strong passwords of customizable lengths
- Secure Storage: Saves encrypted passwords in a file ('passwords.txt' in this implementation)

## Usage

1. Installation:
     - Ensure you have Python installed on your system
     - Install the required package using pip:
       `
       pip install cryptography
       `
2. Running the Application:
     - Clone the repository:
       `
       git clone https://github.com/k-Yashika/password-manager.git
       `
     - navigate to the directory:
       `
       cd password-manager
       `
     - Run the script:
       `
       python password-manager.py
       `
3. Functionality:
     - Generate a strong password: `generate_password()`
     - Save a password for an account: `save_password(account, password)`
     - Retrieve password for an account: `get_password(account)`

## Example
`
from password_manager import PasswordManager

# Initialize password manager with master password
pm = PasswordManager("my_super_secure_password")

# Generate a strong password
generated_password = pm.generate_password()
print("Generated Password:", generated_password)

# Save passwords
pm.save_password("example_account", "example_password")

# Retrieve passwords
retrieved_password = pm.get_password("example_account")
if retrieved_password:
    print("Retrieved Password:", retrieved_password)
else:
    print("Account not found")

`

## License

This project is licensed under the MIT License
