import os
import shutil

class Files:
    def __init__(self,copia) -> None:
        self.pasta_atual = os.getcwd()
        self.pastas = os.listdir()
        self.pasta_anterior = os.path.dirname(os.getcwd())
        self.area_tranfer = copia
    
    def main(self):
        print("----------------------------------------------------------------|\n"
        "->",os.getcwd(),"\n"
        "n- criar pasta |d- remover |r- renomear |c- copiar |x- cortar |v- colar\n\n"
        "0 - Voltar")

        self.listar_pastas()
        n = input("R: ")
        if n.isnumeric():
            self.com_numero(int(n))  
        else:
            self.com_letra(n)

    def listar_pastas(self):
        for n, i in enumerate(self.pastas):
            print(n+1, "-", i)
        
    def com_numero(self, n):
        if n == 0:
            os.chdir(self.pasta_anterior)
        else:
            if os.path.isfile(self.pastas[n-1]):
                os.startfile(self.pastas[n-1])
            else:
                os.chdir("{}\{}".format(self.pasta_atual, self.pastas[n-1]))

        self.__init__(self.area_tranfer)
        self.main()

    def com_letra(self, l):
        copia = self.area_tranfer

        if l == "n":
            os.mkdir(input("Nome da nova pasta: "))
            print("Pasta criada com sucesso!!")

        elif l == "c":
            print("----------------------------------------------------------------|\n"
            "COPIAR ARQUIVO\n")
            self.listar_pastas()
            n = int(input("Copiar: "))
            copia = []

            print("Copiando:", self.pastas[n-1])
            copia.append("{}\{}".format(self.pasta_atual, self.pastas[n-1]))
            copia.append(self.pastas[n-1])

        elif l == "v":
            print("Nome do arquivo:", self.area_tranfer[1], "É arquivo:", os.path.isfile(self.area_tranfer[0]))
            print("Origem", self.area_tranfer[0])
            print("Destino", "{}\{}".format(self.pasta_atual, self.area_tranfer[1]))

            if os.path.isfile(self.area_tranfer[0]):
                shutil.copy2(self.area_tranfer[0], "{}\{}".format(self.pasta_atual, self.area_tranfer[1]))
            else:
                shutil.copytree(self.area_tranfer[0], "{}\{}".format(self.pasta_atual, self.area_tranfer[1]))
            print("Copiado com sucesso!!")

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

            if os.path.isfile(self.pastas[n-1]):
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
    