
# Funções
def elementos (x):
    a = int(input("Informe o 1º número:  "))
    b = int(input("Informe o 2º número:  "))

    if (x == 1):
        sm = a + b
        print("O resultado da", ops.get(operacao), " é: \n")
        print(a, "+", b, "= ", sm)

    if (x == 2):
        sb = a - b
        print("O resultado da" , ops.get(operacao), " é: \n")
        print(a, "-", b, "= ", sb)

    if (x == 3):
        mt = a * b
        print("O resultado da" , ops.get(operacao), " é: \n")
        print(a, "*", b, "= ", mt)

    if (x == 4):
        if (b == 0):
           print("\n OPS! Não é permitido divisão por 0 \n")
        else:
            dv = a / b 
            print("O resultado da" , ops.get(operacao), " é: \n")
            print(a, ":", b, "= ", dv)
        
 
opcao = "S"
ops = {1:"Soma", 2:"Subtração", 3:"Multiplicação", 4:"Divisão"}
nums = ["1","2","3","4"]

print ("## CALCULADORA PY 1.3 ##\n")

while opcao == "S":

    # 1 - Escolha da operação
    print("Selecione: \n 1 - SOMA \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão ")
    operacao = input("\nQual operação matemática desejada realizar: ")
    
    # Caso opção diferente
    while (operacao not in nums):
        operacao = input("\nInforme uma opção válida: 1, 2, 3, 4: ")

    # Se operação escolhida OK executa a função / # operação se torna INTEIRO para conversar com DICIONÁRIO ops
    else:
        print("\nVocê selecionou: ", ops.get(int(operacao)))
        elementos(int(operacao))
    
    # Para encerrar ou não a calculadora
    opcao = input("\nDeseja continuar? S / N: ").upper()
    while (opcao not in "SsNn"):
        opcao = input("\nDeseja continuar? S / N: ").upper()

print ("\n## FIM DO PROGRAMA ##")
