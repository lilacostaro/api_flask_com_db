from models import Pessoas

# Insere dados na tabela pessoas
def insere_pessoas():
    pessoa = Pessoas(nome="João", idade=35)
    print(pessoa)
    pessoa.save()

# Consulta dados na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)

    #pessoa = Pessoas.query.filter_by(nome='Camila').first()
    #print(pessoa.idade, pessoa.nome, pessoa.id)

# Altera dados na tabela pessoas
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Camila').first()
    pessoa.idade = 21
    pessoa.save()

# Deleta dados na tabela pessoas
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='João').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    consulta_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
