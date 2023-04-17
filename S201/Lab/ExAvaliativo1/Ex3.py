print("Bem vindo, Escolha a forma geometrica que deseja calcular a area:\n")
escolha = int(input("1 -> retangulo, 2-> triangulo, 3 -> Circulo, 0-> Sair: "))
while escolha != 0:
    if escolha == 1:
        base = float(input("Digite a Base do Retangulo: "))
        altura = float(input("Digite a Altura do Retangulo: "))
        if base <= 0 or altura <= 0:
            print("Valores invalidos tente novamente")
        else:
            print("Resultado = ", base*altura)
            escolha = int(input("1 -> retangulo, 2-> triangulo, 3 -> Circulo, 0-> Sair: "))
    elif escolha == 2:
        base = float(input("Digite a Base do Triangulo: "))
        altura = float(input("Digite a Altura do Triangulo: "))
        if base <= 0 or altura <= 0:
            print("Valores invalidos tente novamente")
        else:
            print("Resultado = ", (base*altura)/2)
            escolha = int(input("1 -> retangulo, 2-> triangulo, 3 -> Circulo, 0-> Sair: "))

    elif escolha == 3:
        raio = float(input("Digite o Raio do Circulo: "))
        if raio <= 0:
            print("Valores invalidos tente novamente")
        else:
            print("Resultado = ", raio*raio * 3.14)
            escolha = int(input("1 -> retangulo, 2-> triangulo, 3 -> Circulo, 0-> Sair: "))
    else:
        print("Operação invalida tente novamente")
        escolha = int(input("1 -> retangulo, 2-> triangulo, 3 -> Circulo, 0-> Sair:"))

    print("Voce saiu!")