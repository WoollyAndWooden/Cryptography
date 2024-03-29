import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
args = sys.argv[1:]


#Check Affine Key
def CheckAffineKey(a, b):
    bound = 26
    check = a
    while check != bound:
        if check > bound:
            check-=bound
        else:
            bound-=check
    check2 = 0
    a_inv = -1
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            a_inv = i
            check2 = 1
    if check == check2 == 1:
        return a_inv
    return -1


#Cipher part
def Cipher(mode, key, text):
    if mode == "-c":
        key = int(key[0], 10)
        if key > 0 and key < 26:
            CaesarCipher(key, text)
        return -1
        
    elif mode == "-a":
        a = int(key[0])
        b = int(key[1])
        a_inv = CheckAffineKey(a, b)
        if a_inv < 0:
            return -1
        AffineCipher(a, b, text)

def CaesarCipher(key, text):
    text = list(text)
    for i in range(0, len(text)):
        if text[i] in ascii_lowercase:
            a = (ascii_lowercase.find(text[i]) + key) % 26
            text[i] = ascii_lowercase[a]
        if text[i] in ascii_uppercase:
            a = (ascii_uppercase.find(text[i]) + key) % 26
            text[i] = ascii_uppercase[a]

    text = ''.join(text)
    open(os.path.join(ROOT_DIR, "crypto.txt"), "w").write(text)

def AffineCipher(a, b, text):
    text = list(text)
    for i in range(0, len(text)):
        if text[i] in ascii_lowercase:
            x = (a * ascii_lowercase.find(text[i]) + b) % 26
            text[i] = ascii_lowercase[x]
        if text[i] in ascii_uppercase:
            x = (a * ascii_uppercase.find(text[i]) + b) % 26
            text[i] = ascii_uppercase[x]

    text = ''.join(text)
    open(os.path.join(ROOT_DIR, "crypto.txt"), "w").write(text)



#Decipher part
def Decipher(mode, key, text):
    if mode == "-c":
        key = int(key[0], 10)
        if key > 0 and key < 26:
            CaesarDecipher(key, text)
        return -1
        
    elif mode == "-a":
        a = int(key[0])
        b = int(key[1])
        a_inv = CheckAffineKey(a, b)
        if a_inv < 0:
            return -1
        AffineDecipher(a_inv, b, text)

def CaesarDecipher(key, text):
    text = list(text)
    for i in range(0, len(text)):
        if text[i] in ascii_lowercase:
            a = (ascii_lowercase.find(text[i]) - key) % 26
            text[i] = ascii_lowercase[a]
        if text[i] in ascii_uppercase:
            a = (ascii_uppercase.find(text[i]) - key) % 26
            text[i] = ascii_uppercase[a]

    text = ''.join(text)
    open(os.path.join(ROOT_DIR, "decrypt.txt"), "a").write(text+'\n')

def AffineDecipher(a, b, text):
    text = list(text)
    for i in range(0, len(text)):
        if text[i] in ascii_lowercase:
            x = (a * (ascii_lowercase.find(text[i]) - b)) % 26
            text[i] = ascii_lowercase[x]
        if text[i] in ascii_uppercase:
            x = (a * (ascii_uppercase.find(text[i]) - b)) % 26
            text[i] = ascii_uppercase[x]

    text = ''.join(text)
    open(os.path.join(ROOT_DIR, "decrypt.txt"), "a").write(text+'\n')


#Analysis part
def Analysis(mode, crypto, extra):
    if mode == "-c":
        CaesarAnalysis(crypto, extra)
        
    elif mode == "-a":
        AffineAnalysis(crypto, extra)

def CaesarAnalysis(crypto, extra):
    crypto = list(crypto)
    extra = list(extra)
    check = False
    key = 0
    for j in range(0, len(extra)):
        for i in range(1, 26):
            if check == True:
                i = key
            if crypto[j] in ascii_lowercase:
                a = (ascii_lowercase.find(crypto[j]) - i) % 26
                if ascii_lowercase[a] == extra[j]:
                    check = True
            if crypto[j] in ascii_uppercase:
                a = (ascii_uppercase.find(crypto[j]) - i) % 26
                if ascii_uppercase[a] == extra[j]:
                    check = True
            if check == True:
                key = i
            else:
                 key = 0
                 check = False
    if key == 0:
        print("Cannot find key")
    else:
        crypto = ''.join(crypto)
        CaesarDecipher(key, crypto)


    

def AffineAnalysis(crypto, extra):
    crypto = list(crypto)
    extra = list(extra)
    check = False
    a = 0
    b = 0
    for j in range(0, len(extra)):
        for i in range(1, 26):
            inv = CheckAffineKey(i, 1)
            for n in range(1, 26):
                if check == True:
                    i = a
                    inv = CheckAffineKey(i, n)
                    n = b
                if crypto[j] in ascii_lowercase:
                    x = (inv * (ascii_lowercase.find(crypto[j]) - n)) % 26
                    if ascii_lowercase[x] == extra[j]:
                        check = True
                if crypto[j] in ascii_uppercase:
                    x = (inv * (ascii_uppercase.find(crypto[j]) - n)) % 26
                    if ascii_uppercase[x] == extra[j]:
                        check = True
                if check == True:
                    a = i
                    b = n
                else:
                    a = 0
                    b = 0
                    check = False
    if a == 0 or b == 0:
        print("Cannot find key")
    else:
        crypto = ''.join(crypto)
        print(a, b)
        AffineDecipher(a, b, crypto)


#BruteForce part
def Brute(mode, crypto):
    if mode == "-c":
        CaesarBrute(crypto)
        
    elif mode == "-a":
        AffineBrute(crypto)

def CaesarBrute(crypto):
    for j in range(1, 26):
        print(j, " ", crypto)
        CaesarDecipher(j, crypto)

def AffineBrute(crypto):
    for i in range(1, 26):
        for j in range(1, 26):
            inv = CheckAffineKey(i, j)
            if inv != -1:
                AffineDecipher(inv, j, crypto)


def main():
    if(args[1] == "-e"):
        key = open(os.path.join(ROOT_DIR, "key.txt"), "r").readline().split()
        text = open(os.path.join(ROOT_DIR, "plain.txt"), "r").readline()
        Cipher(args[0], key, text)
    elif(args[1] == "-d"):
        key = open(os.path.join(ROOT_DIR, "key.txt"), "r").readline().split()
        text = open(os.path.join(ROOT_DIR, "crypto.txt"), "r").readline()
        Decipher(args[0], key, text)
    elif(args[1] == "-j"):
        crypto = open(os.path.join(ROOT_DIR, "crypto.txt"), "r").readline()
        extra = open(os.path.join(ROOT_DIR, "extra.txt"), "r").readline()
        Analysis(args[0], crypto, extra)
    elif(args[1] == "-k"):
        open(os.path.join(ROOT_DIR, "decrypt.txt"), "w").write('')
        crypto = open(os.path.join(ROOT_DIR, "crypto.txt"), "r").readline()
        Brute(args[0], crypto)

main()