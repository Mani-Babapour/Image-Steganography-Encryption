from Encryption import encrypt_text_to_image
from Decryption import decrypt_image

if __name__ == "__main__":
    # Image files (relative paths)
    image_path = "image.png"
    encrypted_image_path = "image_encrypted.png"

    # General message (edit this variable for different messages)
    message = "Your secret message here"

    # Encrypt the message into the image
    encrypt_text_to_image(image_path, message, encrypted_image_path)

    # Decrypt the message from the image
    decrypted = decrypt_image(image_path, encrypted_image_path, len(message))
    print("Hidden message:", decrypted)
