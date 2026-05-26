import json
import produto


def salvarArquivo(lista_produtos):

    with open("produtos.json", "w", encoding="utf-8") as arquivo:

        json.dump(
            lista_produtos,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

    print("Dados salvos com sucesso!")


def carregarArquivo():

    try:

        with open(
            "produtos.json",
            "r",
            encoding="utf-8"
        ) as arquivo:

            lista_produtos = json.load(arquivo)

        # Atualiza contador de IDs
        if lista_produtos:

            maior_id = max(
                p["id_produto"]
                for p in lista_produtos
            )

            produto.contador = maior_id + 1

        print("Dados carregados com sucesso!")

        return lista_produtos

    except FileNotFoundError:

        print("Arquivo não encontrado.")
        return []

    except json.JSONDecodeError:

        print("Erro ao ler o arquivo.")
        return []