import cv2
import string
import os
import numpy as np

# Disable libpng warnings
os.environ["OPENCV_IO_ENABLE_PNG_WARNING"] = "0"

punctuations = string.punctuation + " "
letters = string.ascii_letters  # a-z + A-Z


# ---------------- LETTER MAPPINGS ---------------- #
def caesar_encrypt(c):
    if c.islower():
        return chr((ord(c) - 97 + 3) % 26 + 97)
    if c.isupper():
        return chr((ord(c) - 65 + 3) % 26 + 65)
    return c


def letter_to_code(c):
    if c.islower():
        return ord(c) - 96   # a=1..z=26
    else:
        return ord(c) - 38   # A=27..Z=52


# ---------------- CHARACTER CLASSIFICATION ---------------- #
def encrypt_map(char):
    """Returns (channel, value_to_add)"""
    if char in letters:
        shifted = caesar_encrypt(char)
        return "B", letter_to_code(shifted)

    elif char.isdigit():
        return "G", 50 + int(char)  # 50–59

    elif char in punctuations:
        return "R", 100 + punctuations.index(char)

    else:
        raise ValueError(f"Unsupported character: {char}")


# ---------------- PNG CLEANER ---------------- #
def clean_png(path_in, path_out):
    """Re-save PNG to remove bad ICC/sRGB profiles."""
    img = cv2.imread(path_in, cv2.IMREAD_UNCHANGED)
    cv2.imwrite(path_out, img)


# ---------------- ENCRYPTION FUNCTION ---------------- #
def encrypt_text_to_image(image_path, text, output_path):
    # Clean PNG metadata first (fixes warnings & corruption issues)
    clean_png(image_path, "_clean_temp.png")
    img = cv2.imread("_clean_temp.png")

    if img is None:
        raise ValueError("Failed to load image. Use PNG only!")

    h, w, _ = img.shape
    flat = img.reshape(-1, 3)

    if len(text) > len(flat):
        raise ValueError("Message too long for this image.")

    # Apply encoding
    for i, ch in enumerate(text):
        channel, value = encrypt_map(ch)

        if channel == "B":
            flat[i][0] = np.uint8((int(flat[i][0]) + value) % 256)
        elif channel == "G":
            flat[i][1] = np.uint8((int(flat[i][1]) + value) % 256)
        elif channel == "R":
            flat[i][2] = np.uint8((int(flat[i][2]) + value) % 256)


        encrypted = flat.reshape(h, w, 3)
        cv2.imwrite(output_path, encrypted)

    os.remove("_clean_temp.png")
    print(f"Message hidden in {output_path}")
