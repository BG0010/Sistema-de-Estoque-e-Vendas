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
    lista_produtos = cadastrarProduto()
    print(lista_produtos)
 elif op == 2:
    from produto import editarProduto
    editarProduto(lista_produtos)  
 elif op == 3:
   from produto import removerProdutoID
   removerProdutoID(lista_produtos)
 elif op == 4:
   from produto import buscarProdutoID
   buscarProdutoID(lista_produtos)
   