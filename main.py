import os 
import csv

if os.path.exists("Produtos.cvs"):
    produtos = carregar_produtos()
else:
    produtos = []

def salvar_produtos(produtos):
    with open("produtos.csv", "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["Nome", "Preço"])

        for produto in produtos:
            escritor.writerow(produto)

def carregar_produtos():
    with open("produtos.csv", "r", encoding="utf-8") as f:
        leitor = csv.reader(f)
        next(leitor)
        for linha in leitor:  
            produtos.append(linha)

def mostrar_menu(qtd_produtos):
    print("---------- Menu ----------\n")
    print(f"Produtos cadastrados: {qtd_produtos}")
    print("1 - Cadastrar produto")
    print("2 - Consultar produto")
    print("3 - Listar produtos")
    print("4 - Alterar produto")
    print("0 - Sair\n")

def alternar_produto(produtos):
    nome_busca = input("Digite o nome do produto: ")
    encontra = False

    for produto in produtos:
        if produto[0].lower() == nome_busca.lower():
            encontrado = True
            print(f"Produto encontrado: {produto[0]} - R$ {produto[1]:.2f}")
            novo_nome = input("Novo nome: ")
            while True:
                novo_preco = float(input("Novo preço: "))

                if novo_preco >= 0:
                    break
                else:
                    print("O preço não pode ser negativo.")
            produto[0] = novo_nome
            produto[1] = novo_preco
            salvar_produtos(produtos)

            print("Produto alterado com sucesso!")
            break


def cadastrar_produto(produtos):
    nome = input("Nome do produto: ")
    preco_valido = False
    while not preco_valido:
        preco = float(input("Preço do produto (maior que zero): "))
        if preco > 0:
            preco_valido = True
        else:
            print("Preço inválido. Digite um valor maior que zero.")
    produtos.insert(0, [nome, preco])
    print("Produto cadastrado com sucesso!")
    print(f"Total de produtos: {len(produtos)}")

def consultar_produto(produtos):
    nome_busca = input("Digite o nome do produto: ")
    encontrado = False
    i = 0
    while i < len(produtos):
        if produtos[i][0].lower() == nome_busca.lower():
            print(
                f"Produto encontrado: "
                f"{produtos[i][0]} - R$ {produtos[i][1]:.2f}"
            )
            encontrado = True
        i += 1
    if not encontrado:
        print("Produto não encontrado.")

def listar_produtos(produtos):
    print("=== Produtos cadastrados ===\n")
    numero_de_pontos = 15
    for i in range(len(produtos)):
        caractres = len(produtos[i][0])
        if caractres > numero_de_pontos:
            numero_de_pontos = caractres + 2
    for i in range(len(produtos)):
        caractres = len(produtos[i][0])
        quantida_de_pontos = "." *(numero_de_pontos - caractres)
        print(f"{i+1}. {produtos[i][0]} {quantida_de_pontos} R${produtos[i][1]:.2f}")
        input("\nPressione entre para continuar...")


print(f"´" * 15)

while True:
    mostrar_menu(len(produtos))
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_produto(produtos)
    elif opcao == "2":
        consultar_produto(produtos)
    elif opcao == "3":
        listar_produtos(produtos)
    elif opcao == "4":
        alterar_produto(produtos)
        input("\nPressione enter para continuar...")
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")
