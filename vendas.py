import os
from time import sleep

from clientes import telaprincipalcliente
#FUNÇÃO PARA O MENU DE VENDAS!
#PARTE EXCLUSIVA DOS FUNCIONÁRIOS
def sistemavendas():
    os.system('cls')
    sistema = ' '
    while sistema != 0:

        print('''===============================
        ============ Área destinada aos funcionários =============
        ===========================================================
        ============ Cadastrar produto [1] ========================
        ============ Visualizar produto [2] =======================
        ============ Atualizar produto [3] ========================
        ============ Deletar Produto [4] ==========================
        ============ Sair do sistema [5] ==========================
        ===========================================================

        ''')
        sistema = input('Escolha uma opção: ')
        if sistema == '1': # acessa a parte de cadastrar os produtos caso digite 1
            cadastroproduto()

        elif sistema == '2': # acessa a parte de visualizar o produto cadastrado caso digite 2
            visualizarproduto()

        elif sistema == '3': # acessa a parte de atualizar o produto cadastrado caso digite 3
            atualizarproduto()

        elif sistema == '4': # acessa a parte de atualizar o produto cadastrado caso digite 4
            deletarproduto()
        
        elif sistema == '5': # caso queira sair do sistema
            print('Obrigado, volte sempre!')
            break
        else:
            print('Opção inválida') # retorna inválido caso digite uma opção inválida


#DICIONÁRIO PARA FACILITAR OS TESTES!
dicionarioproduto = {

        'produto1': ['categoria', 'preço', 'marca', 'durabilidade'],
        'produto2': ['categoria', 'preço', 'marca', 'durabilidade']

}

#FUNÇÃO PARA CADASTRAR PRODUTOS!
def cadastroproduto(): # cadastra um produto no sistema
    os.system('cls')
    print(''' Bem vindo ao cadastramento de produto!
    Vamos cadastrar o produto desejado!
    ''')
    produto = input('Digite o nome do produto:') # funcionário digita o nome do produto que será usado como chave
    categoria = input('Digite a categoria do produto: ') # digita a categoria do produto informado
    preco = input('Digite o preço do produto: ') # digita o preço do produto 
    marca = input('Digite a marca do produto: ') # define a marca do produto
    durabilidade = float(input('Digite a durabilidade do produto em meses: ')) # digita a durabilidade em meses
    while produto not in dicionarioproduto: # usamos a durabilidade como método de controle
        if durabilidade > 1: # se for maior que 1 mês ele entra
            dicionarioproduto[produto] = [produto, categoria, preco, marca, durabilidade] # se for maior que 1, adiciona no dicionario as informações
            print('Produto cadastrado com sucesso!')
            print(f'O produto cadastrado foi {dicionarioproduto[produto]}')
            break
        else:   
            print('Produto com durabilidade inválida!')
            return False # caso a durabilidade for menor que 1 mês, ele retorna erro.
    else:
        print("Produto já cadastrado, tente novamente!")
    
    
        
    sleep(3) # decidimos usar sleep para facilitar a visualização final
    sistemavendas()



#FUNÇÃO PARA VISUALIZAR OS PRODUTOS CADASTRADOS!
def visualizarproduto():
    os.system('cls')
    print(''' Bem vindo, vamos visualizar o produto cadastrado!
          ''')
    produto = input('Qual produto você deseja visualizar: ') # digita qual produto ele quer visualizar
    while produto != dicionarioproduto: # enquanto o produto não estiver no dicionario
        if produto in dicionarioproduto: # se o produto estiver no dicionário ele achar
            print('Produto encontrado!')
            print(dicionarioproduto[produto]) # exibe o produto
            break
        else:
            produto not in dicionarioproduto # se ele não estiver no dicionário retorna falso
            print('Produto não encontrado!')
    
    sleep(3)  # decidimos usar sleep para facilitar a visualização final      
    sistemavendas()

#FUNÇÃO PARA ATUALIZAR OS PRODUTOS CADASTRADOS!
def atualizarproduto():
    os.system('cls')
    print('''Bem vindo, vamos atualizar algum produto já cadastrado!
        ''')
    produto = input('Por favor, digite um produto já cadastrado: ')
    while True: # digita o produto que está cadastrado
        if produto in dicionarioproduto.keys(): # se o produto estiver no dicionário 
            print(dicionarioproduto[produto][0]) # exibe o produto na chave zero
            if produto in dicionarioproduto.keys(): # se o produto estiver dentro do dicionário ele localiza
                print('Localizamos o produto cadastrado!')
                produto_novo = ' '
                produto_novo = input('Qual informação você deseja alterar do produto: ') # escolhe qual informação ele quer atualizar
                if produto_novo == 'Categoria': # se for a categoria, ele acessar a parte de categorias
                    categoria_nova = input('Digite a nova categoria: ') # digita a nova categoria
                    dicionarioproduto[produto][0] = categoria_nova # adiciona a nova categoria
                    print('Categoria atualizada com sucesso!')
                    print(f'Sua nova categoria é {categoria_nova}') # exibe a nova categoria
                    break
                elif produto_novo == 'Preço': # se ele quiser mudar o preço, digita preço
                    preco_novo = input('Digite um preço novo: ') # digita o novo preço
                    dicionarioproduto[produto][1] = preco_novo # guarda o novo preço
                    print('Preço ajustado com sucesso!')
                    print(f'Seu novo preço é de {preco_novo}') # exibe o novo preço
                    break
                elif produto_novo == 'Marca': # caso ele queira alterar a marca do produto
                    marca_nova = input('Digite a nova marca do seu produto: ') # digita a nova marca para o produto
                    dicionarioproduto[produto][2] = marca_nova # insere a nova marca do produto
                    print('Marca alterada com sucesso!')
                    print(f'Sua nova marca é {marca_nova}') # exibe a nova marca
                    break
                elif produto_novo == 'Durabilidade': # caso queira modificar a durabilidade do produto
                    durabi_nova = input('Digite a nova durabilidade do seu produto: ') # insere a nova durabilidade
                    dicionarioproduto[produto][3] = durabi_nova # insere no dicionário a nova durabilidade
                    print('Durabilidade alterada com sucesso!')
                    print(f"Sua durabilidade foi alterada para {durabi_nova}") # exibe a nova durabilidade
                    break
                else:
                    print('Opção não consta no nosso sistema!') # caso ele digite uma opção diferente
                    return False
            print('Obrigado!')
    
    sleep(3)  # decidimos usar sleep para facilitar a visualização final 
    sistemavendas()


#FUNÇÃO PARA DELETAR PRODUTOS CADASTRADOS!
def deletarproduto():
    os.system('cls')
    print('Bem vendo, vamos deletar um produto do seu sistema!')
    deletar = input('Digite o nome do produto que você quer deletar do sistema: ') # digita o produto que ele quer deletar do sistema
    if deletar in dicionarioproduto: # se o produto estiver no sistema ele deleta
        del dicionarioproduto[deletar] # deleta especificamente o produto digitado
        print('Produto deletado com sucesso!')
        print(f'Você deletou o seguinte produto: {deletar}') # exibe o produto no qual foi deletado
        
    else:
        print("Produto não encontrado em nosso sistema!") # caso ele não encontre o produto no sistema
    
    sleep(3) # decidimos usar sleep para facilitar a visualização final
    sistemavendas()


