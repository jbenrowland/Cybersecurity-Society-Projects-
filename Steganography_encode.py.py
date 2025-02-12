from PIL import Image
import numpy as np

def encode_message(image_path, text_file_path, output_image_path):
    # Open the image and convert it to RGB mode
    image = Image.open(image_path).convert("RGB")
    pixels = np.array(image)

    # Read the message from the text file
    with open(text_file_path, "r") as file:
        message = file.read()

    # Append a delimiter to mark the end of the message
    message += "%%EOF%%"

    # Convert the message into a binary string
    binary_message = ''.join([format(ord(char), '08b') for char in message])

    # Flatten the image pixel array
    flat_pixels = pixels.flatten()

    if len(binary_message) > len(flat_pixels):
        raise ValueError("Message is too large to encode in this image.")

    # Encode the binary message into the least significant bits of the pixel array
    for i in range(len(binary_message)):
        flat_pixels[i] = (flat_pixels[i] & ~1) | int(binary_message[i])

    # Reshape the modified pixel array back to the original image shape
    encoded_pixels = flat_pixels.reshape(pixels.shape)

    # Create and save the encoded image
    encoded_image = Image.fromarray(encoded_pixels.astype('uint8'), mode="RGB")
    encoded_image.save(output_image_path)
    print(f"Message successfully encoded into {output_image_path}")

# Example Usage
image_path = "input_image.png"  # Input image file (PNG or JPEG)
text_file_path = "message.txt"  # Text file containing the message
output_image_path = "encoded_image.png"  # Output image with hidden message

encode_message(image_path, text_file_path, output_image_path)
