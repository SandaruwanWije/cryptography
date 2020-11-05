import sys
def help():
    print("python3 ceasar_cipher.py -e -m \"Enter Mesage Here\" -k 3")
    print("python3 ceasar_cipher.py -d -c \"ciper text\" -k 3")
    print("-k should me 0 26")
def encrypt(msg, key):
    cipher = ""
    for letter in msg:
        int_ltr = ord(letter) 
        if int_ltr > 64 and int_ltr < 91:
            new_int_ltr = int_ltr + key
            if new_int_ltr > 90:
               new_int_ltr = 64 + (key - (90 - int_ltr))
            cipher = cipher + chr(new_int_ltr)
        elif int_ltr > 96 and int_ltr < 123:
            new_int_ltr = int_ltr + key
            if new_int_ltr > 122:
               new_int_ltr = 96 + (key - (122 - int_ltr))
            cipher = cipher + chr(new_int_ltr)
        else:
            cipher = cipher + letter
    return cipher

def decrypt(cipher, key):
    msg = ""
    for letter in cipher:
        int_ltr = ord(letter) 
        if int_ltr > 64 and int_ltr < 91:
            new_int_ltr = int_ltr - key
            if new_int_ltr < 65:
               new_int_ltr = 91 - (65 - new_int_ltr)
            msg = msg + chr(new_int_ltr)
        elif int_ltr > 96 and int_ltr < 123:
            new_int_ltr = int_ltr - key
            if new_int_ltr < 97:
               new_int_ltr = 123 - (97 - new_int_ltr)
            msg = msg + chr(new_int_ltr)
        else:
            msg = msg + letter
    return msg

if __name__ == "__main__":
    try:
        argv = sys.argv
        if "-h" in argv:
            help()
        elif "-e" in argv:
            msg_index = argv.index("-m") + 1
            msg = argv[msg_index].replace("\"", "")
            key_index = argv.index("-k") + 1
            key = argv[key_index]
            cipher = encrypt(msg, int(key))
            print(cipher)
        else:
            cipher_index = argv.index("-c") + 1
            cipher = argv[cipher_index].replace("\"", "")
            key_index = argv.index("-k") + 1
            key = argv[key_index]
            msg = decrypt(cipher, int(key))
            print(msg)

    except Exception as e:
        print("Something went wrong. python3 ceasar_cipher.py -h for help")
        print("\nHere the errand log:\n")
        print(e)
