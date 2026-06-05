def saudacao(nome):
    """Retorna uma saudacao personalizada."""
    return f"Olá, {nome}! Bem-vindo ao projeto."


def soma(a, b):
    """Retorna a soma de dois numeros."""
    return a + b


if __name__ == "__main__":
    print(saudacao("Mundo"))
    print(f"2 + 3 = {soma(2, 3)}")
