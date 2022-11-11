import os, sys


print()
## DADOS DO SISTEMA
sistema = os.environ
print("usuario:", sistema['USERNAME']) #fica tudo em um dicionario

#LIDANDO CO PASTAS
#a pasta em que eu estou
print("vc está em:",os.getcwd())

#quero ir para uma pasta diferente (mudar de caminho)
novo_caminho = r'C:\Users\xicas\Documents\Junior\pasta_teste' #o 'r' antes da string serve para ignorar comandos como \n (salto de linha)
os.chdir(novo_caminho)
print("onde estou agr:", os.getcwd())

os.rmdir("TOME") ###########ignore

##shutil #para movimentar arquivos

#criar um arquivo
os.mkdir("TOME")
#listar tudo que tem em um diretorio
print("tudo que esta nesse diretorio:", os.listdir())

#varias pastas, uma dentro da outra
novo_caminho_2 = r'C:\Users\xicas\Documents\Junior\pasta_teste\2022\novembro\08\tarde'
os.makedirs(novo_caminho_2)

#remover uma pasta
novo_caminho_3 = r'C:\Users\xicas\Documents\Junior\pasta_teste\2021\fevereiro\23\manhã'
os.rmdir(novo_caminho_3) #vai dar erro se a pasta não estiver vazia

print()
#LIDANDO COM ARQUIVOS
#abrir um arquivo selecionado
novo_caminho_4 = r'C:\Users\xicas\Documents\Junior\pasta_teste\2022\novembro\08\tarde\oi.txt'
os.startfile(novo_caminho_4) #dá pra usar o os.open de outra forma

#renomear
print("vc está em:", os.getcwd()) 
os.chdir(r'C:\Users\xicas\Documents\Junior\pasta_teste\2022\novembro\08\tarde')
print("agr vc está em:", os.getcwd())
os.rename('oi.txt', 'vlw.txt') #precisa estar na pasta onde o arquivo está

#remover
os.getcwd()
os.remove('vlw.txt')

#criar
path = './file9.txt'
mode = 0o666
flags = os.O_RDWR | os.O_CREAT
fd = os.open(path, flags, mode) #se tiver vai abrir pra escrita e leitura e se não existir vai criar
os.write(fd, "This is test".encode()) #escrevendo

os.lseek(fd,0,0)
string = os.read(fd, os.path.getsize(fd)) # lendo arquivo
print(string.decode())

os.close(fd)

#os.walk() acho que dá pra usar isso pra copiar e colar (tista tudo)
os.chdir(r'C:\Users\xicas\Documents\Junior\pasta_teste')
for root, dirs, files in os.walk(os.getcwd()):
    print(root)

print()

#CAMINHOS(sudmódulos os.path)
print("vc está em:", os.getcwd()) 
print("o nome da pasta que estou",os.path.basename(os.getcwd())) #dá o nome da pasta que estou

#caminhos comuns
caminho1 = r'C:\Users\xicas\Documents\Junior\pasta_teste\2021\janeiro'
caminho2 = r'C:\Users\xicas\Documents\Junior\pasta_teste\2021\fevereiro'
print("as pastas comuns entre os dois",os.path.commonpath([caminho1, caminho2])) #passar uma lista

#nome da pasta em que estou (caminho)
print(os.path.dirname(caminho1))

#os.path.join()
drive = "C:"
usuario = "xicas"
pasta_base = "Junior"
caminho = os.path.join(drive,r'Users', usuario,'Documentos',pasta_base) # junta as strings pra formar o caminho
print(caminho)

os.chdir(caminho)
print("voce esta", os.getcwd())

print("fim\n")

#mover arquivos
#os.rename("t.txt", "t.txt")

#copiar arquivos
import shutil

shutil.copy2(r"tz", r"c:\Users\franc\Documents\GitHub\t")

#follow_symlinks

# A seguir está a sintaxe para o método open() − os.open(file, flags[, mode]);
# Parâmetros arquivo − Nome do arquivo a ser aberto.

# flags − As constantes a seguir são opções para os sinalizadores. Eles podem ser combinados usando o operador OR bit a bit |. Alguns deles não estão disponíveis em todas as plataformas.

# os.O_RDONLY − aberto apenas para leitura
# os.O_WRONLY − aberto apenas para escrita
# os.O_RDWR − aberto para leitura e escrita
# os.O_NONBLOCK – não bloqueia ao abrir
# os.O_APPEND - anexar em cada gravação
# os.O_CREAT – cria arquivo se não existir
# os.O_TRUNC - truncar tamanho para 0
# os.O_EXCL − erro se criar e arquivo existir
# os.O_SHLOCK − obter atomicamente um bloqueio compartilhado
# os.O_EXLOCK − obter atomicamente um bloqueio exclusivo
# os.O_DIRECT − eliminar ou reduzir efeitos de cache
# os.O_FSYNC − gravações síncronas
# os.O_NOFOLLOW − não segue links simbólicos

# mode − Isso funciona de maneira semelhante ao método chmod()
