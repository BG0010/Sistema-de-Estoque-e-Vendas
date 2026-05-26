from datetime import date

# Contador para gerar IDs únicos
contador = 1


def novoID():
    global contador

    id_atual = contador
    contador += 1

    return id_atual


# Cadastrar Produto
def cadastrarProduto():

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    categoria = input("Digite a categoria do produto: ")

    produto = {
        "id_produto": novoID(),
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "categoria": categoria,
        "data_cadastro": date.today().strftime("%d/%m/%Y")
    }

    print("Produto cadastrado com sucesso!")

    return produto


# Editar Produto
def editarProduto(lista_produtos):

    id_editar = int(input("Digite o ID que deseja editar: "))

    for produto in lista_produtos:

        if produto["id_produto"] == id_editar:

            produto["nome"] = input("Novo nome: ")
            produto["preco"] = float(input("Novo preço: "))
            produto["quantidade"] = int(input("Nova quantidade: "))
            produto["categoria"] = input("Nova categoria: ")

            print("Produto editado com sucesso!")
            return

    print("ID não encontrado!")


# Remover Produto
def removerProdutoID(lista_produtos):

    id_remover = int(input("Digite o ID que deseja remover: "))

    for produto in lista_produtos:

        if produto["id_produto"] == id_remover:

            lista_produtos.remove(produto)

            print("Produto removido com sucesso!")
            return

    print("ID não encontrado!")


# Buscar por ID
def buscarProdutoID(lista_produtos):

    id_buscar = int(input("Digite o ID: "))

    for produto in lista_produtos:

        if produto["id_produto"] == id_buscar:

            print(produto)
            return

    print("Produto não encontrado.")


# Buscar por nome
def buscarProdutoNome(lista_produtos):

    nome = input("Digite o nome: ").lower()

    encontrou = False

    for produto in lista_produtos:

        if nome in produto["nome"].lower():

            print(produto)
            encontrou = True

    if not encontrou:
        print("Produto não encontrado.")


# Listar por código
def listarProdutosCodigo(lista_produtos):

    print("\nProdutos:\n")

    for produto in sorted(
        lista_produtos,
        key=lambda x: x["id_produto"]
    ):
        print(produto)


# Listar por categoria
def listarProdutosCategoria(lista_produtos):

    categoria = input("Digite a categoria: ").lower()

    encontrou = False

    for produto in lista_produtos:

        if produto["categoria"].lower() == categoria:

            print(produto)
            encontrou = True

    if not encontrou:
        print("Nenhum produto encontrado.")