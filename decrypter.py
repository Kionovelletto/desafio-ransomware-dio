import os
import pyaes

file_name = "file.txt.encrypted"
file = open(file_name, "rb")
file_data = file.read()
file.close()

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

os.remove(file_name)

new_file = "file.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()


info_file = file_name + ".info"
with open(info_file, 'w') as f:
    if decrypt_data:
        f.write("Arquivo descriptografado com sucesso!")
    else:
        f.write("Erro ao descriptografar o arquivo.")