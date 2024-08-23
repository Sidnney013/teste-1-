def controle_de_acesso():
    cargos_irrestritos = ["gerente", "diretor"]

    dias_uteis = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

    cargo = input("Digite seu cargo: ")
    dia_da_semana = input("Digite o dia da semana: ")

    if cargo in cargos_irrestritos:
        print("Acesso permitido")
    elif cargo == "analista":
        print("Acesso permitido")
    elif cargo == "estagiário":
        if dia_da_semana in dias_uteis:
            print("Acesso permitido")
        else:
            print("Acesso negado")
    else:
        print("Cargo não reconhecido")

controle_de_acesso()