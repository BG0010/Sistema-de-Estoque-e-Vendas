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

    op = int(input("Digite a opção desejada: "))

    match op:

        case 1:
            from produto import cadastrarProduto
            lista_produtos = cadastrarProduto()

        case 2:
            from produto import editarProduto
            editarProduto(lista_produtos)

        case 3:
            from produto import removerProdutoID
            removerProdutoID(lista_produtos)

        case 4:
            from produto import buscarProdutoID
            buscarProdutoID(lista_produtos)

        case 5:
            from produto import buscarProdutoNome
            buscarProdutoNome(lista_produtos)

        case 6:
            from estoque import realizarVenda
            realizarVenda(lista_produtos)

        case 7:
            from produto import listarProdutosCodigo
            listarProdutosCodigo(lista_produtos)   
        case 8:
            from produto import listarProdutosCategoria
            listarProdutosCategoria(lista_produtos)
            
        case 0:
            print("Encerrando...")
            break

        case _:
            print("Opção inválida")