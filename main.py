while (True):
 
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
║ 10  - Salvar / Carregar dados                    ║
║                                                  ║
║  0  - Sair                                       ║
╚══════════════════════════════════════════════════╝
""")
 op = int(input("Digite a opção desejada: "))
 if op == 1:
    from produto import cadastrarProduto
    produto = cadastrarProduto()
    print(produto)
 elif op == 2:
    from produto import editarProduto
    editarProduto(produto)  