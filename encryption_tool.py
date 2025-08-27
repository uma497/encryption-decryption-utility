from cryptography.fernet import Fernet
import os

# --------------------------
# Generate & Load Key
# --------------------------
def generate_key():
    """Generate and save a key to secret.key file"""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("✅ Key generated and saved in 'secret.key'")

def load_key():
    """Load the key from secret.key file"""
    return open("secret.key", "rb").read()

# --------------------------
# Encryption
# --------------------------
def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filename + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted)
    print(f"✅ File encrypted successfully → {filename}.enc")

# --------------------------
# Decryption
# --------------------------
def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message).decode()
    return decrypted

def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = fernet.decrypt(encrypted)

    output_file = filename.replace(".enc", ".dec")
    with open(output_file, "wb") as decrypted_file:
        decrypted_file.write(decrypted)
    print(f"✅ File decrypted successfully → {output_file}")

# --------------------------
# CLI Menu
# --------------------------
def menu():
    while True:
        print("\n--- Encryption/Decryption Utility ---")
        print("1. Generate Key")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Encrypt File")
        print("5. Decrypt File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            msg = input("Enter message to encrypt: ")
            encrypted = encrypt_message(msg)
            print("🔐 Encrypted:", encrypted.decode())
        elif choice == "3":
            encrypted_msg = input("Enter encrypted message: ")
            decrypted = decrypt_message(encrypted_msg.encode())
            print("🔓 Decrypted:", decrypted)
        elif choice == "4":
            file = input("Enter filename to encrypt: ")
            encrypt_file(file)
        elif choice == "5":
            file = input("Enter filename to decrypt (.enc): ")
            decrypt_file(file)
        elif choice == "6":
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    menu()
