# Venda

def realizarVenda(lista_produtos):
  print("Digite o ID do produto que deseja vender: ")
  id_venda = int(input())
  for produto in lista_produtos:
    if id_venda == produto["id_produto"]:
      print("Produto encontrado: ", produto)
      print("Digite a quantidade que deseja vender: ")
      quantidade_venda = int(input())
      if quantidade_venda <= produto["quantidade"]:
        produto["quantidade"] -= quantidade_venda
        print("Venda realizada com sucesso!")
        print("Produto atualizado: ", produto)
      else:
        print("Quantidade insuficiente em estoque!")
      break
  else:
    print("ID não encontrado!")

def relatorioEstoqueBaixo(lista_produtos):
  print("Relatório de estoque baixo:")
  for produto in lista_produtos:
    if produto["quantidade"] < 5:
      print(produto)