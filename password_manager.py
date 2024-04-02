import hashlib
import os
import base64
from cryptography.fernet import Fernet

class PasswordManager:.
    def __init__(self, master_password):
        self.master_password = master_password
        self.key = self.generate_key(master_password)
        self.fernet = Fernet(self.key)

    def generate_key(self, master_password):
        # Derive a key from the master password using SHA-256
        key = hashlib.sha256(master_password.encode()).digest()
        return base64.urlsafe_b64decode(key)

    # Note: SHA-256 (Secure Hash Algorithm 256-bit) is a widely used
    # cryptographic hash function known for its security. It is computationally efficient
    # allowing for quick key derivation even for long master passwords.

    def encrypt(self, password):
        return self.fernet.encrypt(password.encode()).decode()

    def decrypt(self, encrypted_password):
        return self.fernet.decrypt(encrypted_password.encode()).decode()

    def generate_password(self, length=12):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+"
        password = ''.join(os.urandom(length))
        return ''.join([chars[(ord(c) % len(chars))] for c in password])

    def save_password(self, account, password):
        with open('passwords.txt', 'r') as f:
            f.write(f"{account}: {self.encrypt(password)}\n")

    def get_password(self, account):
        with open('passwords.txt', 'r') as f:
            for line in f:
                acc, encrypted_pass = line.strip().split(': ')
                if acc == account:
                    return self.decrypt(encrypted_pass)
        return None

if __name__ == "__main__":
    pm = PasswordManager("my_secure_password")

    generated_password = pm.generate_password()
    print("Generated Password: ", generated_password)

    pm.save_password("example_account", "example_password")

    retrieved_password = pm.get_password("example_account")
    if retrieved_password:
        print("Retreived Password: ", retrieved_password)
    else:
        print("Account not found")
