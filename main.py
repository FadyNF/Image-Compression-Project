import file_handling as fh
import huffman_coding as hf
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

file_directory_paths = {
    'image_dir': './images/',
    'decompressed_dir': './decompressed_images/',
    'compressed_dir': './compressed_images/',
    'huffman_codes_dir': './huffman_codes/'
}

files = [file for file in os.listdir(file_directory_paths['image_dir']) 
        if os.path.isfile(os.path.join(file_directory_paths['image_dir'], file))]

# Get the number of files in the directory
num_files = len(files)
while (True):
    try :
        #Get the image number from user input
        image_number = int(input(f"Enter the image number (0 - {num_files - 1}): "))

        if 0 <= image_number < num_files:
            break
        else: 
            print("Enter a valid number: ")
    except ValueError as e:
        print("Enter a valid number: ")
    


# Construct the path to the image file
image_path = file_directory_paths['image_dir']+'Image' + " " + str(image_number) + '.jpg'

# Display the original image
original_image = mpimg.imread(image_path)
plt.imshow(original_image)
plt.title(f"Original Image {image_number}")
plt.axis('off')
plt.show()

# Read the image bit string from the file
image_bit_string =fh.read_image_bit_string(image_path)

# Compress the image bit string using Huffman coding
compressed_image_bit_string = hf.compress(image_bit_string, image_number, file_directory_paths)

# Construct the path for the compressed image file
compressed_path = file_directory_paths['compressed_dir'] + 'compressed_image_' + str(image_number) + '.bin'

# Ensure the compressed images directory exists
if not os.path.exists(file_directory_paths['compressed_dir']):
    os.makedirs(file_directory_paths['compressed_dir'])

# Write the compressed image bit string to the file
try:
   fh.write_image(compressed_image_bit_string, compressed_path)
except Exception as e:
    # Print an error message if writing fails
    print(f"Error while writing compressed image: {e}")


decompressed_image_bit_string = hf.decompress(compressed_image_bit_string)

decompressed_path = file_directory_paths['decompressed_dir'] + 'decompressed_image_' + str(image_number) + '.jpg'

# Ensure the decompressed images directory exists
if not os.path.exists(file_directory_paths['decompressed_dir']):
    os.makedirs(file_directory_paths['decompressed_dir'])

try:
   fh.write_image(decompressed_image_bit_string, decompressed_path)
except Exception as e:
    print(f"Error while writing decompressed image: {e}")


original_image_size = os.path.getsize(image_path)
compressed_image_size = os.path.getsize(compressed_path)
decompressed_image_size = os.path.getsize(decompressed_path)
CR = original_image_size / compressed_image_size

print("Compression Ratio (CR):", CR, "bytes")
print("Original Image Size:", original_image_size, "bytes")
print("Compressed Image Size:", compressed_image_size, "bytes")
print("Decompressed Image Size:", decompressed_image_size, "bytes")
print("Redundancy:", 1 - (1 / CR))

# Display the decompressed image
decompressed_image = mpimg.imread(decompressed_path)
plt.imshow(decompressed_image)
plt.title(f"Decompressed Image {image_number}")
plt.axis('off')
plt.show()
