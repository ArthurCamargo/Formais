
"""
    File with the definition of an AFN.
"""
from states import State
from states import MultiState

class Af():
    """ Um automato finito """
    def __init__(self, nome=None, alfabeto=None, estados=None, initial=None):
        self.alfabeto = alfabeto

        if estados is None:
            self.estados = State('', False, False)
        else:
            self.estados = estados

        self.nome = nome

        self.initial = initial

        for estado in self.estados:
            if estado.nome == initial:
                estado.is_initial = True

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

    def next(self, estado, letter):
        if estado.next_state is not None:
            for prod in estado.next_state:
                if prod[0] == letter:
                    return prod[1]

        return None

    def transform_afd(self):
        """
        Algoritmo que transforma a afn em uma afd
        """

        stack = [MultiState([self.initial])]
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
                if self.state(estado) is not None:
                    if self.state(estado).is_final:
                        novos_estados[value].is_final = True


        estados = []
        for value in novos_estados:
            estados.append(novos_estados[value].get_state())

        return Af(self.nome, self.alfabeto, estados, self.initial)

    def print_grammar(self):
        new_line = "\n"
        flecha = " -> "
        string = "G = ({"
        for i in range(len(self.estados)):
            variavel_num = ord('A')
            variavel_num += i
            string += (chr(variavel_num))
            if i != len(self.estados) - 1:
                string += ", "
        string += "},{"
        for i in range(len(self.alfabeto)):
            variavel_num = ord('a')
            variavel_num += i
            string += (chr(variavel_num))
            if i != len(self.alfabeto) - 1:
                string += ", "
        string += "}, S, P)" + new_line
        string += "P"  + new_line

        dici = {}
        i = 0
        for estado in self.estados:
            dici[estado.nome] = chr(ord('A') + i)
            i += 1


        for estado in self.estados:
            if estado.next_state is not None:
                for prod in estado.next_state:
                    string += dici[estado.nome] + flecha
                    string += prod[0] + " "
                    string += dici[prod[1]] + new_line
            if estado.is_final:
                string += dici[estado.nome] + flecha + new_line
        print(string)

    def remove_useless(self):

        some_use = set()
        for estado in self.estados:
            if estado.next_state is not None:
                for prod in estado.next_state:
                    some_use.add(prod[1])

        for estado in self.estados:
            if estado.nome not in some_use:
                self.estados.remove(estado)

    def totalize(self):
        nome = 'q1'
        for estado in self.estados:
            if nome == estado.nome:
                nome = 'q' + chr(ord(nome[1]) + 1)

        trans = []
        for letter in self.alfabeto:
            trans.append((letter, nome))

        estado_bolha = State(nome, trans)

        useful = False

        for estado in self.estados:
            for letter in self.alfabeto:

                if self.next(estado, letter) is None:

                    useful = True
                    if estado.next_state is not None:
                        estado.next_state.append((letter, nome))
                    else:
                        estado.next_state = [((letter, nome))]

        if useful:
            self.estados.append(estado_bolha)

    def aceita(self, palavra):
        current = self.initial
        for letra in palavra:
            current = self.state(next(current, letra))
            if current is None:
                return False

        return current.is_final


    def mark(self, marked, current, depend_on):
        if not depend_on:
            return marked
        else:
            for cur in current:
                marked[cur] = True
                cur = depend_on[cur]
                marked = self.mark(marked, cur, depend_on)
        return marked

    def minimize(self):
        afd = self.transform_afd()
        afd.remove_useless()
        afd.totalize()

        is_marked = {}
        for i in afd.estados:
            for j in afd.estados:
                if i != j:
                    conj = set()
                    conj.add(i)
                    conj.add(j)
                    depend_on = {conj:[]}
                    is_marked.update({conj:False})

                    #xor
                    if i.is_final != j.is_final:
                        is_marked[conj] = True

                    if is_marked[conj] is False:
                        for letter in afd.alfabeto:

                            next_1 = afd.next(i, letter)
                            next_2 = afd.next(j, letter)

                            state_1 = self.state(next_1)
                            state_2 = self.state(next_2)

                            conj_next = set()
                            conj_next.add(state_1)
                            conj_next.add(state_2)

                            if conj_next in depend_on:
                                depend_on[conj_next].append(conj)
                            else:
                                depend_on.update({conj_next:conj})
                    else:
                        is_marked = afd.mark(is_marked, [conj], depend_on)
                    print(is_marked)
        print(is_marked)
