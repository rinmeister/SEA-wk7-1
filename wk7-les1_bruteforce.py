#!/usr/bin/env python3

'''
Een XOR met een NOT decryption brute-force voorbeeld.
Het probeert alle mogelijke numerieke sleutelwaarden die in 7 bits passen
(0-127) om een versleuteld bericht te ontsleutelen.
Probeer met dit script de sleutel te vinden die hoort bij de volgende
ciphertext: ÚÉÓÈÏØÃÙÆÏßÁ
'''

def decrypt(plaintext, key):
    d = []
    for p in plaintext:
        cipher = ~p & 0xFF
        cipher = cipher ^ key
        d.append(chr(cipher))
    decryted_message = ''.join(d)
    return decryted_message

def main():
    ciphertext = []
    boodschap = input("Geef de ciphertext: ")
    for c in boodschap:
        ciphertext.append(ord(c))
    for key in range(128):
        decrypted_message = decrypt(ciphertext, key)
        print(f"Key: {key}, Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
