import sys
import os
class Stega:
    def encrypt(filename, message, img):
        text = open(message, 'r')
        image = open(img, "rb")
        encode_bmp = open("encode.bmp", "wb")

        image_size = os.stat(img).st_size
        encode_bmp.write(image.read(54))
        bit_mask = 0b11000000
        encoding_mask = 0b11111100

        while True:
            c=text.read(1)
            if c=='':
                break
            byte_c = ord(c)
            bit_mask = 0b11000000
            for i in range(4):
                byte = int.from_bytes(image.read(1), sys.byteorder)

                bit_2 = (bit_mask & byte_c) >> (6-2*i)

                byte = byte & encoding_mask

                byte = byte | bit_2

                encode_bmp.write(byte.to_bytes(1,sys.byteorder))
                bit_mask = bit_mask >> 2
        encode_bmp.write(image.read())
        text.close()
        image.close()
        encode_bmp.close()


    def decrypt(self, len_to_read, t):
        text = open('encode_stega.txt', 'w')
        encode_bmp = open(t, "rb")
        encode_bmp.read(54)
        bitmask = 0b00000011
        for i in range(len_to_read):
            word_byte = 0
            for j in range(4):
                byte = int.from_bytes(encode_bmp.read(1),sys.byteorder)
                byte_c = (bitmask & byte) << (6-2*j)
                word_byte+=byte_c
            text.write(chr(word_byte))
        text.close()
        encode_bmp.close()