import file_handling
import huffman_coding
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

file_directory_paths = {
    'image': './images/Image',
    'decompressed_directory': './decompressed_images/',
    'compressed_directory': './compressed_images/',
    'huffman_codes_directory': './huffman_codes/'
}

# Get the image number from user input
image_number = int(input("Enter the image number (0 - 93): "))
# Construct the path to the image file
image_path = file_directory_paths['image'] + " " + str(image_number) + '.jpg'

# Display the original image
original_image = mpimg.imread(image_path)
plt.imshow(original_image)
plt.title(f"Original Image {image_number}")
plt.axis('off')
plt.show()

# Read the image bit string from the file
image_bit_string = file_handling.read_image_bit_string(image_path)

# Compress the image bit string using Huffman coding
compressed_image_bit_string = huffman_coding.compress(image_bit_string, image_number, file_directory_paths)

# Construct the path for the compressed image file
compressed_path = file_directory_paths['compressed_directory'] + 'compressed_image_' + str(image_number) + '.bin'

# Ensure the compressed images directory exists
if not os.path.exists(file_directory_paths['compressed_directory']):
    os.makedirs(file_directory_paths['compressed_directory'])

# Write the compressed image bit string to the file
try:
    file_handling.write_image(compressed_image_bit_string, compressed_path)
except Exception as e:
    # Print an error message if writing fails
    print(f"Error while writing compressed image: {e}")


decompressed_image_bit_string = huffman_coding.decompress(compressed_image_bit_string)

decompressed_path = file_directory_paths['decompressed_directory'] + 'decompressed_image_' + str(image_number) + '.jpg'

# Ensure the decompressed images directory exists
if not os.path.exists(file_directory_paths['decompressed_directory']):
    os.makedirs(file_directory_paths['decompressed_directory'])

try:
    file_handling.write_image(decompressed_image_bit_string, decompressed_path)
except Exception as e:
    print(f"Error while writing decompressed image: {e}")


print("Compression Ratio (CR):", len(image_bit_string) / len(compressed_image_bit_string))
print("Original Image Size:", os.path.getsize(image_path), "bytes")
print("Compressed Image Size:", os.path.getsize(compressed_path), "bytes")
print("Decompressed Image Size:", os.path.getsize(decompressed_path), "bytes")
print("Redundancy:", 1 - (1 / (len(image_bit_string) / len(compressed_image_bit_string))))

# Display the decompressed image
decompressed_image = mpimg.imread(decompressed_path)
plt.imshow(decompressed_image)
plt.title(f"Decompressed Image {image_number}")
plt.axis('off')
plt.show()
