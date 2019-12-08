"""
Arquivo com funcoes utilitarias com proposito mais generico:
    read_file - le um arquivo e retorna uma afn que ele descreve

"""

from afn import Afn
from af import State


def read_estados(line):
    """retorna um lista de estados dado uma linha de arquivo"""
    estados = line.split('{')[1] #Pega os estados
    estados = estados.split('}')[0]
    estados = estados.split(',')

    return estados

def read_alfabeto(line):
    """retorna um alfabeto dado uma linha"""
    alfabeto = line.split('{')[2] #Pega o alfabeto
    alfabeto = alfabeto.split('}')[0]
    alfabeto = alfabeto.split(',')

    return alfabeto

def read_inicial(line):
    """retorna o estado inicial dado uma linha"""
    inicial = line.split('}')[2]
    inicial = inicial.split(',')[1]

    return inicial

def read_nome(line):
    """retorna o nome do automato dado uma linha"""
    name = line.split('=')[0] #Pega o nome do automato

    return name

def read_initial(line):
    """retorna o estado inicial dado uma linha"""
    initial = line.split('}')[2]
    initial = initial.split(',')[1]

    return initial

def read_final(line):
    """retorna os estados finais do automato dado uma linha"""
    final = line.split('{')[3]
    final = final.split('}')[0]
    final = final.split(',')

    return final

def read_trans(lines):
    """retorna uma lista de transicoes dado varias linhas"""
    transicoes = []
    for line in lines:
        next_state = line.rsplit('=')[1]

        line = line.rsplit('=')[0]
        line = line.strip("()")
        line = line.split(",")

        current_state = line[0]
        letter = line[1]

        entrada = current_state, letter

        transicoes.append((entrada, next_state))


    return transicoes

def embed_transitions(estado, transicoes):
    """
    Dado uma lista de estados, cria um State e o retorna,
    com suas devidas transicoes
    """
    estados = State()
    t_func = []
    for trans in transicoes:
        if trans[0][0] == estado:
            t_func.append((trans[0][1], trans[1])) #funcao de transicao
            estados = State(estado, t_func)
    return estados

def mark_ini(estados, inicial):
    """
    Dado uma lista de States e o estado inicial,
    marca o estado inicial
    """
    for estado in estados:
        if estado.nome == inicial:
            estado.is_inicial = True

def mark_fin(estados, finals):
    """
    Dado uma lista de States e uma lista de estados finais,
    marca os estados finais
    """
    for final in finals:
        for estado in estados:
            if estado.nome == final:
                estado.is_final = True

def read_file(file_name):
    """
    Le um arquivo que possui a descricao de um automato
    e retorna um Afn.
    """
    with open(file_name) as myfile:
        lines = myfile.read()

        name = read_nome(lines)
        estados_nomes = read_estados(lines)
        alfabeto = read_alfabeto(lines)
        initial = read_initial(lines)
        finals = read_final(lines)
        transicoes = read_trans(lines.split()[2:])

    estados = []
    for estado in estados_nomes:
        estados.append(embed_transitions(estado, transicoes))

    mark_ini(estados, initial)
    mark_fin(estados, finals)

    myafn = Afn(name, alfabeto, estados, initial)


    return myafn
