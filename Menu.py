inventario = []

while True:
    print('-----------------------------------')
    print('Inventário de produtos.')
    print('1.Adicionar produtos.')
    print('2.Consultar preços.')
    print('3.Listar produtos.')
    print('4.Total em estoque.')

    opcao = int(input("Digite uma opcao: "))
    if opcao == 1:

        nome = str(input('Digite o nome do produto: '))
        preco = float(input('Digite o preco do produto: '))
        quantidade = int(input('Digite a quantidade de produtos: '))
        categoria = str(input('Digite a categoria do seu produto: '))
        produto = {'nome': nome,
                   'preco': preco,
                   'quantidade': quantidade,
                   'categoria': categoria}
        inventario.append(produto)
        print('Produto adicionado com sucesso!')

    elif opcao == 2:
        nome_produto = str(input('Digite o nome do produto que deseja consultar: '))
        for produto in inventario:
            if nome_produto == produto['nome']:
                print(f"Preço do produto {nome_produto}: R${produto['preco']}")
                # f antes da string facilita a inserção de variáveis ou expressões dentro da string
                break
    

    elif opcao == 3:
        print('Lista de produtos:')
        for produto in inventario:
            print(f"Nome: {produto['nome']}, Preço: R${produto['preco']}, Quantidade: {produto['quantidade']}, Categoria: {produto['categoria']}")
    
    elif opcao == 4:
        total_estoque = 0
        for produto in inventario:
            total_estoque += produto['quantidade']
        print(f"Total de itens em estoque: {total_estoque}")
    else:
        print("Opção inválida. Tente novamente.")