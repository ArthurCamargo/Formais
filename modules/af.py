"""File with the definitions of an AF."""

class State:
    """
    Um State e um estado que possui:
    """
    def __init__(self, nome='', next_state=None, is_inicial=False, is_final=False):
        """
        Construtor de um State, onde:
        - nome uma string
        - is_inicial um bool
        - is_final um bool
        """

        self.nome = nome
        self.is_inicial = is_inicial
        self.is_final = is_final
        self.next_state = next_state

    def __str__(self):
        traco = " -- "
        ini = "[O]"
        final = "[X]"
        string = self.nome + traco + str(self.next_state)

        if self.is_inicial:
            string += ini

        if self.is_final:
            string += final

        return string

    def __repr__(self):
        return str(self)
    def __doc__(self):
        return self.__class__.__doc__

class Af:
    """Classe basica de um de um automato finito."""
    def __init__(self, nome='', alfabeto=None, estados=None):
        """
        Construtor de um afd, onde:

        - alfabeto e uma lista de string
        - estados eh um State
        - nome eh uma string.

        e Retorna um AF

        """
        self.alfabeto = alfabeto

        if estados is None:
            self.estados = State('', False, False)
        else:
            self.estados = estados

        self.nome = nome

    def __str__(self):
        n_l = "\n"
        string = self.nome + n_l + self.alfabeto + n_l + self.estados + n_l
        return string

    def __doc__(self):
        return self.__class__.__doc__
