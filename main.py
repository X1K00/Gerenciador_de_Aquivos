import os

class Files:
    def __init__(self) -> None:
        self.pasta_atual = os.getcwd()
        self.pastas = os.listdir()
        self.pasta_anterior = os.path.dirname(os.getcwd())
    
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
        "n- criar pasta |r- remover pasta |c- copiar |x- cortar \n\n"
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
        self.__init__()
        self.main()

    def com_letra(self, l):
        if l == "n":
            os.mkdir(input("Nome da pasta: "))
            print("Pasta criada com sucesso!!")
        
        elif l == "r":
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

        self.__init__()
        self.main()

         
arquivo = Files()
arquivo.main()
    