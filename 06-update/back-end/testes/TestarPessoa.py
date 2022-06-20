from geral.config import *
from modelo.Pessoa import Pessoa

def run():
    print("TESTE DE PESSOA")
    
    p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", telefone = "47 99012 3232", endereco = "Blumenau")
    p2 = Pessoa(nome = "Maria Oliveira", email = "molive@gmail.com", telefone = "47 98822 2531", endereco = "Florianópolis")        
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    print(p1, p2)