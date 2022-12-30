import pyAesCrypt

password = input('Enter the password to encrypt the file: ')

# encrypt
pyAesCrypt.encryptFile('test.txt', 'test.txt.aes', password)

# decrypt
# pyAesCrypt.decryptFile('test.txt.aes', 'testout.txt', password)
