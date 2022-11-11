import os
import shutil

class Files:
    def __init__(self,copia) -> None:
        self.pasta_atual = os.getcwd()
        self.pastas = os.listdir()
        self.pasta_anterior = os.path.dirname(os.getcwd())
        self.copia_pastas = []
        self.copia_arquivo = copia
    
    def main(self):
        self.topo()
        self.listar_pastas()
        com = input("R: ")

        if com.isnumeric():
            self.com_numero(int(com))  
        else:
            self.com_letra(com)

    def listar_pastas(self):
        for n, i in enumerate(self.pastas):
            print(n+1, "-", i)

    def topo(self):
        print("----------------------------------------------------------------|\n"
        "->",os.getcwd(),"\n"
        "n- criar pasta |d- remover |r- renomear |c- copiar |x- cortar \n\n"
        "0 - Voltar")
        
    def com_numero(self, n):
        print("numero", n)
        if n == 0:
            os.chdir(self.pasta_anterior)
        else:
            if "." in self.pastas[n-1]:
                os.startfile(self.pastas[n-1])
            else:
                os.chdir("{}\{}".format(self.pasta_atual, self.pastas[n-1]))
        self.__init__(self.copia_arquivo)
        self.main()

    def com_letra(self, l):
        copia = self.copia_arquivo

        if l == "n":
            os.mkdir(input("Nome da pasta: "))
            print("Pasta criada com sucesso!!")

        elif l == "c":
            print("----------------------------------------------------------------|\n"
            "COPIAR ARQUIVO\n")
            self.listar_pastas()
            n = int(input("Copiar: "))
            copia = []
            copia_pastas = []

            if "." in self.pastas[n-1]:
                print("Copiando:", self.pastas[n-1])
                copia.append("{}\{}".format(self.pasta_atual, self.pastas[n-1]))
                copia.append(self.pastas[n-1])
                print(self.copia_arquivo)
            else:
                for root, dirs, files in os.walk("{}\{}".format(self.pasta_atual, self.pastas[n-1])):
                    for fim in files:
                        print("Copiando: {}\{}".format(root,fim))
                        #os.remove("{}\{}".format(root,fim))
                    else:
                        print("Copiando:", root)
                        #os.rmdir(root)
        elif l == "v":
            print(self.copia_arquivo)
            print("Origem", self.copia_arquivo[0])
            print("Destino", "{}\{}".format(self.pasta_atual, self.copia_arquivo[1]))
            shutil.copy2(self.copia_arquivo[0], "{}\{}".format(self.pasta_atual, self.copia_arquivo[1]), topdown=False)
            print("Copia pronta!")

        elif l == "r":
            print("----------------------------------------------------------------|\n"
            "RENOMEAR ARQUIVO\n")
            self.listar_pastas()
            n = int(input("Renomear: "))
            novo_nome = input("Novo nome: ")
            os.rename(self.pastas[n-1], novo_nome)
        
        elif l == "d":
            print("----------------------------------------------------------------|\n"
            "REMOVER ARQUIVO\n")
            self.listar_pastas()
            n = int(input("Remover: "))
            if "." in self.pastas[n-1]:
                print("Removendo:", self.pastas[n-1])
                os.remove("{}\{}".format(self.pasta_atual, self.pastas[n-1]))
            else:
                for root, dirs, files in os.walk("{}\{}".format(self.pasta_atual, self.pastas[n-1]), topdown=False):
                    for fim in files:
                        print("Removendo: {}\{}".format(root,fim))
                        os.remove("{}\{}".format(root,fim))
                    else:
                        print("Removendo:", root)
                        os.rmdir(root)

            print("Remoção com sucesso!!")

        self.__init__(copia)
        self.main()

         
arquivo = Files([])
arquivo.main()
    