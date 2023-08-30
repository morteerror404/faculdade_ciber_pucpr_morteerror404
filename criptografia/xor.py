from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
chave = b'12345'
algorithm = algorithms.ARC4(chave)
cipher = Cipher(algorithm, mode=None)
encryptor = cipher.encryptor()
ciphertext = encryptor.update(b'Special charactors are not allowed')
print(ciphertext)
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext)
print(plaintext)
