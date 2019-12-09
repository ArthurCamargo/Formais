class State:
    def __init__(self, nome=None, next_state=None, is_final=False, is_initial=False):
        self.nome = nome
        self.next_state = next_state
        self.is_initial = is_initial
        self.is_final = is_final

    def __str__(self):
        string = "%s --> %s" % (self.nome, str(self.next_state))
        if self.is_initial:
            string += "[O]"
        if self.is_final:
            string += "[X]"
        return string

    def __repr__(self):
        string = "%s --> %s" % (self.nome, str(self.next_state))
        if self.is_initial:
            string += "[O]"
        if self.is_final:
            string += "[X]"
        return string

class MultiState:
    def __init__(self, estados):
        self.nome = ''
        self.is_final = False
        estados = sorted(estados)
        self.estados = estados

        for estado in estados:
            self.nome += estado
        self.next_state = []

    def get_state(self):
        return State(self.nome, self.next_state, self.is_final)

    def __str__(self):
        string = ''
        string += self.nome + ' -- ' + str(self.next_state)
        return string

    def __repr(self):
        return self.__str__
