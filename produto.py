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
  return produto

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