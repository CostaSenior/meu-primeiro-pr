from hello import saudacao, soma


def test_saudacao():
    assert saudacao("Maria") == "Olá, Maria! Bem-vindo ao projeto."
    assert saudacao("João") == "Olá, João! Bem-vindo ao projeto."


def test_soma():
    assert soma(2, 3) == 5
    assert soma(0, 0) == 0
    assert soma(-1, 1) == 0
