from Codigo.bytebank import Funcionario

def teste_idade():
    funcionario_teste = Funcionario("Teste", '14/05/2002', 4100)
    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()
