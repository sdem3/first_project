import stega as stega
import cesar as cesar
import vijiner as vij

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
            cipher = vij.Vijiner(key, filename, out)
            cipher.encrypt()
        if command == "vjnr decode":
            filename = input("print filename to decode")
            out = input("outname file")
            key = input("print key")
            cipher = vij.Vijiner(key, filename, out)
            cipher.decrypt()
        if command == "cesar encode":
            filename = input("print filename to encode")
            out = input("print outname")
            cipher = cesar.Cesar()
            cipher.encrypt(key, filename, out)
        if command == "cesar decode":
            filename = input("print filename to encode")
            encode = input("print encode file name")
            key = input("print key")
            cipher = cesar.Cesar()
            cipher.decrypt(key, filename, encode)
        if command == "stega encode":
            filename = input("print name textfile to hide")
            img = input("print image name")
            cipher = stega.Stega()
            cipher.encrypt(filename, img)
        if command == "stega decode":
            len = int(input('print len of text'))
            img = input("print image name")
            #out_name = input("print name of out textfile")
            cipher = stega.Stega()
            cipher.decrypt(len, img)
        if command == 'man':
            print('''Available comands: 1)"vjnr encode"
                                        2)"vjnr decode"
                                        3)"cesar encode"
                                        4)"cesar decode"
                                        5)"stega encode"
                                        6)"stega decode"
                        ''')