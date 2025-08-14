from colorama import Fore, Back, Style

# Função principal que controla o fluxo do programa
def exibir_menu():
    print(Fore.BLUE, Back.RED, Style.DIM + "\n===SISTEMA DE CADASTRO===")
    print("1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Sair")
    print(Style.RESET_ALL)

def cadastrar_produto(lista_produtos):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    lista_produtos.append({"nome": nome, "preco": preco})
    print(f"Produto: '{nome}' cadastrado com sucesso!")

def listar_produtos(lista_produtos):
    if not lista_produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("\n=== LISTA DE PRODUTOS===")
        for i, produto in enumerate(lista_produtos, start = 1):
            print(f"{i}, {produto['nome']} - R$ {produto['preco']:.2f}")

def main():
    lista_produtos = []
    produtos = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção:") 

        if opcao == "1":
            cadastrar_produto(produtos)
        elif opcao == "2":
            listar_produtos(produtos)
        elif opcao == "3":
            print("Encerrando sistema ...")
            break
        else:
            print("Opção inválida!")            

# Execução do programa
if __name__=="__main__":
    main()