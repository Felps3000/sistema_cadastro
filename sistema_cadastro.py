from colorama import Fore, Back, Style

# Função principal que controla o fluxo do programa
def exibir_menu():
    print(Fore.BLUE + "\n===SISTEMA DE CADASTRO===")
    print("1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Sair")

def cadastrar_produto(lista_produtos):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    lista_produtos.append({"nome": nome, "preço": preco})
    print(f"Produto: '{nome}' cadastrado com sucesso!")



def main():
    lista_produtos = []
    produtos = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção:") 

        if opcao == "1":
            cadastrar_produto(produtos)
        elif opcao == "2":
            print("listar produtos")
        elif opcao == "3":
            print("Encerrando sistema ...")
            break
        else:
            print("Opção inválida!")            

# Execução do programa
if __name__=="__main__":
    main()