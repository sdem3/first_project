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