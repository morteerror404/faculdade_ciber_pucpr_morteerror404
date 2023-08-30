def ror(n, chave, tam):
    return (2**tam-1) & (n >> chave | n << (tam-chave))


def rol(n, chave, tam):
    return (2**tam-1) & (n << chave | n >> (tam-chave))


def cripto(mensagem, chave):
    cripto = ""
    for c in mensagem:
        codigo = ord(c) + chave
        cripto += chr(codigo)
    return cripto


plain = 'Nada de novo no front'
print(cripto(plain, 3))
cipher = cripto(plain, 4)
print(cipher)
print(cripto(cipher, -4))

# 1) Decodifique a mensagem Sfif%ij%st{t%st%kwtsy
# 2) Qual o espaço de chaves do algoritmo? Qual o tamanho da chave?
# 3) Implemente o algoritmo usando rotação de bits ao invés de caracteres

c = ord('X')
print(format(c, 'b').zfill(8))
c = ror(c, 4, 8)
print(format(c, 'b').zfill(8))
print(chr(c))
c = rol(c, 4, 8)
print(format(c, 'b').zfill(8))
print(chr(c))


# 4) Como é possível aumentar o espaço de chaves do algoritmo
