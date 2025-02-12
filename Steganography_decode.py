from PIL import Image
import numpy as np

def decode_message(encoded_image_path):
    # Open the encoded image and convert it to RGB mode
    encoded_image = Image.open(encoded_image_path).convert("RGB")
    pixels = np.array(encoded_image).flatten()

    # Extract the least significant bits to reconstruct the binary message
    binary_message = ''.join([str(pixel & 1) for pixel in pixels])

    # Convert the binary message back to text
    chars = [chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8)]
    message = ''.join(chars)

    # Look for the delimiter and return the message
    delimiter_index = message.find("%%EOF%%")
    if delimiter_index != -1:
        return message[:delimiter_index]
    else:
        raise ValueError("No hidden message found.")

# Example Usage
encoded_image_path = "encoded_image.png"  # Image with the hidden message

hidden_message = decode_message(encoded_image_path)
print("Decoded message:", hidden_message)
