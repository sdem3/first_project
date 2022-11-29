import os
import sys
import collections
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
class Cesar:

    frequency = {('a', 'A'): 8.2, ('b', 'B'): 1.5, ('c', 'C'): 2.8, ('d', 'D'): 4.3,
                 ('e', 'E'): 13, ('f', 'F'): 2.2, ('g', 'G'): 2, ('h', 'H'): 6.1,
                 ('i', 'I'): 7, ('j', 'J'): 0.15, ('k', 'K'): 0.77, ('l', 'L'): 4,
                 ('m', 'M'): 2.4, ('n', 'N'): 6.7, ('o', 'O'): 7.5, ('p', 'P'): 1.9,
                 ('q', 'Q'): 0.095, ('r', 'R'): 6, ('s', 'S'): 6.3, ('t', 'T'): 9.1,
                 ('u', 'U'): 2.8, ('v', 'V'): 0.98, ('w', 'W'): 2.4, ('x', 'X'): 0.15,
                 ('y', 'Y'): 2, ('z', 'Z'): 0.074}
    lower_letter_index = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    upper_letter_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    def idx(self, char):
        if char.isalpha():
            if char.isupper():
                return self.upper_letter_index.get(char)
            else:
                return self.lower_letter_index.get(char)
        else:
            return None
    def chr(self, idx, upper = False):
        if upper:
            for letter, i in self.upper_letter_index.items():
                if i==idx:
                    return letter
        else:
            for letter, i in self.lower_letter_index.items():
                if i==idx:
                    return letter
    def encrypt(self, key, t, e):
        key = self.idx(key)
        text = open(t, "r")
        encode_text = open(e, "w")
        while True:
            c = text.read(1)
            if c=='':
                break
            if (self.idx(c) != None):
                c = self.chr((self.idx(c)+key)%26)

            encode_text.write(c)
        encode_text.close()
        text.close()

    '''def decrypt(self, key):
        encode_text = open("cesar.txt", "r")
        decode_text = open("ans.txt", "w")
        while True:
            c = encode_text.read(1)
            if c=='':
                break
            if (self.idx(c)!=None):
                c = self.chr((self.idx(c)+26-key)%26)
            decode_text.write(c)
        decode_text.close()
        encode_text.close()'''
    def build_frequency_table(self, filename):
        text = open(filename, "r")
        s = text.read()
        letters =[]
        for c in s:
            if c.isalpha():
                letters.append(c)
        table = collections.Counter(letters)
        return table
    def decrypt(self, e, d):
        encode_text = open(e, "r")
        decode_text = open(d, "w")
        table = self.build_frequency_table(e)
        max_count = max(list(table.values()))
        l = ''
        for letter, count in table.items():
            if count==max_count:
                l = letter

        key = (self.idx(l) - self.idx('e') + 26) % 26

        while True:
            c = encode_text.read(1)
            if c == '':
                break
            if (self.idx(c) != None):
                c = self.chr((self.idx(c) + 26 - key) % 26)
            decode_text.write(c)
        decode_text.close()
        encode_text.close()
class Vijiner(Cesar):
    def encrypt(self, key_word, t, e ):
        keys = [self.idx(key_word[i]) for i in range(len(key_word))]
        text = open(t, 'r')
        encode = open(e, 'w')
        i = 0
        while True:
            c = text.read(1)
            if c=='':
                break
            if (self.idx(c)!=None) :
                key = keys[i%len(key_word)]
                i+=1
                c=self.chr((self.idx(c)+key)%26)

            encode.write(c)
        encode.close()
        text.close()
    def decrypt(self, key_word, e, d):
        keys = [self.idx(key_word[i]) for i in range(len(key_word))]
        encode = open(e, "r")
        decode = open(d, 'w')
        i = 0
        while True:
            c = encode.read(1)
            if c=='':
                break
            if (self.idx(c)!=None):
                key = keys[i % len(key_word)]
                i += 1
                c = self.chr((self.idx(c) - key +26) % 26)
            decode.write(c)
        encode.close()
        decode.close()

#cipher = Cesar()
#cipher.encrypt('B')
#cipher.decrypt()
#cipher = Vijiner()
#cipher.encrypt('alice')
#cipher.decrypt('alice')
def start():
    print("print command: ")
    print("print man - if you need a manual")
    while True:
        command = input('...')
        if command == 'exit':
            print("bye")
            break
        if command == "vjnr encode":
            filename = input("print filename to encode")
            out = input("outname file")
            key = input("print key")
            cipher = Vijiner(key, filename, out)
            cipher.encrypt()
        if command == "vjnr decode":
            filename = input("print filename to decode")
            out = input("outname file")
            key = input("print key")
            cipher = Vijiner(key, filename, out)
            cipher.decrypt()
        if command == "cesar encode":
            filename = input("print filename to encode")
            out = input("print outname")
            cipher = Cesar()
            cipher.encrypt(key, filename, out)
        if command == "cesar decode":
            filename = input("print filename to encode")
            encode = input("print encode file name")
            key = input("print key")
            cipher = Cesar()
            cipher.decrypt(key, filename, encode)
        if command == "stega encode":
            filename = input("print name textfile to hide")
            img = input("print image name")
            cipher = Stega()
            cipher.encrypt(filename, img)
        if command == "stega decode":
            len = int(input('print len of text'))
            img = input("print image name")
            #out_name = input("print name of out textfile")
            cipher = Stega()
            cipher.decrypt(len, img)
if __name__ == "__main__":
    start()