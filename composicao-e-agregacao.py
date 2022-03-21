class Quarto:
    def __init__(self, nome="", dimensoes="", casa=None):
        self.nome = nome
        self.dimensoes = dimensoes
        if casa is None: # regra da composição
            raise Exception("Um quarto precisa ter casa")
        self.casa = casa

    def __str__(self): # expressão do objeto em forma textual
        s = f'Quarto: {self.nome}, {self.dimensoes}'
        if self.casa:
            s+= f', na casa: {str(self.casa)}'
        return s

class Mobilia:
    def __init__(self, nome="", funcao="", material="", quarto=None):
        self.nome = nome
        self.funcao = funcao
        self.material = material
        self.quarto = quarto

    def __str__(self): # expressão do objeto em forma textual
        s = f'Mobília: {self.nome}, '+\
               f'{self.funcao}, {self.material}'
        if self.quarto:
            s += f', localizada em: {str(self.quarto)}'
        return s

class Casa:
    def __init__(self, formato="", quartos=None):
        self.formato=formato
        self.quartos=quartos

    def __str__(self):
        s = f'Casa: {self.formato}'
        if self.quartos:
            for quarto in self.quartos:
                s += f', possui: {str(quarto)}'
            return s

if __name__ == "__main__": # teste das classes

    c1 = Casa(formato="Germânica")
    print(c1)
    
    q1 = Quarto(nome="Sala", dimensoes="6x5 metros", casa=c1)
    print(q1)

    m1 = Mobilia(nome = "Armário", funcao = "Guardar coisas", 
        material = "Madeira", quarto=q1) # quarto é opcional
    print(m1)

    q2 = Quarto(nome="Banheiro", dimensoes="3x4 metros", casa=c1)

    c1.quartos[q1, q2]
    print(c1)