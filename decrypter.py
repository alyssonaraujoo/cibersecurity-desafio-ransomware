import os
import pyaes

# Abrir o arquivo criptografado

nome_do_arquivo = 'documento.txt.ransomwareCrypt'
arquivo = open(nome_do_arquivo, 'rb')
dado_do_arquivo = arquivo.read()
arquivo.close()


# Chave de descriptografia

chave = b'chaveRansomwares'
aes = pyaes.AESModeOfOperationCTR(chave)
dado_descriptografado = aes.decrypt(dado_do_arquivo)


# Remover o arquivo criptografado

os.remove(nome_do_arquivo)


# Criar um novo arquivo descriptografado

novo_arquivo = 'documento.txt'
novo_arquivo = open(f'{novo_arquivo}','wb')
novo_arquivo.write(dado_descriptografado)
novo_arquivo.close()
