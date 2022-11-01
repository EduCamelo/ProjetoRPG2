def NomeComNumero(valor_campo, nome_campo, listaErros):
    if any(char.isdigit() for char in valor_campo):
        listaErros[nome_campo] = 'Não inclua números'

def NaoTemNumero(valor_campo, idade_campo, listaErros):
    if any(int.isdigit() for int in valor_campo):
        listaErros[idade_campo] = 'Inclua apenas números!'


def Classe(classe_Person, listaErros):
    if classe_Person == None:
        listaErros['classe_Person'] = 'Escolha uma classe para o seu personagem'


def raca(Raca, listaErros):
    if Raca == None:
        listaErros['Raça'] = 'Escolha a raça do seu personagem'

def SemRumo(destino, listaErros):
    if destino == None:
        listaErros['destino'] = 'Escolha seu destino'