from datetime import date 

# Contador para gerar IDs únicos para cada produtos
contador = 1
def novoID():
  global contador
  id_atual = contador
  contador += 1
  return id_atual
   
# Cadastrar Produto
def cadastrarProduto():
  nome = str(input("Digite o nome do produto: "))
  preco = float(input("Digite o preço do produto: "))
  quantidade = int(input("Digite a quantidade do produto: "))
  categoria = str(input("Digite a categoria do produto: "))
  data_cadastro = date.today().strftime("%d/%m/%Y")
  id_produto = novoID()
  print("Produto cadastrado com sucesso!")
  
  produto = {
    "nome": nome,
    "preco": preco,
    "quantidade": quantidade,
    "categoria": categoria,
    "data_cadastro": data_cadastro,
    "id_produto": id_produto
  }

  lista_produtos = []
  lista_produtos.append(produto)
  return lista_produtos

# Editar Produto
def editarProduto(produto):
  print("Digite o ID que deseja editar: ")
  id_editar = int(input())
  if id_editar == produto["id_produto"]:
    print("Produto encontrado!")
    print("Digite o novo nome do produto: ")
    produto["nome"] = str(input())
    print("Digite o novo preço do produto: ")
    produto["preco"] = float(input())
    print("Digite a nova quantidade do produto: ")
    produto["quantidade"] = int(input())
    print("Digite a nova categoria do produto: ")
    produto["categoria"] = str(input())
    print("Produto editado com sucesso!")
  else:
    print("ID não encontrado!")

def removerProdutoID(lista_produtos):
  print("Digite o ID que deseja remover: ")
  id_remover = int(input())

  for produto in lista_produtos:
    if id_remover == produto["id_produto"]:
      lista_produtos.remove(produto)
      print("O Produto foi removido com sucesso!")
      print("Produto removido: ", produto)
      break
  else:
    print("ID não encontrado!")  

def buscarProdutoID(lista_produtos):
  print("Digite o ID que deseja buscar: ")
  id_buscar = int(input())

  for produto in lista_produtos:
    if id_buscar == produto["id_produto"]:
      print("Produto encontrado: ", produto)
      break
  else:
    print("ID não encontrado!")
# Buscar produto por nome
def buscarProdutoNome(lista_produtos):
  print("Digite o nome do produto que deseja buscar: ")
  nome_buscar = str(input())

  for produto in lista_produtos:
    if nome_buscar.lower() in produto["nome"].lower():
      print("Produto encontrado: ", produto)
      break
  else:
    print("Produto não encontrado!")

def listarProdutosCodigo(lista_produtos):
  print("Produtos listados por código: ")
  for produto in sorted(lista_produtos, key=lambda x: x["id_produto"]):
    print(produto)

def listarProdutosCategoria(lista_produtos):
    categoria = input("Digite a categoria: ").lower()
    print("\nProdutos encontrados:\n")
    encontrou = False

    for produto in lista_produtos:

        if produto["categoria"].lower() == categoria:
            print(produto)
            encontrou = True

    if not encontrou:
        print("Nenhum produto encontrado.")