# Gerenciador_de_Aquivos
- Equipe:
  - Francisco da Cunha Júnior
  - Zennon Sampaio Miranda Lopes
  - Joyce Teixeira da Silva
  - Cicera Fabíola Angelo da Silva
  - Michael Alexandrino Freire

## Especificações
- [x] Alterar o diretorio de trabalho;
- [x] Listar arquivos e diretórios;
- #### Permitir consulta de informações sobre um determinado arquivo/diretório, tais como:
 - [x] Identificador de Prorietário (UID);
 - [x] Identificador de Grupo (GID);
 - [x] Permissões de acesso;
 - [x] Datas (criação, acesso e modificação);
 - [x] Tamanho em disco (armazenamento).
- #### Permitir alterar os seguintes atributos:
- [ ] Identificador de Prorietário (UID);
- [ ] Identificador de Grupo (GID);
- [ ] Permissões de acesso.
- #### Permitir operações em arquivos/diretórios, tais como:
- [x] Criação;
- [x] Remoção;
- [x] Cópia;
- [x] Movimento;
- [x] Criação de links simbólicos (ou atalhos).

## Funcionamento
- ![image](https://user-images.githubusercontent.com/101655473/207075800-12500102-5fa0-4682-b71c-7f840d448c3a.png)
- Para o sistema funcionar corretamente o programa precisa ser executado como Administrador no Prompt de Comando em uma máquina com sistema operacional Windows.
- ![image](https://user-images.githubusercontent.com/101655473/207077454-61b25222-eff6-4983-8beb-4f7716f6229a.png)
- Depois que achar a pasta com o arquivo “main.py”, execute-o.

## Tela Principal
- ![image](https://user-images.githubusercontent.com/101655473/207077710-727f38dc-e39f-4ddb-8f1d-c8b137f25c08.png)
- Na parte superior da tela é impresso o diretório onde o sistema está no momento.
- Logo abaixo, temos uma lista que especifica quais as funções presentes no sistema.
- Do meio para a parte inferior, temos uma lista com os nomes, datas de modificação, tamanhos de cada arquivo ou pasta presente no diretório atual e um número na frente de cada linha da lista.
- Na parte mais inferior temos um ‘R:’ indicando a entrada. 

## Navegação
- ![image](https://user-images.githubusercontent.com/101655473/207076837-80b87ef4-c702-47cd-9e38-f45b8eb5082e.png)
- A alteração do diretório de trabalho é feita através dos números que estão na frente do nome dos diretórios ou pelo próprio nome das pastas (se o nome da pasta for um número ou uma única letra o sistema não reconhecerá).
- Se o número ou nome de algum arquivo for escolhido, o arquivo será executado.
- O número 0 ou a palavra “Voltar” são os comandos padrão para voltar uma pasta.

## Funções
- ### “n” - Criar pasta
  - ![image](https://user-images.githubusercontent.com/101655473/207078354-9a299ea8-b11e-49f9-866b-88408afb36ed.png)
  - Depois de chamar a função Criar Pasta o usuário vai digitar o nome da nova pasta e pronto.
  - ![image](https://user-images.githubusercontent.com/101655473/207078578-7c3770c2-f11f-436d-b28b-5293e7c46863.png)
- ### “r” - Renomear
  - ![image](https://user-images.githubusercontent.com/101655473/207079886-b39221a2-974f-4799-bb78-b1558b1ec987.png)
  - Depois de chamar a função Renomear, o usuário vai escolher o número ou digitar o nome da pasta ou do arquivo que deseja alterar o nome.
  - ![image](https://user-images.githubusercontent.com/101655473/207080026-3c33964c-5e3f-437e-b8de-6b54821bf074.png)

- ### “d” - Remover
  - ![image](https://user-images.githubusercontent.com/101655473/207080149-8e4486f8-a7e7-4e2b-aa96-626c4a54892b.png)
  - Depois de chamar a função Remover, o usuário vai escolher o número ou digitar o nome da pasta ou do arquivo que deseja deletar.
  - ![image](https://user-images.githubusercontent.com/101655473/207080277-788355b3-5373-4e7e-81f9-767091041627.png)
  - Quando executado, a função retornará todos os diretórios que acabaram de ser removidos.
  
- ### “c” - Copiar
  - ![image](https://user-images.githubusercontent.com/101655473/207080469-a621d41a-5455-4d2c-8989-0eac6026847f.png)
  - Quando chamada a função Copiar o usuário vai escolher o número ou digitar o nome da pasta ou do arquivo que deseja copiar.
  - ![image](https://user-images.githubusercontent.com/101655473/207081160-ed5acaaf-182c-44c9-80b6-bc5ddd975c40.png)
  - Quando copiado o objeto que agora estará na área de transferência, ficará sendo setado à frente da indicação do comando colar.
  - O usuário poderá navegar livremente pelos diretórios, e sempre que chamar o comando colar (“v”) o objeto copiado terá uma nova cópia, ao menos que o tente ser colado na pasta de origem.
  - O ‘c’ à frente do nome do arquivo indica que existe um objeto a ser clonado.
  
- ### “x” - Cortar
  - ![image](https://user-images.githubusercontent.com/101655473/207081427-4b51063b-926e-4ea1-be39-33d16f85427d.png)
  - Quando chamada a função Cortar o usuário vai escolher o número ou digitar o nome da pasta ou do arquivo que deseja recortar.
  - ![image](https://user-images.githubusercontent.com/101655473/207081578-80cf546d-582c-4707-8454-c2fe3ec7967c.png)
  - Quando cortado o objeto que agora estará na área de transferência, ficará sendo setado à frente da indicação do comando colar.
  - O usuário poderá navegar livremente pelos diretórios, e assim que chamar o comando colar (“v”) o objeto cortado será movido para o novo diretório, ao menos que o tente ser colado na pasta de origem.
  - Após ser colado no novo diretório, o objeto será apagado do diretório de origem.
  - O ‘x’ à frente do nome do arquivo indica que existe um objeto a ser recortado.

- ### “v” - Colar
  - ![image](https://user-images.githubusercontent.com/101655473/207081958-d9707c26-b6e7-48e3-b3fe-44561bb1df5a.png)
  - Irá colar, o que estiver na área de transferência para o diretório que o sistema estiver, algum objeto copiado com a função copiar (“c”) ou recortado com a função cortar (“x”).
  
- ### “l” - Criar atalho (Permissões de administrador)
  - ![image](https://user-images.githubusercontent.com/101655473/207082134-257ba86e-b812-42f6-913e-e80bde65bfeb.png)
  - Depois de chamar a função Criar atalho, o usuário vai escolher o número ou digitar o nome da pasta ou do arquivo que deseja criar o atalho.
  - ![image](https://user-images.githubusercontent.com/101655473/207082229-2d053821-efb3-4355-b6e4-7ea3d51c5661.png)
  - Após selecionado o objeto para ser criado o atalho, o usuário vai navegar até a pasta onde ele deseja criar o atalho.
  - “c” cancela a ação.
  - “v” cria o atalho no diretório escolhido.
  - ![image](https://user-images.githubusercontent.com/101655473/207082429-1320f34e-a082-430c-9633-661ee3383fb7.png)
  - Quando criado o atalho, o nome do arquivo ou pasta é modificado, ficando com “(atalho)_” na frente do nome original.

- ### “i” - Informações
  - ![image](https://user-images.githubusercontent.com/101655473/207082645-594f6270-86d7-473e-b131-5d2d92b426da.png)
  - Depois de chamar a função Informações, o usuário vai escolher o número ou digitar o nome da pasta ou do arquivo que deseja ver as informações.
  - ![image](https://user-images.githubusercontent.com/101655473/207082797-63a1f9b4-6ebe-4e6b-9aa8-dbe7fceb84eb.png)
  - Após escolhido o arquivo ou a pasta, as informações (Nome, IP Proprietário, IP Grupo, Criação, Modificação, Acesso, Tamanho e Permissões) serão impressas na tela.
  - Abaixo das informações teremos a opção de voltar.
  - Alterar Proprietário, Alterar Grupo e Alterar Acessos, não foram finalizados.
