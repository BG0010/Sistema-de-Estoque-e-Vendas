lista_produtos = []

while True:

    print("""
╔══════════════════════════════════════════════════╗
║                SISTEMA DE PRODUTOS               ║
╠══════════════════════════════════════════════════╣
║  1  - Cadastrar produto                          ║
║  2  - Editar produto                             ║
║  3  - Remover produto pelo código                ║
║  4  - Buscar produto por código                  ║
║  5  - Buscar produtos por nome                   ║
║  6  - Registrar venda                            ║
║  7  - Listar produtos por código                 ║
║  8  - Listar produtos por categoria              ║
║  9  - Relatório de estoque baixo                 ║
║ 10 - Salvar / Carregar dados                     ║
║                                                  ║
║  0  - Sair                                       ║
╚══════════════════════════════════════════════════╝
""")

    try:
        op = int(input("Digite a opção desejada: "))

    except ValueError:
        print("Digite apenas números.")
        continue

    match op:

        case 1:
            from produto import cadastrarProduto

            produto = cadastrarProduto()
            lista_produtos.append(produto)

        case 2:
            if lista_produtos:
                from produto import editarProduto
                editarProduto(lista_produtos)
            else:
                print("Nenhum produto cadastrado.")

        case 3:
            if lista_produtos:
                from produto import removerProdutoID
                removerProdutoID(lista_produtos)
            else:
                print("Nenhum produto cadastrado.")

        case 4:
            if lista_produtos:
                from produto import buscarProdutoID
                buscarProdutoID(lista_produtos)
            else:
                print("Nenhum produto cadastrado.")

        case 5:
            if lista_produtos:
                from produto import buscarProdutoNome
                buscarProdutoNome(lista_produtos)
            else:
                print("Nenhum produto cadastrado.")

        case 6:
            if lista_produtos:
                from estoque import realizarVenda
                realizarVenda(lista_produtos)
            else:
                print("Nenhum produto cadastrado.")

        case 7:
            if lista_produtos:
                from produto import listarProdutosCodigo
                listarProdutosCodigo(lista_produtos)
            else:
                print("Nenhum produto cadastrado.")

        case 8:
            if lista_produtos:
                from produto import listarProdutosCategoria
                listarProdutosCategoria(lista_produtos)
            else:
                print("Nenhum produto cadastrado.")

        case 9:
            if lista_produtos:
                from estoque import relatorioEstoqueBaixo
                relatorioEstoqueBaixo(lista_produtos)
            else:
                print("Nenhum produto cadastrado.")

        case 10:

            from arquivos import salvarArquivo, carregarArquivo

            print("""
1 - Salvar dados
2 - Carregar dados
""")

            escolha = input("Escolha: ")

            if escolha == "1":
                salvarArquivo(lista_produtos)

            elif escolha == "2":
                lista_produtos = carregarArquivo()

            else:
                print("Opção inválida.")

        case 0:
            print("Sistema encerrado.")
            break

        case _:
            print("Opção inválida.")