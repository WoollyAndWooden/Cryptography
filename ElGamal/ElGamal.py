import os
import random
import sys
from math import pow

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[1]

#Greater Common Division
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

#Power in modulo
def power(a, b, c):
    x = 1
    y = a
 
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
 
    return x % c

#Key generation functions
def createPrivate(p, g, mode = "r"):
    private = random.getrandbits(256) % p
    while gcd(private, p)!= 1:
        private = random.getrandbits(256) % p
    if(mode == "w"):
        print("Generate private key")
        open("private.txt", "w").write(str(p)+"\n"+str(g)+"\n"+str(private))
    return int(private)

def createPublic(p, g, b):
    public = power(p, g, b)
    open("public.txt", "w").write(str(p)+"\n"+str(g)+"\n"+str(public))
    return int(public)


#Encryption functions
def encrypt(plain, p, g, public):
    if plain >= p:
        return 0
    private = createPrivate(p, g)
    print(private)
    en_g = power(g, private, p)
    en_b = power(public, private, p)
    #print(en_b)
    plain = (en_b * plain)
    open("crypto.txt", "w").write(str(en_g)+"\n"+str(plain))
    
    return 1


#Decryption functions
def decrypt(encrypted, p, g, private):
    gk = int(encrypted[0])
    B = power(gk, private, p)
    print(private) 
    decrypted = (encrypted[1]/B)
    open("decrypted.txt", "w").write(str(decrypted))
    return 0



def main():
    if args == '-k':
        file = open(os.path.join(ROOT_DIR, "elgamal.txt"), "r")
        p = int(file.readline())
        g = int(file.readline())
        private = createPrivate(p, g, "w")
        public = createPublic(p, g, private)
        print(private)
        file.close()
    if args == "-e":
        file = open("public.txt", "r")
        p = int(file.readline())
        g = int(file.readline())
        public = int(file.readline())
        file.close()
        plain = int(open("plain.txt", "r").readline())
        if not encrypt(plain, p, g, public):
            print("Za duże m")
    if args == "-d":
        file = open("private.txt", "r")
        p = int(file.readline())
        g = int(file.readline())
        private = int(file.readline())
        file.close()
        encrypted = []
        file = open("crypto.txt", "r")
        encrypted.append(int(file.readline()))
        encrypted.append(int(file.readline()))
        file.close()
        decrypt(encrypted, p, g, private)
        

main()