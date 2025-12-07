# Image-Steganography-Encryption

## Overview

**Image-Steganography-Encryption** is a Python-based project that allows you to **hide text messages inside images** using pixel-level manipulation.  
The project supports **case-sensitive letters, numbers, spaces, and punctuation** and uses a combination of **Caesar cipher for letters**, **numeric mapping for digits**, and **custom mapping for punctuation**.  

This repository contains both **encryption** and **decryption** modules, allowing you to securely hide and reveal messages in images.  

---

## Features

- Hide text in images by modifying **only one RGB channel per character**.
- Supports:
  - Uppercase and lowercase letters (A-Z, a-z)
  - Numbers (0-9)
  - Spaces and punctuation (`string.punctuation`)
- Case-sensitive message preservation.
- Caesar cipher shift for letters (shift = 3)
- Overflow-safe pixel operations using NumPy.
- PNG images are cleaned to avoid **iCCP / sRGB warnings**.
- Fully tested in Windows with Python 3.11 and virtual environments.
- Easy to extend for larger messages or additional file formats.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Mani-Babapour/Image-Steganography-Encryption.git
cd Image-Steganography-Encryption
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Encrypt a message
```python
from Encryption import encrypt_text_to_image

image_path = "images.png"
encrypted_image_path = "images_encrypted.png"
message = "Hello! I am Mani:)"

encrypt_text_to_image(image_path, message, encrypted_image_path)
```

### Decrypt a message
```python
from Decryption import decrypt_image

hidden_message = decrypt_image(image_path, encrypted_image_path, len(message))
print("Hidden message:", hidden_message)
```

## File Structure

```bash
Image-Steganography-Encryption/
│
├── Encryption.py         # Encryption module
├── Decryption.py         # Decryption module
├── main.py               # Example usage script
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── images/               # Optional: sample images
```