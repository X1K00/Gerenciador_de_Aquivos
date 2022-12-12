import os, sys, stat
import shutil
import time

class Files:
    def __init__(self,copia) -> None:
        self.pasta_atual = os.getcwd()
        self.pastas = os.listdir()
        self.pasta_anterior = os.path.dirname(os.getcwd())
        self.area_tranfer = copia
    
    def main(self):
        print("----------------------------------------------------------------------|\n"
        "->",os.getcwd(),"\n\n"
        "n- criar pasta |d- remover |r- renomear |c- copiar |x- cortar |s- SAIR\n"
        "i- informações |l- criar atalho |v- colar >", self.area_tranfer[1],"_",self.area_tranfer[2],"\n")

        self.listar_pastas()
        n = input("R: ")

        if n.isnumeric() or (len(n)>1):
            try:
                self.navegacao(n) 
            except FileNotFoundError:
                print("\n\nArquivo ou pasta inexistente!!")

            self.__init__(self.area_tranfer) # O self.area_transfer sempre é repassado para que possa ser colado em qualquer lugar
            self.main() 
        else:
            self.comandos(n)

    def listar_pastas(self): #Cria uma lista com todos os diretorios e arquivos do local, todos enumerados
        try:
            m = len(max(self.pastas, key=len))
            if m <= 35:
                maior = m
            else:
                maior = 35
        except ValueError:
            maior = 7

        print("    {:<{}} | Modificação             | Tamanho\n0 - Voltar".format("Nome", maior))
        for n, i in enumerate(self.pastas):
            t_modific = os.path.getmtime(i)
            tamanho = os.path.getsize(i)
            modif = time.strftime("%d/%m/%Y ás %H:%M", time.gmtime(t_modific))
            
            print("{} - {:<{}} | {}     | {} KB".format(n+1, i[:35], maior, modif, round(tamanho/1000)))
             
    def listar_pastas_2(self): #Cria uma lista com todos os diretorios e arquivos do local, todos enumerados
        try:
            m = len(max(self.pastas, key=len))
            if m <= 35:
                maior = m
            else:
                maior = 35
        except ValueError:
            maior = 7

        print("    {:<{}} \n0 - Voltar".format("Nome", maior))
        for n, i in enumerate(self.pastas):
            print(n+1, "-", i)  
    
    def navegacao(self, n): #Todos os comandos referentes a navegação estão aqui
        try:    
            if (n == "0") or (n == "Voltar"):
                os.chdir(self.pasta_anterior) # 0 retona uma pasta no diretorio 
            elif n.isnumeric(): #Qualquer outro numero além de o 0 entra em uma pasta ou abre um arquivo correspondente ao numero digitado
                n = int(n)
                if os.path.isfile(self.pastas[n-1]):  
                    os.startfile(self.pastas[n-1]) # Abre arquivo
                else:
                    os.chdir(os.path.join(self.pasta_atual, self.pastas[n-1])) #Entra na pasta
            else:
                if os.path.isfile(n):  
                    os.startfile(n) # Abre arquivo
                else:
                    os.chdir(os.path.join(self.pasta_atual, n))
        except IndexError:
            print("\n\nPasta ou arquivo não encontrado!!")
    
    def apagar(self, end, n): # Apaga os arquivos ou pastas
        if os.path.isfile(n): #Apaga arquivos
            print("Removendo:", n)
            os.remove(os.path.join(end, n)) 
        else: #Apaga pasta e tudo que tem dentro da pasta
            for root, dirs, files in os.walk(os.path.join(end, n), topdown=False):
                for fim in files:
                    print("Removendo:", os.path.join(root,fim))
                    os.remove(os.path.join(root,fim))
                else:
                    print("Removendo:", root)
                    os.rmdir(root)

    def copiar(self, n, t): # Copia os arquivos ou pastas
        if n.isnumeric():
            n = int(n)
            copia = []
            print("Copiando:", self.pastas[n-1])
            copia.append(self.pasta_atual)
            copia.append(self.pastas[n-1]) # Adiciona o endereço e o nome do objeto escolhido a uma lista que será salva
            copia.append(t)
            return copia
        else:
            copia = []
            print("Copiando:", n)
            copia.append(self.pasta_atual)
            copia.append(n) # Adiciona o endereço e o nome do objeto escolhido a uma lista que será salva
            copia.append(t)
            return copia

    def atalho(self, p, a): # Função que cria links simbolicos
        print("----------------------------------------------------------------------|\n"
        "CRIAR ATALHO\n"
        "c- cancelar |v- criar atalho >",a ,"\n"
        "\nSelecione um diretorio para colar o atalho!\n")
        self.listar_pastas_2()
        n = input("Criar Atalho: ")

        if n.isnumeric():
            self.navegacao(n)
            self.__init__(self.area_tranfer)
            self.atalho(p, a)  
        else:
            src = os.path.join(p,a)
            dst = os.path.join(self.pasta_atual,"(atalho)_"+a)

            try:
                if n == "c":
                    print("\nCancelado!!\n")
                    pass
                elif n == "v":
                    if os.path.isfile(src):
                        os.symlink(src, dst)
                    else:
                        os.symlink(src, dst, target_is_directory=True)
                    print("\nAtalho criado com sucesso!!\n")
                else:
                    print("\nComando invalido!!\n")
                    self.atalho(p, a)

            except OSError:
                print("\n\nVocê precisa acessar essa função como administrador!!")

    def comandos(self, n): # Todos os comandos menos os de navegação estão aqui
        copia = self.area_tranfer
        l = n.lower()

        try:
            if l == "s": # "s" para sair do sistema
                print("Saindo do sistema...")
                exit()

            elif l == "x": # "x" para cortar um arquivo ou pasta
                print("----------------------------------------------------------------------|\n"
                "CORTAR\n")
                self.listar_pastas()
                n = input("Cortar: ")

                if n == "0" or (n == "Voltar"):
                    pass
                elif n.isnumeric():
                    copia = self.copiar(n, "x")
                else:
                    if os.path.exists(n):
                        copia = self.copiar(n, "x")
                    else:
                        print("\n\nArquivo ou pasta inexistente!!")

            elif l == "n": # "n" cria uma nova pasta
                os.mkdir(input("Nome da nova pasta: "))
                print("Pasta criada com sucesso!!")

            elif l == "c": # "c" faz a copia do arquivo ou da pasta
                print("----------------------------------------------------------------------|\n"
                "COPIAR\n")
                self.listar_pastas()
                n = input("Copiar: ")

                if n == "0" or (n == "Voltar"):
                    pass
                elif n.isnumeric():
                    copia = self.copiar(n, "c")
                else:
                    if os.path.exists(n):
                        copia = self.copiar(n, "c")
                    else:
                        print("\n\nArquivo ou pasta inexistente!!")

            elif l == "l": # "l" para criar um link
                print("----------------------------------------------------------------------|\n"
                "ATALHO\n")
                self.listar_pastas()
                n = input("Atalho de: ")

                if n == "0" or (n == "Voltar"):
                    pass
                elif n.isnumeric():
                    n = int(n)
                    path = self.pasta_atual
                    arq = self.pastas[n-1]
                    self.atalho(path, arq)
                else:
                    if os.path.exists(n):
                        path = self.pasta_atual
                        arq = n
                        self.atalho(path, arq)
                    else:
                        print("\n\nArquivo ou pasta inexistente!!")
                
            elif l == "v": # "v" para colar os arquivos ou pastas cortadas ou copiadas
                try:
                    orig = os.path.join(self.area_tranfer[0], self.area_tranfer[1])
                    dest = os.path.join(self.pasta_atual, self.area_tranfer[1])

                    if os.path.isfile(orig):
                        shutil.copy2(orig, dest)
                    else:
                        shutil.copytree(orig, dest)
                    if self.area_tranfer[2] == "c":
                        print("Copiado com sucesso!!")
                    else:
                        self.apagar(self.area_tranfer[0], self.area_tranfer[1])
                        copia = ["","",""]
                        print("Cortado com sucesso!!")

                except shutil.SameFileError:
                    print("\n\nJá existe um arquivo ou pasta com esse nome!")
                except FileNotFoundError:
                    print("\n\nSelecione uma pasta ou arquivo para ser colado!!")

            elif l == "r": # "r" renomeia o arquivo ou a pasta selecionado
                print("----------------------------------------------------------------------|\n"
                "RENOMEAR\n")
                self.listar_pastas()
                n = input("Renomear: ")

                try:
                    if n == "0" or (n == "Voltar"):
                        pass
                    elif n.isnumeric():
                        n = int(n)
                        print("Renomear:",self.pastas[n-1])
                        novo_nome = input("Novo nome: ")
                        os.rename(self.pastas[n-1], novo_nome)
                    else:
                        if os.path.exists(n):
                            novo_nome = input("Novo nome: ")
                            os.rename(n, novo_nome)
                        else:
                            print("\n\nArquivo ou pasta inexistente!!")
                except FileExistsError:
                    print("\n\nNão é possível criar um arquivo já existente!!")
            
            elif l == "d": # "d" apaga o arquivou ou pasta selecionada 
                print("----------------------------------------------------------------------|\n"
                "REMOVER\n")
                self.listar_pastas()
                n = input("Remover: ")

                if n == "0" or (n == "Voltar"):
                    pass
                elif n.isnumeric():
                    n = int(n)
                    self.apagar(self.pasta_atual, self.pastas[n-1])          
                    print("Removido com sucesso!!")
                else:
                    if os.path.exists(n):
                        self.apagar(self.pasta_atual, n)          
                        print("Removido com sucesso!!")
                    else:
                        print("\n\nArquivo ou pasta inexistente!!")
            
            elif l == "i": # "i" para saber informações sobre determinada pasta ou arquivo
                print("----------------------------------------------------------------------|\n"
                "INFORMAÇÕES\n")
                self.listar_pastas()
                n = input("Informações: ")
                path = None

                if n == "0" or (n == "Voltar"):
                    pass
                elif n.isnumeric():
                    n = int(n)
                    path = self.pastas[n-1]
                else:
                    if os.path.exists(n):
                        path = n
                    else:
                        print("\n\nArquivo ou pasta inexistente!!")

                if path == None:
                    pass
                else:
                    t_criacao = os.path.getctime(path)
                    t_modific = os.path.getmtime(path)
                    t_acess = os.path.getatime(path)
                    tamanho = os.path.getsize(path)
                    proprie = os.stat(path).st_uid
                    grupo = os.stat(path).st_gid
                    p_ler = os.access(path, os.R_OK)
                    p_gra = os.access(path, os.W_OK)
                    p_exe = os.access(path, os.X_OK)

                    while True:
                        print("----------------------------------------------------------------------|\n"
                        "INFORMAÇÕES\n")
                        print("Nome:",path)
                        print("IP Proprietario:", proprie)
                        print("IP Grupo:", grupo)
                        print(time.strftime("Criado em: %d/%m/%Y ás %H:%M", time.gmtime(t_criacao)))
                        print(time.strftime("Modificado em: %d/%m/%Y ás %H:%M", time.gmtime(t_modific)))
                        print(time.strftime("Acessado em: %d/%m/%Y ás %H:%M", time.gmtime(t_acess)))
                        print("Tamanho: {} KB ({} bytes)".format(round(tamanho/1000), tamanho))
                        print("Permições: Ler: {} | Gravar: {} | Executar: {}".format(p_ler, p_gra, p_exe))
                        print()
                        acao = input("0 - Voltar\n1 - Alterar Proprietario\n2 - Alterar Grupo\n3 - Alterar Acessos\nR: ")
                        
                        if acao == "0":
                            break
                        
                        elif acao == "1":
                            pro = input("Novo Proprietario: ")
                            print("\n\nNão está disponivel nesse sistema operacional")
                            #os.fchown(path, pro, -1)
                        elif acao == "2":
                            gru = input("Novo Grupo: ")
                            print("\n\nNão está disponivel nesse sistema operacional")
                            #os.fchown(path, -1, gru)
                        elif acao == "3":
                            print("\n\nNão está disponivel nesse sistema operacional")

            elif l == "w": # "w" informações sobre o sistema
                sistema = os.environ
                
                while True:
                    print("----------------------------------------------------------------------|\n"
                    "INFORMAÇÕES SOBRE O SISTEMA\n")
                    print("usuario:", sistema['USERNAME'])
                    print("Sistema Operacional:", sistema['OS'])
                    print("Linguagem:", sistema['LANG'])
                    print("Processador:", sistema['PROCESSOR_IDENTIFIER'])

                    acao = input("\n0 - Voltar\nR: ")
                    if acao == "0" or (acao == "Voltar"):
                        break
                    else:
                        print("\nComando invalido!!")

            else:
                print("\n\nComando inexistente!!")
        
        except IndexError:
            print("\n\nPasta ou arquivo não encontrado!!") 
        except KeyError:
            print("\n\nOuve um erro!!")  
        
        self.__init__(copia)
        self.main()

arquivo = Files(["","",""])
arquivo.main()