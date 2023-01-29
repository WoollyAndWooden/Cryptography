import os
import sys


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    longer = "hash"
    shorter = "hash2"
    ext = ".txt"
    ver = ["md5", "1", "224", "256", "384", "512"]
    open(os.path.join(ROOT_DIR, "diff.txt"), "w").write('')
    file = open(os.path.join(ROOT_DIR, "diff.txt"), "a")

    for i in ver:
        hash1 = longer + i + ext
        hash2 = shorter + i + ext

        hash1 = open(os.path.join(ROOT_DIR, hash1), "r").read()
        hash2 = open(os.path.join(ROOT_DIR, hash2), "r").read()

        hash1 = int(hash1[0:len(hash1)-3], 16)
        hash2 = int(hash2[0:len(hash2)-3], 16)

        result = hash1^hash2
        result = bin(result)[2:]

        n = 0
        for j in result:
            if j == "1":
                n += 1

        file.writelines("hash-.pdf personal_.txt by sha" + i + "\n")
        file.writelines("hash-.pdf personal.txt by sha" + i + "\n")
        file.writelines(hex(hash1) + "\n")
        file.writelines(hex(hash2) + "\n")

        file.write("Bit differnce: ")
        file.write(str(n) + " out of " + str(len(result)) + ", " + str(int(n / len(result) * 100)) + "%\n\n\n")
   
    file.close()


main()


