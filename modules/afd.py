"""
File with the definition of an AFD.
"""
from af import Af

class Afd(Af):
    """ Um automato finito determinístico. """
    def __init__(self, nome=None, alfabeto=None, estados=None):
        Af.__init__(self, nome, alfabeto, estados)

    def __str__(self):
        n_l = "\n"
        string = self.nome + n_l + str(self.alfabeto) + n_l + str(self.estados)
        return string

    def __doc__(self):
        return self.__class__.__doc__
