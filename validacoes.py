#Essa função serve para validar o CPF do cliente.
def cadastrocpf(cpf):
    # fLAVIUS, RETIRAMOS ESSA VALIDAÇÃO DA INTERNET, NÃO CONSEGUI ACHAR O LINK
    # NÃO CONSEGUIMOS DESENVOLVER O VALIDADOR DE CPF
    #validação do CPF do cliente
    cpf = [int(char) for char in cpf if char.isdigit()]
 
    if len(cpf) != 11: #faz a verificação se o CPF do cliente tem mesmo 11 dígitos
        return False
    
    if cpf == cpf [::-1]: #verifica se tem todos os números iguais, pois mesmos com os números sendo considerados inválidos, eles passam na verificação
        return False

    for i in range(9, 11): #valida os dois dígitos verificadores
        valor = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digito = ((valor * 10) % 11) % 10
        if digito != cpf[i]:
            return False
    return True


def validemail(email):
    
    tam = len(email) #aqui ele faz a contagem da lista de email
    lista_cara = ['@', '_', '.'] # decidimos levar em consideração apenas esses 3 caracteres de validação
    cont=0
    for i in range(0, 3):
        for j in range (0, tam -1):
            if lista_cara[i] == email[j]:
                cont += 1
    if cont>=2 and cont<=3:
        return True
    else:
        return False  

           
                
    