from Encryption import encrypt_text_to_image
from Decryption import decrypt_image

if __name__ == "__main__":
    image_path = r"C:\Users\ASuS\Desktop\images.png"
    encrypted_image_path = r"C:\Users\ASuS\Desktop\images_encrypted.png"

    message = "Hello! I am Mani:)"

    encrypt_text_to_image(image_path, message, encrypted_image_path)

    decrypted = decrypt_image(image_path, encrypted_image_path, len(message))
    print("Hidden message:", decrypted)
