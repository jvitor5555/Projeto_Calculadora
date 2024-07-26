def entrada():
    
    import os
    
    while True:
        
        try:
            
            
            print(60*"-")
            a = float(input("Informe o Primeiro Valor: \n"))
            b = float(input("Informe o Segundo Valor: \n"))
            print(60*"-")
            c = int(input("Escolha de acordo com a opção desejada: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n -----------------------------------------------------------\n"))
            print(60*"-")
            
            if c == 0:
                print("Encerrando...")
                break
            
            
            calculo = 0
            
            calculo = calcular(a,b,c)
            print(calculo)
            
            
            
        except:
            print(60*"-")
            print("Caro Usuário, Por Favor, Insira Somente Números")
            os.system("timeout 07")
            os.system("cls")
            

def calcular(f,g,h):
    
    resultado = "Sem Informação"
    
    if h == 1:
        conta = f + g
        resultado = "O Resultado de {:.2f} + {:.2f} = {:.2f}".format(f,g,conta)
        return resultado
    elif h == 2:
        conta = f - g
        resultado = "O Resultado de {:.2f} - {:.2f} = {:.2f}".format(f,g,conta)
        return resultado
    elif h == 3:
        conta = f * g
        resultado = "O Resultado de {:.2f} * {:.2f} = {:.2f}".format(f,g,conta)
        return resultado
    elif h == 4:
        conta = f / g
        resultado = "O Resultado de {:.2f} / {:.2f} = {:.2f}".format(f,g,conta)
        return resultado
    elif h == 0:
        resultado = "O Sistema Será Encerrado"
        return resultado
    else:
        resultado = "<Essa Opção Não Existe>"
        return resultado