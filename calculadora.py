def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida."

def calculadora():
    print("Bem-vindo à Calculadora Simples!")
    print("Selecione a operação:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    
    while True:
        try:
            escolha = int(input("Digite a opção (1/2/3/4): "))
            if escolha in [1, 2, 3, 4]:
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
        return

    if escolha == 1:
        print(f"O resultado de {num1} + {num2} é {adicionar(num1, num2)}")
    elif escolha == 2:
        print(f"O resultado de {num1} - {num2} é {subtrair(num1, num2)}")
    elif escolha == 3:
        print(f"O resultado de {num1} * {num2} é {multiplicar(num1, num2)}")
    elif escolha == 4:
        print(f"O resultado de {num1} / {num2} é {dividir(num1, num2)}")

# Chama a função calculadora
calculadora()
