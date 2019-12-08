
"""
    File with the definition of an AFN.
"""
from af import Af

class Afn(Af):
    """ Um automato finito não determinístico. """
    def __init__(self, nome=None, alfabeto=None, estados=None):
        Af.__init__(self, nome, alfabeto, estados)
    def __str__(self):
        nl = "\n"
        string = self.nome + nl + str(self.alfabeto) + nl + str(self.estados) + nl
        return string
    def __doc__(self):
        return self.__class__.__doc__
