# A Function That Reads an Image as Binary Data and Returns a String of bits
def read_image_bit_string(path):
    with open(path, 'rb') as image:
        bit_string = ""
        
        # read first byte in the image
        byte = image.read(1)
        while (len(byte) > 0):
            # Convert byte into ASCII value
            byte = ord(byte)
            
            # Convert ASCII value into binary
            bits = bin(byte)[2:].rjust(8, '0')
            bit_string += bits
        # read next byte in the image
            byte = image.read(1)
    return bit_string


# A Function That Writes a String of Bits to an Image File
def write_image(bit_string, path):
    with open(path, 'wb') as image:
        
        # write the bits to the image file
        for i in range(0, len(bit_string), 8):
            # get the next byte
            byte = bit_string[i:i + 8]
            
            # convert the byte into an integer
            image.write(bytes([int(byte, 2)]))


# A Function That Reads a Dictionary from a File 
def write_dictionary_file(dictionary, path):
    with open(path, 'w') as f:
        for key, value in dictionary.items():
            f.write('%s:%s\n' % (key, value))
