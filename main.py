import os
from clientes import telaprincipalcliente
from vendas import sistemavendas

cliente = ' '
os.system('cls')
while cliente != 0:
        
        print('*'*60)
        print('''
        =========== Bem vindos ao Nosso Sistema Integrado! ===========
        ===============  Obrigado pela preferência! ==================
        ========= Administração! [1] ================================
        ========= Quero ser cliente! [2] =============================
        ========= Consultar Promoções! [3] ============================
        ========= Sair do sistema! [4] ===============================
        ==============================================================   
        ''')
        print('*'*60)

        cliente = input('O que você deseja: ')

        if cliente == '1': # caso digfgtite 1, ele acessa o sistema para cadastramento de produtos
            sistemavendas()

        elif cliente == '2': # caso digite 2, ele acessa o sistema para cadastrar os clientes
            telaprincipalcliente()

        elif cliente == '3': # caso ele digite 3, acessa as promoções (EM DESENVOLVIMENTO!)
            print('oi')

        elif cliente == '4': # caso ele digite 4, sai do sistema
            print('Obrigado, volte sempre!')
            break

        else:
            print('Opção inválida') # caso digite uma opção maior que 4 ele retorna uma opção inválida.


