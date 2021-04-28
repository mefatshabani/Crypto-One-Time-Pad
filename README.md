# Crypto-One-Time-Pad
Implementation of the one-time pad cryptosystem

Even considering the lose of zero bytes when convert bytes to integer, 
as far as the key length is the same as the encrypted message, we will have 
a one-to-one mapping from messages to ciphertexts not repeating any pair. 
So, we will have perfect secrecy.

However, the situation of losing zero bytes will affect the probability 
of using the same key even for diffent generated random bytes; for example, 
'\x00\x61', '\x61', '\x00\x00\x61' all translate to the same int key.
Using the key more than once makes it vulnerable.

# Testing the code 

$ chmod +x test_otp.sh <br>
$ chmod +x otp.py <br>
$ sed -i 's/\r//g' test_otp.sh <br>
$ sed -i 's/\r//g' otp.py <br>
$ ./test_otp.sh <br>

# sed -i 's/\r//g' Explenation 
Depending the OS where you are modifying the, characters (like \r) could be added to 
the code, breaking functionality. In that case, we would need first to run: sed -i 's/\r//g'
