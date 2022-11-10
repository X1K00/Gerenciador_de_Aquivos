import os

class Files:
    def __init__(self) -> None:
        self.pasta_atual = os.getcwd()
        self.pastas = os.listdir()
        self.pasta_anterior = os.path.dirname(os.getcwd())
    
    def main(self):
        self.topo()
        for n, i in enumerate(self.pastas):
            print(n+1, "-", i)
        com = input("R: ")

        if com.isnumeric():
            self.com_numero(int(com))  
        else:
            self.com_letra(com)

    def topo(self):
        print("----------------------------------------------------------------|\n"
        "",os.getcwd(),"\n\n"
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
        print("letra", l)

         
arquivo = Files()
arquivo.main()
    