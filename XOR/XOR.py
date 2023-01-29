import os
import sys


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[1]
legalchars = 'abcdefghijklmnopqrstuvwxyz '


def main():
    if(args == "-p"):
        file = open(os.path.join(ROOT_DIR, "origin.txt"), "r")
        plain = ''
        for line in file.readlines():
            plain = plain  + line


        

        plain = plain.replace('\n', '')
        plain = plain.replace('.', '')
        plain = plain.replace(',', '')
        remain = len(plain) % 64
        plain = plain.lower()
        for i in range(remain):
            plain = plain + " "
        file.close()
        print(len(plain))
        open("plain.txt", "w").write("")
        file = open(os.path.join(ROOT_DIR, "plain.txt"), "a")

        for i in range(0, int(len(plain) / 64)):
            file.write(plain[i*64:64*(i+1)]+"\n") 

        file.close()

    if(args == "-e"):
        key = open(os.path.join(ROOT_DIR, "key.txt"), "r").readline()
        open("crypto.txt", "w").write("")
        crypto = open(os.path.join(ROOT_DIR, "crypto.txt"), "a")
        plain = open(os.path.join(ROOT_DIR, "plain.txt"), "r")

        for line in plain:
            line = line.replace('\n', '')
            
            for i in range(0, 64):
                if ''.join(chr(ord(key[i]) ^ ord(line[i]))) == "\n":
                    print("Fuck "+ key[i] + line[i])
                crypto.write(''.join(chr(ord(key[i]) ^ ord(line[i]))))

        crypto.close()
        plain.close()

    if(args == "-k"):
        crypto = open(os.path.join(ROOT_DIR, "crypto.txt"), "r")
        d = []
        j = 0
        for line in crypto:
            for i in line:
                d.append(i)
        key = []
        print(len(d))
        



main()