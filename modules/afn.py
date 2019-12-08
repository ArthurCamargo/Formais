
"""
    File with the definition of an AFN.
"""
from afd import Afd
from af import Af
from af import State

class Afn(Af):
    """ Um automato finito não determinístico. """
    def __init__(self, nome=None, alfabeto=None, estados=None, current=None):
        Af.__init__(self, nome, alfabeto, estados)

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

    def concat_trans(self, tup):
        """
        Recebe um set de tuplas de transicoes e une as que possuem
        a mesma letra de transicao retornando uma lista de transicoes
        """
        new_trans = []
        for letter in self.alfabeto:
            name = ''
            for t in tup:
                if t[0] == letter:
                    name += t[1]
            if name != '':
                new_trans.append((letter, name))
        return new_trans

    def afd_state(self, estado):
        """
        Recebe um estado de um afn e o transforma em um afd
        """
        new_trans = self.concat_trans(estado.next_state)
        return State(estado.nome, new_trans, estado.is_final, estado.is_final)

    def sanitize_states(self, states):
        """
        Dado uma lista de State, garante que eles sejam deterministicos
        e retorna uma nova lista de estados
        """
        new_states = []
        for state in states:
            new_states.append(self.afd_state(state))

        return new_states

    def new_state(self, estados):
        """
        Recebe uma lista de estados e cria um State novo que os junta
        e possui transicoes como a uniao das transicoes dos itens da
        lista
        """
        nome = ''
        final = False
        transicoes = set()
        for estado in estados:
            nome += estado
            state = self.state(estado)
            transicoes.update(state.next_state)

            if state.is_final:
                final = True

        #for trans in transicoes:
            #if trans.is_final:
                #final = True

        if self.state(nome) is not None:
            transicoes = self.concat_trans(transicoes)

        print("t", transicoes)

        new_state = State(nome, transicoes, False, final)
        return new_state

    def add_trans(self, estado, trans):
        """
        Recebe um estado e uma transicao e adiciona essa transicao
        a esse estado
        """
        state = self.state(estado)

        if state is not None:
            state.add_trans(trans)

    def peak(self, letter):
        """
        Anda com o estado atual para o proximo estado dado uma letra
        se houver mais de 1 estado para qual ele vai retorna um novo estado
        com a juncao dos estados, se nao houver como andar retorna None
        """
        estado = self.current.peak(letter)

        if len(estado) == 1:
            return  self.state(estado[0])

        return self.new_state(estado)

    def transform_afd(self):
        """
        Algoritmo que transforma a afn em uma afd
        """

        visited = set()
        tmp = [self.current.nome]
        myafd = Afn(self.nome, self.alfabeto, [], None)

        while len(tmp) != 0:
            myafd.current = tmp.pop()
            if myafd.current not in visited:

                visited.add(myafd.current)
                myafd.estados.append(State(myafd.current))

                for letter in self.alfabeto:
                    if myafd.current is not None:
                        tmp.append(myafd.peak(letter))
                        print(tmp)

        myafd.estados = self.sanitize_states(myafd.estados)
