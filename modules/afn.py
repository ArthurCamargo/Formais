
"""
    File with the definition of an AFN.
"""
from af import Af

class Afn(Af):
    """ Um automato finito não determinístico. """
    def __init__(self, nome=None, alfabeto=None, estados=None):
        Af.__init__(self, nome, alfabeto, estados)
    def __str__(self):
        n_l = "\n"
        string = self.nome + n_l + str(self.alfabeto) + n_l + str(self.estados) + n_l
        return string

    def __repr__(self):
        return str(self)

    def __doc__(self):
        return self.__class__.__doc__
