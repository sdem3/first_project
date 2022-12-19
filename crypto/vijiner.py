import cesar as cesar
class Vijiner(cesar.Cesar):
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