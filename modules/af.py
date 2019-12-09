
"""
    File with the definition of an AFN.
"""
from states import State
from states import MultiState

class Af():
    """ Um automato finito """
    def __init__(self, nome=None, alfabeto=None, estados=None, current=None):
        self.alfabeto = alfabeto

        if estados is None:
            self.estados = State('', False, False)
        else:
            self.estados = estados

        self.nome = nome

        self.current = current

        for estado in self.estados:
            if estado.nome == current:
                self.current = estado

    def __str__(self):
        n_l = "\n"
        string = self.nome + n_l + str(self.alfabeto) + n_l + str(self.estados)
        return string

    def __repr__(self):
        return str(self)

    def __doc__(self):
        return self.__class__.__doc__

    def state(self, estado_nome):
        """
        Retorna um State presente no automato dado um nome de estado
        """
        for estado in self.estados:
            if estado.nome == estado_nome:
                return estado
        return None

    def get_trans(self, current, letter):

        transitions = []

        for estado in current.estados:
            state = self.state(estado)
            if state is not None and state.next_state is not None:
                for trans in state.next_state:
                    if trans[0] == letter:
                        transitions.append(trans[1])

        return list(set(transitions))

    def transform_afd(self):
        """
        Algoritmo que transforma a afn em uma afd
        """

        stack = [MultiState([self.current.nome])]
        novos_estados = {}

        while stack:

            current = stack.pop()

            for letter in self.alfabeto:
                trans = self.get_trans(current, letter)
                if not trans:
                    continue

                aux = MultiState(trans)
                current.next_state.append((letter, aux.nome))

                if aux.nome not in novos_estados:
                    stack.append(aux)

            novos_estados[current.nome] = current

        for value in novos_estados:
            for estado in novos_estados[value].estados:
                if self.state(estado).is_final:
                    print(novos_estados[value])
                    novos_estados[value].is_final = True


        estados = []
        for value in novos_estados:
            estados.append(novos_estados[value].get_state())

        return Af(self.nome, self.alfabeto, estados, self.current)
