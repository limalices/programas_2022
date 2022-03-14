# Alice Lima dos Santos - 302 informática

class Contato():
    def __init__(self, nome: str, email: str, telefone: str) -> None:
        self.nome = nome
        self.email = email
        self.telefone = telefone
    
    def solicitar_dados(self, nome, email, telefone):
        nome = input("Digite seu nome: ")
        email = input("Digite seu e-mail: ")
        telefone = input("Digite seu telefone: ")

        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __repr__(self) -> str:
        contato = "Nome: " + self.nome + "\n" + "E-mail: " + self.email + "\n" + "Telefone: " + self.telefone
        return contato

if __name__ == "__main__":
    pessoa = Contato(" ", " ", " ")
    pessoa.solicitar_dados(" ", " ", " ")
    print(pessoa)

#----------------------------------------------------------------------------------------

nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
telefone = input("Digite seu telefone: ")

contato = nome + "\n" + email + "\n" + telefone

print(contato)