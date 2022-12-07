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
        "i- informações |v- colar->", self.area_tranfer[1],"_",self.area_tranfer[2],"\n")

        self.listar_pastas()
        n = input("R: ")
        if n.isnumeric():
            self.navegacao(int(n))  
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
            #print(n+1, "-", i)  
    def navegacao(self, n): #Todos os comandos numericos sõa direcionados para esse metodo
        if n == 0:
            os.chdir(self.pasta_anterior) # 0 retona uma pasta no diretorio 
        else: #Qualquer outro numero além de o 0 entra em uma pasta ou abre um arquivo correspondente ao numero digitado
            if os.path.isfile(self.pastas[n-1]):  
                os.startfile(self.pastas[n-1]) # Abre arquivo
            else:
                os.chdir(os.path.join(self.pasta_atual, self.pastas[n-1])) #Entra na pasta

        self.__init__(self.area_tranfer) # O self.area_transfer sempre é repassado para que possa ser colado em qualquer lugar
        self.main()

    def apagar(self, end, n):
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

    def copiar(self, n, t):
        copia = []
        print("Copiando:", self.pastas[n-1])
        copia.append(self.pasta_atual)
        copia.append(self.pastas[n-1]) # Adiciona o endereço e o nome do objeto escolhido a uma lista que será salva
        copia.append(t)
        return copia

    def comandos(self, l): #Todos os comandos com letras estão nesse metodo
        copia = self.area_tranfer

        if l == "s":
            print("Saindo do sistema...")
            exit()

        elif l == "x":
            print("----------------------------------------------------------------------|\n"
            "CORTAR\n")
            self.listar_pastas()
            n = int(input("Cortar: "))
            copia = self.copiar(n, "x")

        elif l == "n": # "n" cria uma nova pasta
            os.mkdir(input("Nome da nova pasta: "))
            print("Pasta criada com sucesso!!")

        elif l == "c": # "c" faz a copia do arquivo ou da pasta
            print("----------------------------------------------------------------------|\n"
            "COPIAR\n")
            self.listar_pastas()
            n = int(input("Copiar: "))
            copia = self.copiar(n, "c")

        elif l == "v": #           
            orig = os.path.join(self.area_tranfer[0], self.area_tranfer[1])
            dest = os.path.join(self.pasta_atual, self.area_tranfer[1])
            print("Origem", orig)
            print("Destino", dest)

            if os.path.isfile(orig):
                shutil.copy2(orig, dest)
            else:
                shutil.copytree(orig, dest)
            if self.area_tranfer[2] == "c":
                print("Copiado com sucesso!!")
            else:
                self.apagar(self.area_tranfer[0], self.area_tranfer[1])
                print("Cortado com sucesso!!")

        elif l == "r": # "r" renomeia o arquivo ou a pasta selecionado
            print("----------------------------------------------------------------------|\n"
            "RENOMEAR\n")
            self.listar_pastas()
            n = int(input("Renomear: "))
            novo_nome = input("Novo nome: ")
            os.rename(self.pastas[n-1], novo_nome)
        
        elif l == "d": # "d" apaga o arquivou ou pasta selecionada 
            print("----------------------------------------------------------------------|\n"
            "REMOVER\n")
            self.listar_pastas()
            n = int(input("Remover: "))
            end = self.pasta_atual
            path = self.pastas[n-1]

            self.apagar(end, path)          
            print("Remoção com sucesso!!")
        
        elif l == "i":
            print("----------------------------------------------------------------------|\n"
            "INFORMAÇÕES\n")
            self.listar_pastas()
            n = int(input("Informações: "))

            path = self.pastas[n-1]
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
                    print("Não está disponivel no momento")
                    #os.fchown(path, pro, -1)
                elif acao == "2":
                    gru = input("Novo Grupo: ")
                    print("Não está disponivel no momento")
                    #os.fchown(path, -1, gru)
                elif acao == "3":
                    print("Não está disponivel no momento")
    

        self.__init__(copia)
        self.main()
       
arquivo = Files(["","",""])
arquivo.main()