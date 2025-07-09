file = 'arquivo.txt'

# para abrir

arquivo_leitura = open(file, "r") # r = read, w = write, wb = binário

# para escrever, depois de abrir com "w"

arquivo_escrita.write("texto a ser escrito")

# leitura de um arquivo - precisa fechar ele primeiro, caso já tenha sido aberto

leitura = arquivo_leitura.read()
print(leitura)
arquivo_leitura.close()




