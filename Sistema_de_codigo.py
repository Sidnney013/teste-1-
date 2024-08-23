# Sistema de controle de acesso em um escritório

# Função para verificar o acesso com base no cargo e no dia da semana
def verificar_acesso(cargo, dia_da_semana):
    # Definir as regras de acesso para cada cargo
    if cargo == "gerente":
        return "Acesso permitido"
    elif cargo == "analista" e dia_da_semana in ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]:
        return "Acesso permitido"
    elif cargo == "estagiário" e dia_da_semana in ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]:
        return "Acesso permitido"
    else:
        return "Acesso negado"

# Testes do programa
testes = [
    ("gerente", "segunda-feira"),
    ("gerente", "sábado"),
    ("analista", "quarta-feira"),
    ("analista", "domingo"),
    ("estagiário", "sexta-feira"),
    ("estagiário", "sábado")
]

# Executando os testes
resultados = [(cargo, dia, verificar_acesso(cargo, dia)) for cargo, dia in testes]
resultados
