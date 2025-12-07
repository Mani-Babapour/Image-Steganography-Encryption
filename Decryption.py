import cv2
import string
import os

# Disable libpng warnings
os.environ["OPENCV_IO_ENABLE_PNG_WARNING"] = "0"

punctuations = string.punctuation + " "


# ---------------- LETTER MAPPINGS ---------------- #
def caesar_decrypt(c):
    if c.islower():
        return chr((ord(c) - 97 - 3) % 26 + 97)
    if c.isupper():
        return chr((ord(c) - 65 - 3) % 26 + 65)
    return c


def code_to_letter(code):
    if 1 <= code <= 26:
        return chr(code + 96)
    else:
        return chr(code + 38)


# ---------------- MAIN DECRYPT FUNCTION ---------------- #
def decrypt_image(original_path, encrypted_path, msg_length):
    # Clean PNGs before comparison
    clean_orig = "_orig_clean.png"
    clean_enc = "_enc_clean.png"

    img_o = cv2.imread(original_path)
    img_e = cv2.imread(encrypted_path)

    cv2.imwrite(clean_orig, img_o)
    cv2.imwrite(clean_enc, img_e)

    orig = cv2.imread(clean_orig)
    enc = cv2.imread(clean_enc)

    os.remove(clean_orig)
    os.remove(clean_enc)

    flat_orig = orig.reshape(-1, 3)
    flat_enc = enc.reshape(-1, 3)

    result = ""

    for i in range(msg_length):
        b = (int(flat_enc[i][0]) - int(flat_orig[i][0])) % 256
        g = (int(flat_enc[i][1]) - int(flat_orig[i][1])) % 256
        r = (int(flat_enc[i][2]) - int(flat_orig[i][2])) % 256


        if 1 <= b <= 52:     # Letter
            shifted = code_to_letter(b)
            original = caesar_decrypt(shifted)
            result += original

        elif 50 <= g <= 59:  # Number
            result += str(g - 50)

        elif r >= 100:       # Punctuation
            result += punctuations[r - 100]

        else:
            result += "?"

    return result
