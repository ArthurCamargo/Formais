"""
Arquivo com funcoes utilitarias com proposito mais generico:
    read_file - le um arquivo e retorna uma afn que ele descreve

"""

from afn import Afn

def read_file(file_name):
    """
    Le um arquivo que possui a descricao de um automato
    e retorna um Afn.
    """
    with open(file_name) as myfile:
        lines = myfile.read()
        name = lines.split('=')[0] #Pega o nome do automato

        estados = lines.split('{')[1] #Pega os estados
        estados = estados.split('}')[0]
        estados = estados.split(',')

        alfabeto = lines.split('{')[2] #Pega o alfabeto
        alfabeto = alfabeto.split('}')[0]
        alfabeto = alfabeto.split(',')

        inicial = lines.split('}')[2]
        inicial = inicial.split(',')[1]

        finals = lines.split('{')[3]
        finals = finals.split('}')[0]
        finals = finals.split(',')

    myafn = Afn(name, alfabeto, estados,)
    print(myafn)
    print(name)
    print(estados)
    print(alfabeto)
    print(inicial)
    print(finals)
    print(lines)
