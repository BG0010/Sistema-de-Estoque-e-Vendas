# Venda

def realizarVenda(lista_produtos):

    id_venda = int(input("Digite o código do produto que deseja vender: "))

    for produto in lista_produtos:

        if produto["codigo"] == id_venda:

            print("\nProduto encontrado:")
            print(produto)

            quantidade_venda = int(
                input("Digite a quantidade que deseja vender: ")
            )

            if quantidade_venda <= 0:
                print("Quantidade inválida.")
                return

            if quantidade_venda <= produto["quantidade"]:

                produto["quantidade"] -= quantidade_venda

                print("Venda realizada com sucesso!")
                print("Quantidade restante:",
                      produto["quantidade"])

            else:
                print("Quantidade insuficiente em estoque!")

            return

    print("Produto não encontrado!")


def relatorioEstoqueBaixo(lista_produtos):

    print("\nRelatório de estoque baixo:\n")

    encontrou = False

    for produto in lista_produtos:

        if produto["quantidade"] < 5:
            print(produto)
            encontrou = True

    if not encontrou:
        print("Nenhum produto com estoque baixo.")