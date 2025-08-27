# Encryption-Decryption-Utility

## Overview

The Encryption Decryption Utility is a simple yet powerful tool designed to encrypt and decrypt text using various algorithms. This utility is built to provide a secure way to handle sensitive information, ensuring that data remains confidential and protected from unauthorized access.

## Features

- Supports multiple encryption algorithms (e.g., AES, DES, RSA)
- User-friendly command-line interface
- Ability to encrypt and decrypt files as well as text
- Key generation for symmetric encryption
- Secure handling of sensitive data

## Installation

To install the Encryption Decryption Utility, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/uma497/encryption-decryption-utility.git
   ```

2. Navigate to the project directory:
   ```bash
   cd encryption-decryption-utility
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Encrypting Text

To encrypt a text string, use the following command:

```bash
python encrypt.py --text "Your text here" --key "YourEncryptionKey"
```

### Decrypting Text

To decrypt an encrypted text string, use the following command:

```bash
python decrypt.py --text "EncryptedTextHere" --key "YourEncryptionKey"
```

### Encrypting a File

To encrypt a file, use the following command:

```bash
python encrypt.py --file "path/to/your/file.txt" --key "YourEncryptionKey"
```

### Decrypting a File

To decrypt an encrypted file, use the following command:

```bash
python decrypt.py --file "path/to/your/encrypted_file.txt" --key "YourEncryptionKey"
```

## Algorithms Supported

- **AES (Advanced Encryption Standard)**
- **DES (Data Encryption Standard)**
- **RSA (Rivest-Shamir-Adleman)**

## Key Management

For symmetric encryption algorithms like AES and DES, you can generate a secure key using the following command:

```bash
python keygen.py --length 256
```

This will generate a random key of the specified length (in bits).

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Cryptography Library](https://cryptography.io/en/latest/) for providing the cryptographic algorithms.
- Open-source community for their contributions and support.

## Contact

For any inquiries or support, please contact - umatomar497@gmail.com
