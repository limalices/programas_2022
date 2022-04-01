from config import *

class Proprietario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))

    casas = db.relationship("Casa", backref = "proprietario")

    def __str__(self) -> str:
        return f'proprietário(a): ({self.id}) {self.nome}, {self.email}, {self.telefone}'

class Casa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    formato = db.Column(db.String(254))

    comodos = db.relationship("Comodo", backref = "casa")

    proprietario_id = db.Column(db.Integer, db.ForeignKey(Proprietario.id), nullable = False)

    def __str__(self) -> str:
        s = f'casa {self.formato}'
        if self.proprietario:
            s += f' é do(a) {str(self.proprietario)}'
        return s

class Comodo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(254))
    dimensoes = db.Column(db.String(254))

    casa_id = db.Column(db.Integer, db.ForeignKey(Casa.id), nullable = False)

    mobilias = db.relationship("Mobilia", backref = "comodo")

    def __str__(self) -> str:
        s = f' cômodo: {self.nome}, {self.dimensoes}'
        #if self.casa:
        s += f' na {str(self.casa)}'
        return s

class Mobilia(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(254))
    funcao = db.Column(db.String(254))
    material = db.Column(db.String(254))

    quarto_id = db.Column(db.Integer, db.ForeignKey(Comodo.id), nullable = True)

    def __str__(self) -> str:
        s = f'Mobília: ({self.id}) {self.nome}, {self.funcao}, {self.material}'
        if self.comodo:
            s += f', no {str(self.comodo)}'
        return s

if __name__ == "__main__":
    if os.path.exists(arquivobd): # se houver o arquivo...
        os.remove(arquivobd) # ...apagar!

    db.create_all() # criar tabelas

    print()
    print("*** TESTE criando objetos")
    print()

    p1 = Proprietario(nome = "Alice", email = "alice@gmail.com", telefone = "123")
    db.session.add(p1)
    db.session.commit()
    print(p1)
    print()

    c1 = Casa(formato = "russa", proprietario = p1)
    db.session.add(c1)
    db.session.commit()
    
    q1 = Comodo(nome = "sala", dimensoes = "6x5 metros", casa = c1)
    q2 = Comodo(nome="banheiro", dimensoes="3x4 metros", casa = c1)

    db.session.add(q1)
    db.session.add(q2)
    db.session.commit()

    # sem lista reversa
    for q in db.session.query(Comodo).filter(Comodo.casa_id == c1.id).all():
        print(q)
    print()

    # com lista reversa
    for q in c1.comodos:
        print(q)
    print()

    print("*** TESTE das mobílias")
    print()
    
    m1 = Mobilia(nome = "armário", funcao = "guardar coisas", material = "madeira", comodo=q1)
    m2 = Mobilia(nome = "espelho", funcao = "ajudar a se arrumar", material = "vidro polido", comodo = q2)

    db.session.add(m1)
    db.session.add(m2)
    db.session.commit()
    
    # quartos da casa, com lista reversa
    for q in c1.comodos:
        print(q)
        for m in q.mobilias:
            print(m)
            print()