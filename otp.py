#!/usr/bin/env python3
import os, sys


def file_read_data(filename):
    file_handle = open(filename, 'rb')
    data = file_handle.read()
    file_handle.close()
    return data
    
def file_write_data(filename, data):
    file_handle = open(filename, 'wb+')
    file_handle.write(data)
    file_handle.close()
    
def bn(b):
    # b - bytes to encode as integer
    i = 0
    for byte in b:
        i = (i << 8) + byte
    return i

def nb(i, length):
    # i - integer to encode as bytes
    # length - specifies in how many bytes the number should be encoded
    b = bytearray()
    for n in range(0, length)[::-1]:
        b.append((i >> (n << 3) & 0xff))
    return b

def encrypt(pfile, kfile, cfile):
    plain_text = file_read_data(pfile)
    plain_text_int = bn(plain_text)
    plain_text_bytes_len = len(plain_text)
    # key creation
    key = os.urandom(plain_text_bytes_len)
    key_int = bn(key)
    # encryption
    cipher_text_int = plain_text_int ^ key_int
    cipher_text_bytes_len = plain_text_bytes_len
    cipher_text = nb(cipher_text_int, cipher_text_bytes_len)
    # create ciphertext and key files
    file_write_data(cfile, cipher_text)
    file_write_data(kfile, key)
  
def decrypt(cfile, kfile, pfile):
    cipher_text = file_read_data(cfile)
    cipher_text_int = bn(cipher_text)
    key = file_read_data(kfile)
    key_int = bn(key)
    # decrypt
    plain_text_int = cipher_text_int ^ key_int
    plain_text_bytes_len = len(cipher_text)
    plain_text = nb(plain_text_int, plain_text_bytes_len)
    # create plaintext file
    file_write_data(pfile, plain_text)

def usage():
    print("Usage:")
    print("encrypt <plaintext file> <output key file> <ciphertext output file>")
    print("decrypt <ciphertext file> <key file> <plaintext output file>")
    sys.exit(1)



if len(sys.argv) != 5:
    usage()
elif sys.argv[1] == 'encrypt':
    encrypt(sys.argv[2], sys.argv[3], sys.argv[4])
elif sys.argv[1] == 'decrypt':
    decrypt(sys.argv[2], sys.argv[3], sys.argv[4])
else:
    usage()
