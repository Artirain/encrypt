#шифрование файлов с текстом семитричным алгоритмов блочного шифрования AES
import pyAesCrypt

password = input('Введите пароль для шифрования файла: ') #запрашивает у юзера пароль

# ecrypt
pyAesCrypt.encryptFile('encrypt/data.txt','encrypt/data.txt.aes', password) #файл который хотим зашифровать, имя зашифрованного файла на выходе, указываем пароль

#decrypt

# pyAesCrypt.decryptFile('encrypt/data.txt.aes', 'encrypt/dataout.txt', password)