prod = []
funcionarios = []
valores  = []
#=====MENU INICIAL==================================#
def main ():
    #==============================#
    #MENU PARA EXEBIÇÃO
    #==============================#
    print("########## CADASTRAR PRODUTOS ##########")
    print("\n")
    print("           1- Cadastrar produtos")
    print("           2- Cadastrar funcionarios")
    print("           3- Exibir produtos  ")
    print("           4- Exibir funcionários")
    print("           5- Valor total dos produtos")  
    print("\n")
    opc = int(input("Açâo desejada: "))
    if opc == 1:
        cadastro_prod()
    elif opc == 2:
        cadastro_func()
    elif opc == 3:
        exibir_prod()
    elif opc == 4:
        exibir_func()
    elif opc == 5:
        soma()
#=====FIM MENU INICIAL===============================#
#====SOMAR==================#
def soma():
        print("Valor total: ", sum(valores))
#====FIM SOMAR===============#
#====EXIBIR PRODUTOS=========#
def exibir_prod():
    print("Produtos e seus valores unitários")
    for i in prod:
        print(i,end = " | ")
    print("\n")
    for j in valores:
      print(j,end = " | ")
#====EXIBIR FUNCIONARIOS=========#
def exibir_func():
    print("Lista de Funcionários")
    for i in funcionarios:
        print(i,end = " ")
#====FIM EXIBIR FUNCIONARIOS=====#
#====CADASTRO DE PRODUTOS==================#
def cadastro_prod():
    while True:
        nome = str(input("Nome do produto: "))
        prod.append(nome)
        val_uni = float(input("Valor unitário: "))
        valores.append(val_uni)
        print("\n")
        op = str(input("Continuar? S/N: "))
        if op == 's' :
            continue
        elif op == 'n' :
            return main()
#====FIM CADASTRO DE PRODUTOS==================#
#====CADASTRO DE PRODUTOS==================#
def cadastro_func():
    while True:
        nome = str(input("Nome: "))
        cod = int(input ("Código: "))
        cpf = str(input ("Cpf: "))
        func = str(input("Função: "))
        ch = str(input  ("Carga horária: "))
        hr_ent=str(input("Horário de entrada: "))
        hr_sai=str(input("Horário de saída: "))
        sal= float(input("Salário: "))
        funcionarios.append(nome)
        funcionarios.append(cod)
        funcionarios.append(cpf)
        funcionarios.append(func)
        funcionarios.append(ch)
        funcionarios.append(hr_ent)
        funcionarios.append(hr_sai)
        funcionarios.append(sal)
        print("\n")
        op = str(input("Continuar? S/N: "))
        if op == 's' :
            continue
        elif op == 'n' :
            return main()
#====FIM CADASTRO DE PRODUTOS==================#
main()
        
    
    

